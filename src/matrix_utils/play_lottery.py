import os
import json
from matrix_utils.configs import Config



class PlayLottery:
    def __init__(self) -> None:
        self.talent_counter = Config.BASE_COUNTER
        self.will_power_counter = Config.BASE_COUNTER
        self.magnet_is_on = False
        self.magnet_counter = 0
        self.all_cards_number = Config.TOTAL_NFTS + Config.ENHANCE_COUNT
        if not os.path.exists(Config.GAME_DATA_DIR):
            os.makedirs(Config.GAME_DATA_DIR)

    def start(self):
        collection = open(Config.GAME_DATA_DIR + 'suffled_nft_collection.json', 'r')
        collection_data = json.load(collection)
        # print('starter_place: ',collection_data['starter'])
        return collection_data

    def check_magnets_win(self, collection, condidate):
        magnet_winners = []
        if collection['collection'][condidate]['properties'].get('is_magnet'):
            magnet_winners.append(condidate)
            return magnet_winners, True

        if condidate == 0:
            if collection['collection'][self.all_cards_number-1]['properties'].get('is_magnet'):
                magnet_winners.append(self.all_cards_number-1)
            if collection['collection'][1]['properties'].get('is_magnet'):
                magnet_winners.append(1)

            if len(magnet_winners) > 0:
                return magnet_winners, True
        
        elif condidate == self.all_cards_number-1:
            if collection['collection'][self.all_cards_number-2]['properties'].get('is_magnet'):
                magnet_winners.append(self.all_cards_number-2)
            if collection['collection'][0]['properties'].get('is_magnet'):
                magnet_winners.append(0)
        
            if len(magnet_winners) > 0:
                return magnet_winners, True
        else:
            if collection['collection'][condidate+1]['properties'].get('is_magnet'):
                magnet_winners.append(condidate+1)
            if collection['collection'][condidate-1]['properties'].get('is_magnet'):
                magnet_winners.append(condidate-1)
        
        if len(magnet_winners) > 0:
            return magnet_winners, True
        else:
            return [condidate], False

    def check_winner(self, collection_item):
        if self.counter == 0 or collection_item['properties'].get('is_breaker'):
            return True
        return False

    def play(self, data=None):
        # printer
        magnet_stole = False
        printer = ""
        winner_place = []
        if data:
            collection_data = data
        else:
            collection_data = self.start()
        condidate = collection_data['starter']
        round = 1
        for i in range(Config.ALL_ROUNDS):
            printer += "round: " + str(round) + "\n"
            printer += "counter is: " + str(self.counter) + "\n"
            printer += "magnet is on? " + str(self.magnet_is_on) + "\n"
            printer += "condidate place: " + str(condidate) + "\n"
            printer += "condidate nft: " + json.dumps(collection_data['collection'][condidate]) + "\n"
            printer += "################################" + "\n"
            if self.magnet_counter != 0:
                self.magnet_counter -= 1
            else:
                self.magnet_is_on = False
            item = collection_data['collection'][condidate]['properties']
            self.counter += item['counter']
            if self.check_winner(collection_data['collection'][condidate]):
                winner_place = [condidate]
                if self.magnet_is_on:
                    winner_place, magnet_stole = self.check_magnets_win(collection_data, condidate)
                printer += "Winners decided" + "\n"
                break
            if item.get('is_double'):
                self.counter += item['counter']
                if self.check_winner(collection_data['collection'][condidate]):
                    winner_place = [condidate]
                    if self.magnet_is_on:
                        winner_place, magnet_stole = self.check_magnets_win(collection_data, condidate)
                    printer += "Winners decided" + "\n"
                    break
            if item.get('is_magnet'):
                self.magnet_is_on = True
                self.magnet_counter = Config.MAGNET_EFFECTIVE_ROUNDS

            # Go to next
            condidate = (condidate * item['mul']) + item['sum']
            if condidate > self.all_cards_number-1:
                condidate = (condidate % self.all_cards_number)
            round += 1
        if len(winner_place) == 0:
            # Go to 51
            printer += f"round {round} decides the winner\n"
            condidate = (condidate * item['mul']) + item['sum']
            if condidate > self.all_cards_number-1:
                condidate = (condidate % self.all_cards_number)
            winner_place = [condidate]
            if self.magnet_is_on:
                winner_place, magnet_stole = self.check_magnets_win(collection_data, condidate)
        winners_nft = []
        for w in winner_place:
            winners_nft.append(collection_data['collection'][w])
        printer += "winners places: " + str(winner_place) + ", winner nfts: " + str(winners_nft) + ", round: " + str(round) + ", was magnet on: " + str(self.magnet_is_on) + "magnet stole" + str(magnet_stole) + "\n"
        printer += "**********************************************\n"
        if Config.STORE_GAME_PROCCESS:
            with open('winners.txt', 'a') as f:
                f.write(printer)
        return winner_place, winners_nft, round, self.magnet_is_on, magnet_stole

