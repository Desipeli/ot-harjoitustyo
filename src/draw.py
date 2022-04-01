
import pygame

from deck import Deck

class Draw:
    def __init__(self, info):
        self.info = info

    def draw(self):
        # draw menu buttons
        if self.info.game_stage == 0:
            for b in self.info.menu_buttons:
                b.draw()
        

        # draw deck only if cards left
        if self.info.game_stage == 1:
            if len(self.info.match.deck.see_deck()) > 0:
                self.draw_deck()
            if len(self.info.match.player_hand) > 0:
                i = 0
                for c in self.info.match.player_hand:
                    card_width = self.info.match.deck.get_back().image.get_width()
                    x = (self.info.screen.get_width()-4*card_width)/2 + i*card_width
                    y = self.info.screen.get_height()-self.info.match.deck.get_back().image.get_height()
                    pos = (x, y)
                    self.draw_card(c, pos)
                    i += 1

    def draw_card(self, card, pos):
        self.info.screen.blit(card.image, pos)

    def draw_deck(self):
        self.info.screen.blit(self.info.match.deck.get_back().image, self.info.deck_pos)


