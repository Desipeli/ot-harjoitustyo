import imp
import pygame

class Draw:
    def __init__(self, info):
        self.info = info

    def draw(self):
        if self.info.game_stage == 0:
            for b in self.info.menu_buttons:
                b.draw()
        


        #Draw all cards test
        #if self.info.game_stage == 1:
        #    for i in range(52):
        #        self.info.screen.blit(self.info.cards[i].image, (i*((self.info.screen.get_width()/52)),200))

