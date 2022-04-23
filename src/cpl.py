from calc import Calcs


# Computer player logic
class Cpl:
    def __init__(self):
        self.calcs = Calcs()

    def play(self, table, computer_hand, player_collected):
        # if cards in hand
        # if cards in table
        # check table for combinations
        # evaluate combinations
        # pick cards
        # change turn
        if len(computer_hand) < 1:
            # no cards in hand, return turn to player for now
            return False
        if len(table) < 1:
            # no cards in table, play a card to the table
            return self.choose_which_card_to_table(computer_hand, player_collected)
        else:
            # Check table cards for combinations
            return self.decide_what_cards_to_pick(table, computer_hand, player_collected)

    def choose_which_card_to_table(self, computer_hand, player_collected):
        weakest_card = computer_hand[0]
        for card in computer_hand:
            if self.calcs.card_value(card, player_collected) < self.calcs.card_value(weakest_card, player_collected):
                weakest_card = card
        return ("card_to_table", weakest_card)

    def decide_what_cards_to_pick(self, table, computer_hand, player_collected):
        all_combinations = self.calcs.find_all_table_combinations(table.copy(), player_collected)
        result = self.calcs.check_best_combination_for_computer(all_combinations, computer_hand, table)
        if result:
            hand_card = result[0]
            table_cards = result[1]
            return ("cards_to_computer", hand_card, table_cards)
        else: # No possible combinations, play card to table
            return self.choose_which_card_to_table(computer_hand, player_collected)
