import pygame
from ui.game_buttons import Buttons
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
        # 0 = menu, 1 = game table, 3 = show statistics, 4 = settings
        self.game_stage = 0
        self.screen = pygame.display.set_mode([1366, 768])
        pygame.display.set_caption("Kasino")
        self.font = pygame.font.SysFont("Corbel", 35)

        self.info = info.Info()
        self.info.screen = self.screen
        self.info.font = self.font

        Buttons(self.screen, self.info)
        # Load images
        self.cards = load_cards()
        self.backs = load_backs()

        self.info.cards = self.cards
        self.info.backs = self.backs
        self.info.settings.backside = self.backs[0]
        self.info.game_log = LogWindow(self.screen)

        self.loop = Loop(self.info)


if __name__ == "__main__":
    Game()
