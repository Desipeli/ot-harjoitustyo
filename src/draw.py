
import pygame

from deck import Deck

class Draw:
    def __init__(self, info):
        self.info = info

    def draw(self):
        if self.info.game_stage == 0:
            for b in self.info.menu_buttons:
                b.draw()
        
        if self.info.game_stage == 1:
            self.draw_deck()
        

    def draw_deck(self):
        #for i in range(len(self.info.deck.see_full_deck())):
            #self.info.screen.blit(self.info.backs[0].image, (30, self.info.screen.get_height()/2 - self.info.backs[0].image.get_height()/2))
        if self.info.match:
            self.info.screen.blit(self.info.match.deck.get_back().image, self.info.deck_pos)

        #Draw all cards test
        #if self.info.game_stage == 1:
        #    for i in range(52):
        #        self.info.screen.blit(self.info.cards[i].image, (i*((self.info.screen.get_width()/52)),200))

