import random


class Deck:
    """ Class for all of the deck functions """

    def __init__(self, cards, back):
        """ Constructor

            Args:
                cards: Cards which build the deck
                back: Back side of the cards
        """
        self.__full_deck = cards
        self.__cards = []
        self.__back = back
        self.assemble_deck()
        random.shuffle(self.__cards)

    def assemble_deck(self):
        """ Depleted deck can be set to original state """
        self.__cards = []
        for card in self.__full_deck:
            self.__cards.append(card)

    def see_deck(self):
        """ Return copy of the current deck """

        return self.__cards.copy()

    def see_full_deck(self):
        """ Return copy of the deck in original state """

        return self.__full_deck.copy()

    def pick_top(self):
        """ remove and return the top(last in the list) card of the deck """

        if len(self.__cards) > 0:
            return self.__cards.pop()

    def get_back(self):
        """ Return the back side of the card """

        return self.__back

    def shuffle(self):
        """ Shuffle the deck """

        random.shuffle(self.__cards)
