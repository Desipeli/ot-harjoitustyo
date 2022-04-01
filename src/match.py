import pygame

class Match:
    def __inti__(self, info, deck):
        self.player_hand = []
        self.computer_hand = []
        self.deck = deck
        self.table = []
        self.turn = True # t = player, f = computer
        self.round = 1
        self.points_player = 0
        self.points_computer = 0