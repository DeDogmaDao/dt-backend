import json
from .configs import Config
from project.nft.enums import Side, CounterType



class PlayLottery:
    def __init__(self, collection_queryset, starter) -> None:
        self.talent_counter = Config.BASE_TALENT_COUNTER
        self.will_power_counter = Config.BASE_WILL_COUNTER
        self.magnet_is_on = False
        self.magnet_counter = 0
        self.all_cards_number = collection_queryset.count()
        self.collection_data = collection_queryset
        self.starter = starter

    def check_magnets_win(self, collection, candidate):
        magnet_winners = []
        if collection.get(deck_place=candidate).nft.speciality == CounterType.MAGNET:
            magnet_winners.append(candidate)
            return magnet_winners, True

        if candidate == 0:
            if collection.get(deck_place=self.all_cards_number).speciality == CounterType.MAGNET:
                magnet_winners.append(self.all_cards_number)
            if collection.get(deck_place=collection.first()+1).nft.speciality == CounterType.MAGNET:
                magnet_winners.append(2)

            if len(magnet_winners) > 0:
                return magnet_winners, True
        
        elif candidate == self.all_cards_number:
            if collection.get(deck_place=self.all_cards_number-1).nft.speciality == CounterType.MAGNET:
                magnet_winners.append(self.all_cards_number-1)
            if collection.first().nft.speciality == CounterType.MAGNET:
                magnet_winners.append(1)
        
            if len(magnet_winners) > 0:
                return magnet_winners, True
        else:
            if collection.get(deck_place=candidate+1).nft.speciality == CounterType.MAGNET:
                magnet_winners.append(candidate+1)
            if collection.get(deck_place=candidate-1).nft.speciality == CounterType.MAGNET:
                magnet_winners.append(candidate-1)
        
        if len(magnet_winners) > 0:
            return magnet_winners, True
        else:
            return [candidate], False

    def check_winner(self, collection_item):
        if self.talent_counter == self.will_power_counter or \
                collection_item.nft.speciality == CounterType.COUNTER_BREAKER:
            return True
        return False

    def play(self):
        # printer
        magnet_stole = False
        printer = ""
        winner_place = []
        chosen_card = []
        candidate = self.starter
        round = 1
        while self.talent_counter < 51 and self.will_power_counter < 51:
            item = self.collection_data.get(deck_place=candidate)

            printer += "round: " + str(round) + "\n"
            printer += "will power counter is: " + str(self.will_power_counter) + "\n"
            printer += "talent counter is: " + str(self.talent_counter) + "\n"
            printer += "magnet is on? " + str(self.magnet_is_on) + "\n"
            printer += "candidate place: " + str(candidate) + "\n"
            printer += "candidate nft: " + str(item.deck_place) + "\n"
            printer += "################################" + "\n"
            if self.magnet_counter != 0:
                self.magnet_counter -= 1
            else:
                self.magnet_is_on = False

            if item.nft.side == Side.WILL:
                self.will_power_counter += item.nft.counter
                chosen_card.append({
                    "deck_place": item,
                    "total_counter": self.will_power_counter,
                    "magnet_status": self.magnet_is_on,
                    "magnet_stole": magnet_stole})
            elif item.nft.side == Side.TALENT:
                self.talent_counter += item.nft.counter
                chosen_card.append({
                    "deck_place": item,
                    "total_counter": self.talent_counter,
                    "magnet_status": self.magnet_is_on,
                    "magnet_stole": magnet_stole})
            if self.check_winner(item):
                winner_place = [candidate]
                if self.magnet_is_on:
                    winner_place, magnet_stole = self.check_magnets_win(self.collection_data, candidate)
                    if magnet_stole:
                        for winner in winner_place:
                            if winner != candidate:
                                chosen_card.append({
                                    "deck_place": item,
                                    "total_counter": 0,
                                    "magnet_status": self.magnet_is_on,
                                    "magnet_stole": magnet_stole})
                printer += "Winners decided" + "\n"
                break
            if item.nft.speciality == CounterType.DOUBLE_COUNTER:
                if item.nft.side == Side.WILL:
                    self.will_power_counter += item.nft.counter
                    chosen_card[-1]["total_counter"] = self.will_power_counter
                elif item.nft.side == Side.TALENT:
                    self.talent_counter += item.nft.counter
                    chosen_card[-1]["total_counter"] = self.talent_counter

                if self.check_winner(item):
                    winner_place = [candidate]
                    if self.magnet_is_on:
                        winner_place, magnet_stole = self.check_magnets_win(self.collection_data, candidate)
                        if magnet_stole:
                            for winner in winner_place:
                                if winner != candidate:
                                    chosen_card.append({
                                        "deck_place": item,
                                        "total_counter": 0,
                                        "magnet_status": self.magnet_is_on,
                                        "magnet_stole": magnet_stole})
                    printer += "Winners decided" + "\n"
                    break
            if item.nft.speciality == CounterType.MAGNET:
                self.magnet_is_on = True
                self.magnet_counter = Config.MAGNET_EFFECTIVE_ROUNDS

            # Go to next if not balanced yet
            if self.talent_counter < 51 and self.will_power_counter < 51:
                candidate = (candidate * item.nft.multiply_num) + item.nft.sum_num
                if candidate > self.all_cards_number:
                    candidate = (candidate % self.all_cards_number)
            round += 1
        if len(winner_place) == 0:
            # Go to 51
            printer += f"round {round} decides the winner\n"
            winner_place = [candidate]
            # item = self.collection_data.get(deck_place=candidate)
            # chosen_card.append({
            #     "deck_place": item,
            #     "total_counter": 0,
            #     "magnet_status": self.magnet_is_on})
            if self.magnet_is_on:
                winner_place, magnet_stole = self.check_magnets_win(self.collection_data, candidate)
                item = self.collection_data.get(deck_place=candidate)
                if magnet_stole:
                    for winner in winner_place:
                        if winner != candidate:
                            chosen_card.append({
                                "deck_place": item,
                                "total_counter": 0,
                                "magnet_status": self.magnet_is_on,
                                "magnet_stole": magnet_stole})
        winners_nft = []
        winners = self.collection_data.filter(deck_place__in=winner_place)
        return winners, chosen_card
        # return winner_place, winners_nft, round, self.magnet_is_on, magnet_stole

