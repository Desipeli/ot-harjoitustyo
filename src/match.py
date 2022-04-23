from cpl import Cpl
from calc import Calcs

class Match:
    def __init__(self, info):
        self.info = info
        self.cpl = Cpl(info)
        self.calc = Calcs()
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
        self.table_combinations = [] # This must be updated every time table is updated
        self.info_text_computer = ""
        self.info_text_player = ""

    def start_round(self):
        self.deal_cards(True)

    def update_table_combinations(self):
        self.table_combinations = self.calc.find_all_table_combinations(self.table, self.player_collected_cards)
        #print(self.table_combinations)

    def deal_cards(self, start_of_round):
        for i in range(2):
            if self.round % 2 == 1:  # Start by dealing player first
                self.info_text_player = "Your turn"
                self.deal_two_cards_to(self.player_hand)
                self.deal_two_cards_to(self.computer_hand)
                if start_of_round:
                    self.deal_two_cards_to(self.table)
            else:
                self.info_text_player = "computer's turn"
                self.deal_two_cards_to(self.computer_hand)
                self.deal_two_cards_to(self.player_hand)
                if start_of_round:
                    self.deal_two_cards_to(self.table)
        self.update_table_combinations()

    def deal_two_cards_to(self, target):
        target.append(self.deck.pick_top())
        target.append(self.deck.pick_top())

    def check_if_player_can_pick_cards(self):
        if len(self.player_chosen_table_cards) > 0:  # Player has chosen cards from table
            for c in self.player_chosen_table_cards:
                if c.v_table > self.player_chosen_hand_card.v_hand:
                    self.info_text_player = "You can't pick cards of higher value"
                    return False
            if sum([x.v_table for x in self.player_chosen_table_cards]) % self.player_chosen_hand_card.v_hand == 0: # filter most of the cases
                checked = [0 for x in range(len(self.player_chosen_table_cards))]
                print("start checking")
                result = self.calc.check_if_pick_is_allowed(self.player_chosen_table_cards, self.player_chosen_hand_card, checked, 0, 0, {})
                print(result)
                return result
        return False

    def player_action_button(self):
        if self.player_chosen_hand_card == None:
            self.info_text_player = "Choose a card from hand"
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
        
        # table
        #picked_cards = ""
        for c in self.player_chosen_table_cards:
            self.table.remove(c)
            self.add_points_to("player", c)
            self.player_collected_cards.append(c)
            #picked_cards += f"{c.v_table} of {c.suit}, "
        self.player_chosen_table_cards = []
        #self.info_text_player = f"You picked [{picked_cards}] with {self.player_chosen_hand_card.v_hand} of {self.player_chosen_hand_card.suit}"
        self.info_text_player = "Your turn"
        self.player_chosen_hand_card = None
        self.update_table_combinations()

    def play_card_to_table(self):
        self.table.append(self.player_chosen_hand_card)
        self.player_hand.remove(self.player_chosen_hand_card)
        self.info_text_player = "Your turn"
        self.player_chosen_hand_card = None
        self.update_table_combinations()

    def change_turn(self):
        print(len(self.player_hand), len(
            self.computer_hand), len(self.deck.see_deck()))
        if len(self.player_hand) == 0 and len(self.computer_hand) == 0 and len(self.deck.see_deck()) > 0:
            self.deal_cards(False)
        if self.turn:
            self.turn = False
            self.cpl.play()
        else:
            self.turn = True
            self.info_text_player = "Your turn"

    def computer_card_to_table(self, card):
        self.table.append(card)
        self.computer_hand.remove(card)
        self.info_text_computer = f"Computer played {card.v_hand} of {card.suit} to table"
        self.update_table_combinations()
        print("computer played", card.v_hand, card.suit, " to table")

    def move_selected_cards_to_computer(self, hand_card, table_cards):
        self.computer_hand.remove(hand_card)
        self.computer_collected_cards.append(hand_card)
        picked_cards = ""
        for card in table_cards:
            self.table.remove(card)
            self.computer_collected_cards.append(card)
            picked_cards += f"{card.v_table} of {card.suit} ,"
        self.info_text_computer = f"Computer picked [{picked_cards}] with {hand_card.v_hand} of {hand_card.suit}"
        self.update_table_combinations()

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
