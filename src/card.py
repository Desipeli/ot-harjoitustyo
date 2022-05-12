

class Card:
    """ This class has all the information that is needed for a card """

    def __init__(self, v_hand, v_table, suit, image):
        """ Constructor

            Args:
                v_hand: Hand value of this card
                v_table: Table value of this card
                suit: Suit of this card
                image: Image associated with this card
        """

        self.v_hand = v_hand
        self.v_table = v_table
        self.suit = suit
        self.image = image
        self.pos = (0, 0)
