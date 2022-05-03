from settings import Settings


class Info:
    """ Stores information of the app """

    def __init__(self):
        self.screen = None
        self.font = None
        self.game_stage = 0
        self.cards = []
        self.backs = []
        self.menu_buttons = []
        self.game_buttons = []
        self.match_end_buttons = []
        self.settings_buttons = []
        self.deck_pos = (0, 0)
        self.match = None
        self.game_log_text = ["Welcome to Kasino!", "Press play to start a match"]
        self.game_log = None
        self.settings = Settings()
