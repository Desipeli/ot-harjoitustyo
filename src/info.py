import pygame


class Info:
    def __init__(self, screen, font):
        self.screen = screen
        self.font = font
        self.game_stage = 0
        self.cards = []
        self.backs = []
        self.menu_buttons = []
        self.deck = None
        self.deck_pos = (0,0)

        