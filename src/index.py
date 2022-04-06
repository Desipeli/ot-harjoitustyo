import pygame
import sys
from button import Button
from card import Card
from draw import Draw
from deck import Deck
from load_backs import load_backs
from load_cards import load_cards
from event_handler import Events
import info
from loop import Loop



class Game:

    def __init__(self):
        pygame.init()
        # 0 = menu, 1 = game table, 2 =enter highscore, 3 = show highscore
        self.game_stage = 0
        self.screen = pygame.display.set_mode([1366,768])
        self.font = pygame.font.SysFont("Corbel", 35)

        # buttonlists
        b1 = Button(0, self.screen, "Play", (100,60), (self.screen.get_width()/2,self.screen.get_height()/2))
        b2 = Button(1, self.screen, "Highscores", (150,60), (self.screen.get_width()/2,self.screen.get_height()/2+100))
        b3 = Button(2, self.screen, "Exit", (100,60), (50,self.screen.get_height()- 30))
        self.menu_buttons = [b1, b2, b3]
        
        b4 = Button(3, self.screen, "play to table", (150,60), (self.screen.get_width()/2, self.screen.get_height() - 60))
        self.game_buttons = [b4]
        
        self.info = info.Info(self.screen, self.font)
        # Load images
        self.cards = load_cards()
        self.backs = load_backs()

        self.info.cards = self.cards
        self.info.backs = self.backs
        self.info.menu_buttons = self.menu_buttons
        self.info.game_buttons = self.game_buttons

        self.loop = Loop(self.info)




if __name__ == "__main__":
    Game()