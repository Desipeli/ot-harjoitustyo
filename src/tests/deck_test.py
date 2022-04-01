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

    
    def test_pick_top_card(self):
        self.assertEqual((self.deck.pick_top().v_hand, self.deck.pick_top().suit), (13, "3"))

    def test_deck_diminishes(self):
        for i in range(10):
            self.deck.pick_top()
        self.assertEqual(len(self.deck.see_deck()), 42)
    
    def test_deck_get_back(self):
        self.assertEqual(self.deck.get_back(), "test")
    
    def test_see_full_deck(self):
        for i in range(10):
            self.deck.pick_top()
        self.assertEqual(len(self.deck.see_full_deck()), 52)
    
    def test_assemble_deck(self):
        for i in range(10):
            self.deck.pick_top()
        self.deck.assemble_deck()
        self.assertEqual(len(self.deck.see_deck()), 52)

