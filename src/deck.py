from card import Card

class Deck:

    def __init__(self, cards, back):
        self.__full_deck = cards
        self.__cards = []
        self.__back = back
        self.assemble_deck()
        

    def assemble_deck(self):
        for card in self.__full_deck:
            self.__cards.append(card)
        
    def see_deck(self):
        return self.__cards.copy()
    
    def see_full_deck(self):
        return self.__full_deck.copy()
    
    def pick_top(self):
        return self.__cards.pop()
    
    def get_back(self):
        return self.__back

