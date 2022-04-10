import unittest
from calc import Calcs
from card import Card


class TestCalc(unittest.TestCase):
    def setUp(self):
        self.ace = 1
        self.s2 = 1
        self.spades = 0.2
        self.d10 = 2
        self.p_col = [Card(x, x, "spades", "image") for x in range(1,8)]
        self.calc = Calcs()
        self.cards = [
            Card(14, 1, "spades", "image"),
            Card(14, 1, "hearts", "image"),
            Card(16, 10, "diamonds", "image"),
            Card(13, 13, "spades", "image"),
            Card(13, 13, "diamonds", "image"),
            Card(15, 2, "spades", "image")
        ]
    
    def test_card_value_ace_of_spades(self):
        self.assertEqual(self.calc.card_value(self.cards[0], []), self.ace + self.spades)
    
    def test_card_value_ace(self):
        self.assertEqual(self.calc.card_value(self.cards[1], []), self.ace)
    
    def test_card_value_d10(self):
        self.assertEqual(self.calc.card_value(self.cards[2], []), self.d10)
    
    def test_card_value_spades(self):
        self.assertEqual(self.calc.card_value(self.cards[3], []), self.spades)

    def test_card_value_basic(self):
        self.assertEqual(self.calc.card_value(self.cards[4], []), 0)
    
    def test_card_value_spades_when_player_has_half(self):
        self.assertEqual(self.calc.card_value(self.cards[3], self.p_col), 0)
    
    def test_card_value_ace_of_spades_when_player_has_half(self):
        self.assertEqual(self.calc.card_value(self.cards[0], self.p_col), 1)
    
    def test_card_value_2_of_spades(self):
        self.assertEqual(self.calc.card_value(self.cards[5], []), self.s2 + self.spades)
    
    def test_card_value_2_of_spades_when_player_hald(self):
        self.assertEqual(self.calc.card_value(self.cards[5], self.p_col), self.s2)