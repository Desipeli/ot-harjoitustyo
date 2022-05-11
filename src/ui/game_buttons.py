from ui.button import Button


class Buttons:
    def __init__(self, screen, info):
        self.info = info
        self.screen = screen
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
        # statistics buttons
        self.stats_buttons = [b10]

        self.info.menu_buttons = self.menu_buttons
        self.info.game_buttons = self.game_buttons
        self.info.settings_buttons = self.settings_buttons
        self.info.match_end_buttons = self.match_end_buttons
        self.info.stats_buttons = self.stats_buttons
