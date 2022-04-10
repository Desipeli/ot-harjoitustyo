from cpl import Cpl


class Match:
    def __init__(self, info):
        self.info = info
        self.cpl = Cpl(info)
        self.player_hand = []
        self.computer_hand = []
        self.player_collected_cards = []
        self.computer_collected_cards = []
        self.deck = None
        self.table = []
        self.turn = True  # t = player, f = computer
        self.round = 1
        self.points_player = 0
        self.points_computer = 0
        self.player_chosen_hand_card = None
        self.player_chosen_table_cards = []

    def start_round(self):
        self.deal_cards(True)

    def deal_cards(self, start_of_round):
        for i in range(2):
            if self.round % 2 == 1:  # Start by dealing player first
                self.deal_two_cards_to(self.player_hand)
                self.deal_two_cards_to(self.computer_hand)
                if start_of_round:
                    self.deal_two_cards_to(self.table)
            else:
                self.deal_two_cards_to(self.computer_hand)
                self.deal_two_cards_to(self.player_hand)
                if start_of_round:
                    self.deal_two_cards_to(self.table)

    def deal_two_cards_to(self, target):
        target.append(self.deck.pick_top())
        target.append(self.deck.pick_top())

    def check_if_player_can_pick_cards(self):
        if len(self.player_chosen_table_cards) > 0:  # Player has chosen cards from table
            for c in self.player_chosen_table_cards:
                if c.v_table > self.player_chosen_hand_card.v_hand:
                    return False
            if sum([x.v_table for x in self.player_chosen_table_cards]) % self.player_chosen_hand_card.v_hand == 0:
                return True
        return False

    def player_action_button(self):
        if self.player_chosen_hand_card == None:
            return
        if self.check_if_player_can_pick_cards():
            self.move_selected_cards_to_player()
        else:
            if len(self.player_chosen_table_cards) > 0:
                return
            self.play_card_to_table()
        self.change_turn()

    def move_selected_cards_to_player(self):
        # hand
        self.player_collected_cards.append(self.player_chosen_hand_card)
        self.add_points_to("player", self.player_chosen_hand_card)
        self.player_hand.remove(self.player_chosen_hand_card)
        self.player_chosen_hand_card = None
        # table
        for c in self.player_chosen_table_cards:
            self.table.remove(c)
            self.add_points_to("player", c)
            self.player_collected_cards.append(c)
        self.player_chosen_table_cards = []

    def play_card_to_table(self):
        self.table.append(self.player_chosen_hand_card)
        self.player_hand.remove(self.player_chosen_hand_card)
        self.player_chosen_hand_card = None

    def change_turn(self):
        print(len(self.player_hand), len(
            self.computer_hand), len(self.deck.see_deck()))
        if len(self.player_hand) == 0 and len(self.computer_hand) == 0 and len(self.deck.see_deck()) > 0:
            print("deallll")
            self.deal_cards(False)
        if self.turn:
            self.turn = False
            self.cpl.play()
        else:
            self.turn = True

    def computer_card_to_table(self, card):
        self.table.append(card)
        self.computer_hand.remove(card)
        print("computer played", card.v_hand, card.suit, " to table")

    def move_selected_cards_to_computer(self, cc, tc):
        self.computer_collected_cards.append(cc)
        self.add_points_to("computer", cc)
        self.computer_hand.remove(cc)
        print("Computer took", tc[0].v_table,
              tc[0].suit, "with", cc.v_hand, cc.suit)
        for card in tc:
            self.computer_collected_cards.append(card)
            self.add_points_to("computer", card)
            self.table.remove(card)

    def print_hands(self):
        print("player col:", [(c.v_hand, c.suit)
              for c in self.player_collected_cards])
        print("computer col:", [(c.v_hand, c.suit)
              for c in self.computer_collected_cards])

    def add_points_to(self, who, card):
        points = 0
        if card.v_hand == 14 or card.v_hand == 15:
            points += 1
        elif card.v_hand == 16:
            points += 2
        if who == "player":
            self.points_player += points
        else:
            self.points_computer += points
