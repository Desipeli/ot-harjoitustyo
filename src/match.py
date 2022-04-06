import pygame


class Match:
    def __init__(self, info):
        self.info = info
        self.player_hand = []
        self.computer_hand = []
        self.deck = None
        self.table = []
        self.turn = True # t = player, f = computer
        self.round = 1
        self.points_player = 0
        self.points_computer = 0
        self.player_chosen_hand_card = None
        self.player_chosen_table_cards = []
        
    def start_round(self):
        self.deal_cards(True)
    
    def deal_cards(self, start_of_round):
        for i in range(2):
            if self.round % 2 == 1: # Start by dealing player first
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
        if self.player_chosen_hand_card and len(self.player_chosen_table_cards) > 0: #Player has chosen cards from hand & table
            for c in self.player_chosen_table_cards:
                if c.v_table > self.player_chosen_hand_card.v_hand:
                    return False
            if sum([x.v_table for x in self.player_chosen_table_cards]) % self.player_chosen_hand_card.v_hand == 0:
                return True
        return False
    

