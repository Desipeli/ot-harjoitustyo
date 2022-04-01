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