import datetime
import time
import logging
from abc import ABC, abstractmethod
from typing import Tuple, Optional, Callable, List, Iterable

from web3 import Web3
from web3.contract import Contract
from web3.datastructures import AttributeDict
from web3.exceptions import BlockNotFound
from eth_abi.codec import ABICodec
from web3._utils.filters import construct_event_filter_params
from web3._utils.events import get_event_data


logger = logging.getLogger(__name__)


class EventScannerState(ABC):
    @abstractmethod
    def get_last_scanned_block(self) -> int:
        pass

    @abstractmethod
    def start_chunk(self, block_number: int):
        pass

    @abstractmethod
    def end_chunk(self, block_number: int):
        pass

    @abstractmethod
    def process_event(self, block_when: datetime.datetime, event: AttributeDict) -> object:
        pass

    @abstractmethod
    def delete_data(self, since_block: int) -> int:
        pass


class EventScanner:

    def __init__(self, web3: Web3, contract: Contract, state: EventScannerState, events: List, filters: {},
                 max_chunk_scan_size: int = 10000, max_request_retries: int = 30, request_retry_seconds: float = 3.0):
        self.logger = logger
        self.contract = contract
        self.web3 = web3
        self.state = state
        self.events = events
        self.filters = filters
        self.min_scan_chunk_size = 10
        self.max_scan_chunk_size = max_chunk_scan_size
        self.max_request_retries = max_request_retries
        self.request_retry_seconds = request_retry_seconds
        self.chunk_size_decrease = 0.5
        self.chunk_size_increase = 2.0

    @property
    def address(self):
        return self.token_address

    def get_block_timestamp(self, block_num) -> datetime.datetime:
        try:
            block_info = self.web3.eth.getBlock(block_num)
        except BlockNotFound:
            return None
        last_time = block_info["timestamp"]
        return datetime.datetime.utcfromtimestamp(last_time)

    def get_suggested_scan_start_block(self):
        end_block = self.get_last_scanned_block()
        if end_block:
            return max(1, end_block - self.NUM_BLOCKS_RESCAN_FOR_FORKS)
        return 1

    def get_suggested_scan_end_block(self):
        return self.web3.eth.blockNumber - 1

    def get_last_scanned_block(self) -> int:
        return self.state.get_last_scanned_block()

    def delete_potentially_forked_block_data(self, after_block: int):
        self.state.delete_data(after_block)

    def scan_chunk(self, start_block, end_block) -> Tuple[int, datetime.datetime, list]:
        block_timestamps = {}
        get_block_timestamp = self.get_block_timestamp
        def get_block_when(block_num):
            if block_num not in block_timestamps:
                block_timestamps[block_num] = get_block_timestamp(block_num)
            return block_timestamps[block_num]

        all_processed = []

        for event_type in self.events:
            def _fetch_events(_start_block, _end_block):
                return _fetch_events_for_all_contracts(self.web3,
                                                       event_type,
                                                       self.filters,
                                                       from_block=_start_block,
                                                       to_block=_end_block)
            end_block, events = _retry_web3_call(
                _fetch_events,
                start_block=start_block,
                end_block=end_block,
                retries=self.max_request_retries,
                delay=self.request_retry_seconds)

            for evt in events:
                idx = evt["logIndex"]
                assert idx is not None, "Somehow tried to scan a pending block"
                block_number = evt["blockNumber"]
                block_when = get_block_when(block_number)

                logger.debug("Processing event %s, block:%d count:%d", evt["event"], evt["blockNumber"])
                processed = self.state.process_event(block_when, evt)
                all_processed.append(processed)

        end_block_timestamp = get_block_when(end_block)
        return end_block, end_block_timestamp, all_processed

    def estimate_next_chunk_size(self, current_chuck_size: int, event_found_count: int):
        if event_found_count > 0:
            current_chuck_size = self.min_scan_chunk_size
        else:
            current_chuck_size *= self.chunk_size_increase

        current_chuck_size = max(self.min_scan_chunk_size, current_chuck_size)
        current_chuck_size = min(self.max_scan_chunk_size, current_chuck_size)
        return int(current_chuck_size)

    def scan(self, start_block, end_block, start_chunk_size=20, progress_callback=Optional[Callable]) -> Tuple[
        list, int]:
        assert start_block <= end_block
        current_block = start_block
        chunk_size = start_chunk_size
        last_scan_duration = last_logs_found = 0
        total_chunks_scanned = 0
        all_processed = []

        while current_block <= end_block:

            self.state.start_chunk(current_block, chunk_size)
            estimated_end_block = current_block + chunk_size
            logger.debug(
                "Scanning token transfers for blocks: %d - %d, chunk size %d, last chunk scan took %f, last logs found %d",
                current_block, estimated_end_block, chunk_size, last_scan_duration, last_logs_found)

            start = time.time()
            actual_end_block, end_block_timestamp, new_entries = self.scan_chunk(current_block, estimated_end_block)
            current_end = actual_end_block

            last_scan_duration = time.time() - start
            all_processed += new_entries

            if progress_callback:
                progress_callback(start_block, end_block, current_block, end_block_timestamp, chunk_size, len(new_entries))
            chunk_size = self.estimate_next_chunk_size(chunk_size, len(new_entries))
            current_block = current_end + 1
            total_chunks_scanned += 1
            self.state.end_chunk(current_end)

        return all_processed, total_chunks_scanned


def _retry_web3_call(func, start_block, end_block, retries, delay) -> Tuple[int, list]:
    for i in range(retries):
        try:
            return end_block, func(start_block, end_block)
        except Exception as e:
            if i < retries - 1:
                logger.warning(
                    "Retrying events for block range %d - %d (%d) failed with %s, retrying in %s seconds",
                    start_block,
                    end_block,
                    end_block-start_block,
                    e,
                    delay)
                end_block = start_block + ((end_block - start_block) // 2)
                time.sleep(delay)
                continue
            else:
                logger.warning("Out of retries")
                raise


def _fetch_events_for_all_contracts(
        web3,
        event,
        argument_filters: dict,
        from_block: int,
        to_block: int) -> Iterable:
    if from_block is None:
        raise TypeError("Missing mandatory keyword argument to getLogs: fromBlock")
    abi = event._get_event_abi()
    codec: ABICodec = web3.codec
    data_filter_set, event_filter_params = construct_event_filter_params(
        abi,
        codec,
        address=argument_filters.get("address"),
        argument_filters=argument_filters,
        fromBlock=from_block,
        toBlock=to_block
    )

    logger.debug("Querying eth_getLogs with the following parameters: %s", event_filter_params)
    logs = web3.eth.get_logs(event_filter_params)
    all_events = []
    for log in logs:
        evt = get_event_data(codec, abi, log)
        all_events.append(evt)
    return all_events


if __name__ == "__main__":
    import sys
    import json
    from web3.providers.rpc import HTTPProvider
    from tqdm import tqdm
    RCC_ADDRESS = "0x9b6443b0fB9C241A7fdAC375595cEa13e6B7807A"
    ABI = """[
        {
            "anonymous": false,
            "inputs": [
                {
                    "indexed": true,
                    "name": "from",
                    "type": "address"
                },
                {
                    "indexed": true,
                    "name": "to",
                    "type": "address"
                },
                {
                    "indexed": false,
                    "name": "value",
                    "type": "uint256"
                }
            ],
            "name": "Transfer",
            "type": "event"
        }
    ]
    """

    class JSONifiedState(EventScannerState):
        def __init__(self):
            self.state = None
            self.fname = "test-state.json"
            self.last_save = 0

        def reset(self):
            self.state = {
                "last_scanned_block": 0,
                "blocks": {},
            }

        def restore(self):
            try:
                self.state = json.load(open(self.fname, "rt"))
                print(f"Restored the state, previously {self.state['last_scanned_block']} blocks have been scanned")
            except (IOError, json.decoder.JSONDecodeError):
                print("State starting from scratch")
                self.reset()

        def save(self):
            with open(self.fname, "wt") as f:
                json.dump(self.state, f)
            self.last_save = time.time()
        def get_last_scanned_block(self):
            return self.state["last_scanned_block"]

        def delete_data(self, since_block):
            for block_num in range(since_block, self.get_last_scanned_block()):
                if block_num in self.state["blocks"]:
                    del self.state["blocks"][block_num]

        def start_chunk(self, block_number, chunk_size):
            pass

        def end_chunk(self, block_number):
            self.state["last_scanned_block"] = block_number
            if time.time() - self.last_save > 60:
                self.save()

        def process_event(self, block_when: datetime.datetime, event: AttributeDict) -> str:
            log_index = event.logIndex
            txhash = event.transactionHash.hex()
            block_number = event.blockNumber
            args = event["args"]
            transfer = {
                "from": args["from"],
                "to": args.to,
                "value": args.value,
                "timestamp": block_when.isoformat(),
            }
            if block_number not in self.state["blocks"]:
                self.state["blocks"][block_number] = {}

            block = self.state["blocks"][block_number]
            if txhash not in block:
                self.state["blocks"][block_number][txhash] = {}

            self.state["blocks"][block_number][txhash][log_index] = transfer
            return f"{block_number}-{txhash}-{log_index}"

    def run():

        if len(sys.argv) < 2:
            print("Usage: eventscanner.py http://your-node-url")
            sys.exit(1)

        api_url = sys.argv[1]
        logging.basicConfig(level=logging.INFO)

        provider = HTTPProvider(api_url)
        provider.middlewares.clear()

        web3 = Web3(provider)
        abi = json.loads(ABI)
        ERC20 = web3.eth.contract(abi=abi)
        state = JSONifiedState()
        state.restore()
        scanner = EventScanner(
            web3=web3,
            contract=ERC20,
            state=state,
            events=[ERC20.events.Transfer],
            filters={"address": RCC_ADDRESS},
            max_chunk_scan_size=10000
        )
        chain_reorg_safety_blocks = 10
        scanner.delete_potentially_forked_block_data(state.get_last_scanned_block() - chain_reorg_safety_blocks)
        start_block = max(state.get_last_scanned_block() - chain_reorg_safety_blocks, 0)
        end_block = scanner.get_suggested_scan_end_block()
        blocks_to_scan = end_block - start_block

        print(f"Scanning events from blocks {start_block} - {end_block}")
        start = time.time()
        with tqdm(total=blocks_to_scan) as progress_bar:
            def _update_progress(start, end, current, current_block_timestamp, chunk_size, events_count):
                if current_block_timestamp:
                    formatted_time = current_block_timestamp.strftime("%d-%m-%Y")
                else:
                    formatted_time = "no block time available"
                progress_bar.set_description(f"Current block: {current} ({formatted_time}), blocks in a scan batch: {chunk_size}, events processed in a batch {events_count}")
                progress_bar.update(chunk_size)
            result, total_chunks_scanned = scanner.scan(start_block, end_block, progress_callback=_update_progress)

        state.save()
        duration = time.time() - start
        print(f"Scanned total {len(result)} Transfer events, in {duration} seconds, total {total_chunks_scanned} chunk scans performed")

    run()