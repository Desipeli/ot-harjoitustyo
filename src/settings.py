class Settings:
    """ This class contains settings that user can change. """

    def __init__(self):
        """ Initially basic settings. Can be altered through settings menu. """

        self.open_cards = False
        self.backside = None

    def open_cards_change(self):
        if self.open_cards:
            self.open_cards = False
        else:
            self.open_cards = True
