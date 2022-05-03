import pygame
from ui.button import Button
from ui.load_backs import load_backs
from ui.load_cards import load_cards
from ui.log_window import LogWindow
import info
from loop import Loop


class Game:
    """ Class that initializes the game. """

    def __init__(self):
        """ Constructor.
        
            Display's size is defined, info object created and images loaded.
            Game buttons are defined here, probably moved to separete module later.
            Lastly the game loop begins.
        """

        pygame.init()
        # 0 = menu, 1 = game table, 2 =enter highscore, 3 = show highscore, 4 = settings
        self.game_stage = 0
        self.screen = pygame.display.set_mode([1366, 768])
        self.font = pygame.font.SysFont("Corbel", 35)

        # buttonlists
        # Main menu
        b1 = Button(0, self.screen, "Play", (100, 60),
                    (self.screen.get_width()/2, self.screen.get_height()/2))
        b2 = Button(1, self.screen, "Highscores", (150, 60),
                    (self.screen.get_width()/2, self.screen.get_height()/2+100))
        b3 = Button(2, self.screen, "Exit", (100, 60),
                    (self.screen.get_width() -50, self.screen.get_height() - 30))
        b7 = Button(6, self.screen, "Continue", (130, 60),
                    (self.screen.get_width()/2, self.screen.get_height()/2 - 100))
        b8 = Button(7, self.screen, "Settings", (150, 60),
                    (self.screen.get_width()/2, self.screen.get_height()/2+200))
        self.menu_buttons = [b1, b2, b3, b7, b8]
        # Match buttons
        b4 = Button(3, self.screen, "play to table", (150, 60),
                    (self.screen.get_width()/2, self.screen.get_height() - 60))
        b6 = Button(5, self.screen, "Menu", (100, 60),
                    (self.screen.get_width() -50, self.screen.get_height() - 30))
        self.game_buttons = [b4, b6]
        b5 = Button(4, self.screen, "Main menu", (150, 60),
                    (self.screen.get_width()/2, self.screen.get_height()/2 + 100))
        self.match_end_buttons = [b5]
        # Settings buttons
        b9 = Button(8, self.screen, "hidden cards", (160, 60),
                    (self.screen.get_width()/2, self.screen.get_height()/2))
        b10 = Button(9, self.screen, "Menu", (100, 60),
                    (self.screen.get_width() -50, self.screen.get_height() - 30))
        self.settings_buttons = [b9, b10]

        self.info = info.Info()
        self.info.screen = self.screen
        self.info.font = self.font
        # Load images
        self.cards = load_cards()
        self.backs = load_backs()

        self.info.cards = self.cards
        self.info.backs = self.backs
        self.info.settings.backside = self.backs[0]
        self.info.menu_buttons = self.menu_buttons
        self.info.game_buttons = self.game_buttons
        self.info.settings_buttons = self.settings_buttons
        self.info.match_end_buttons = self.match_end_buttons
        self.info.game_log = LogWindow(self.screen)

        self.loop = Loop(self.info)


if __name__ == "__main__":
    Game()
