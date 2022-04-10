# Computer player logic


class Cpl:
    def __init__(self, info):
        self.info = info

    def check_turn(self):
        if not self.info.match.turn:  # f = computers turn
            self.play()

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
        weakest_card = m.computer_hand[0]
        for card in m.computer_hand:
            print("weakest card:", weakest_card.v_hand, weakest_card.suit, self.card_value(
                weakest_card), "card", card.v_hand, card.suit, self.card_value(card))
            if self.card_value(card) < self.card_value(weakest_card):
                weakest_card = card
        self.info.match.computer_card_to_table(weakest_card)

    def card_value(self, card):
        value = 0
        if card.v_hand == 14 or card.v_hand == 15:
            value += 1
        elif card.v_hand == 16:
            value += 1
        if card.suit == "spades":
            # check if player has < half of spades
            if len([x for x in self.info.match.player_collected_cards if x.suit == "spades"]) < 7:
                print("player spades:", len(
                    [x for x in self.info.match.player_collected_cards if x.suit == "spades"]))
                value += 0.2
        return value

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
