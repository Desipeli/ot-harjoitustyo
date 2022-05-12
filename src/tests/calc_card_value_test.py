import unittest
from logic.calc import Calcs
from card import Card


class TestCalc(unittest.TestCase):
    def setUp(self):
        self.card_base = 0.1
        self.ace = 1
        self.s2 = 1
        self.spades = 0.2
        self.d10 = 2
        self.p_col = [Card(x, x, "spades", "image") for x in range(1, 8)]
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
        self.assertEqual(self.calc.card_value(
            self.cards[0], []), self.ace + self.spades + self.card_base)

    def test_card_value_ace(self):
        self.assertEqual(self.calc.card_value(
            self.cards[1], []), self.ace + self.card_base)

    def test_card_value_d10(self):
        self.assertEqual(self.calc.card_value(
            self.cards[2], []), self.d10 + self.card_base)

    def test_card_value_spades(self):
        self.assertEqual(self.calc.card_value(
            self.cards[3], []), self.spades + self.card_base)

    def test_card_value_basic(self):
        self.assertEqual(self.calc.card_value(
            self.cards[4], []), self.card_base)

    def test_card_value_spades_when_player_has_half(self):
        self.assertEqual(self.calc.card_value(
            self.cards[3], self.p_col), self.card_base)

    def test_card_value_ace_of_spades_when_player_has_half(self):
        self.assertEqual(self.calc.card_value(
            self.cards[0], self.p_col), 1 + self.card_base)

    def test_card_value_2_of_spades(self):
        self.assertEqual(self.calc.card_value(
            self.cards[5], []), self.s2 + self.spades + self.card_base)

    def test_card_value_2_of_spades_when_player_hald(self):
        self.assertEqual(self.calc.card_value(
            self.cards[5], self.p_col), self.s2 + self.card_base)
