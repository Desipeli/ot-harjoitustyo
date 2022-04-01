import unittest
from deck import Deck
from card import Card


class TestDeck(unittest.TestCase):
    def setUp(self):
        self.cards = []
        for s in range(4):
            for i in range(1, 14):
                self.cards.append(Card(i,i,str(s), None))
        self.deck = Deck(self.cards, "test")

    
    def test_deck_diminishes(self):
        self.pick_n(10)
        self.assertEqual(len(self.deck.see_deck()), 42)
    
    def test_deck_get_back(self):
        self.assertEqual(self.deck.get_back(), "test")
    
    def test_see_full_deck(self):
        self.pick_n(10)
        self.assertEqual(len(self.deck.see_full_deck()), 52)
    
    def test_assemble_deck(self):
        self.pick_n(10)
        self.deck.assemble_deck()
        self.assertEqual(len(self.deck.see_deck()), 52)
    
    def test_pick_when_empty(self):
        self.pick_n(55)
        self.assertEqual(len(self.deck.see_deck()), 0)
    
    def pick_n(self, n):
        for i in range(n):
            self.deck.pick_top()

