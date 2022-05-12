import unittest
from logic.cpl import Cpl
from card import Card


class TestDeck(unittest.TestCase):
    def setUp(self):
        self.cpl = Cpl()
        self.p_col = []
        self.computer_hand = [
            Card(14, 1, "spades", "image"),
            Card(14, 1, "hearts", "image"),
            Card(8, 8, "spades", "image"),
            Card(8, 8, "clubs", "image")
        ]
        self.table = [
            Card(8, 8, "hearts", "image"),
            Card(4, 4, "spades", "image"),
            Card(2, 2, "hearts", "image")
        ]

    def test_pick_all_cards_spadehigh(self):
        result = self.cpl.play(self.table, self.computer_hand, self.p_col)
        self.assertEqual(result[0], "cards_to_computer")
        self.assertEqual(result[1], self.computer_hand[0])
        self.assertEqual(result[2], self.table)

    def test_pick_spades(self):
        self.computer_hand.pop(1)
        self.computer_hand.pop(0)
        result = self.cpl.play(self.table, self.computer_hand, self.p_col)
        self.assertEqual(result[0], "cards_to_computer")
        self.assertEqual(result[1], self.computer_hand[0])
        self.assertEqual(result[2][0], self.table[0])

    def test_cant_pick(self):
        self.computer_hand = [Card(3, 3, "hearts", "image")]
        result = self.cplresult = self.cpl.play(
            self.table, self.computer_hand, self.p_col)
        self.assertEqual(result[0], "card_to_table")
        self.assertEqual(result[1], self.computer_hand[0])

    def test_cant_pick_weakest_card(self):
        self.computer_hand = [
            Card(3, 3, "spades", "image"),
            Card(3, 3, "clubs", "image"),
        ]
        result = self.cplresult = self.cpl.play(
            self.table, self.computer_hand, self.p_col)
        self.assertEqual(result[0], "card_to_table")
        self.assertEqual(result[1], self.computer_hand[1])

    def test_empty_hand(self):
        self.computer_hand = []
        result = self.cplresult = self.cpl.play(
            self.table, self.computer_hand, self.p_col)
        self.assertEqual(result, False)

    def test_empty_table(self):
        self.table = []
        result = self.cplresult = self.cpl.play(
            self.table, self.computer_hand, self.p_col)
        self.assertEqual(result[0], "card_to_table")
        self.assertEqual(result[1], self.computer_hand[3])
