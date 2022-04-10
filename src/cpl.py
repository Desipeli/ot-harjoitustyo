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
            self.just_some_card()
            m.change_turn()

    def choose_which_card_to_table(self):
        # card = self.info.match.computer_hand[0] # first for now
        # self.info.match.computer_card_to_table(card)
        m = self.info.match
        p_col = m.player_collected_cards
        weakest_card = m.computer_hand[0]
        for card in m.computer_hand:
            if self.calcs.card_value(card, p_col) < self.calcs.card_value(weakest_card, p_col):
                weakest_card = card
        self.info.match.computer_card_to_table(weakest_card)

    def just_some_card(self):
        # For now check if any card matches hand
        m = self.info.match
        found_card = False
        computer_card = None
        table_card = None
        for tc in m.table:
            for cc in m.computer_hand:
                if cc.v_hand == tc.v_table:
                    found_card = True
                    computer_card = cc
                    table_card = tc
        if found_card:
            m.move_selected_cards_to_computer(computer_card, [table_card])
        else:
            self.choose_which_card_to_table()
