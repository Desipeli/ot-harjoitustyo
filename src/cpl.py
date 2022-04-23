from calc import Calcs


# Computer player logic
class Cpl:
    def __init__(self, info):
        self.info = info
        self.calcs = Calcs()

    def play(self):
        m = self.info.match
        # if cards in hand
        # if cards in table
        # check table for combinations
        # evaluate combinations
        # pick cards
        # change turn
        if len(m.computer_hand) < 1:
            # no cards in hand, return turn to player for now
            print("hand < 1")
            m.change_turn()
            return
        if len(m.table) < 1:
            print("table < 1")
            # no cards in table, play a card to the table
            self.choose_which_card_to_table()
            m.change_turn()
        else:
            print("hand and table")
            # Check table cards for combinations
            self.decide_what_cards_to_pick()
            m.change_turn()

    def choose_which_card_to_table(self):
        m = self.info.match
        p_col = m.player_collected_cards
        weakest_card = m.computer_hand[0]
        for card in m.computer_hand:
            if self.calcs.card_value(card, p_col) < self.calcs.card_value(weakest_card, p_col):
                weakest_card = card
        self.info.match.computer_card_to_table(weakest_card)

    def decide_what_cards_to_pick(self):
        m = self.info.match
        all_combinations = self.calcs.find_all_table_combinations(m.table, m.player_collected_cards)
        result = self.calcs.check_best_combination_for_computer(all_combinations, m.computer_hand, m.table)
        if result:
            hand_card = result[0]
            table_cards = result[1]
            m.move_selected_cards_to_computer(hand_card, table_cards)
        else: # No possible combinations, play card to table
            self.choose_which_card_to_table()
