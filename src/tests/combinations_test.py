import unittest
from logic.calc import Calcs
from card import Card


class TestCalc(unittest.TestCase):
    def setUp(self):
        self.calc = Calcs()
        self.cards = [
            Card(14, 1, "spades", "image"),
            Card(14, 1, "hearts", "image"),
            Card(6, 6, "diamonds", "image"),
            Card(8, 8, "spades", "image"),
        ]

    def test_table_combinations_count(self):
        result = self.calc.find_all_table_combinations(self.cards, [])
        self.assertEqual(len(result), 16)

    def test_check_if_pick_is_allowed_yes_2_pairs(self):
        book = {}
        card = Card(8, 8, "hearts", "image")
        checked = [0 for x in range(len(self.cards))]
        self.assertEqual(self.calc.check_if_pick_is_allowed(
            self.cards, card, checked, 0, 0, book), True)

    def test_check_if_pick_is_allowed_yes_all_same(self):
        book = {}
        cards = [
            Card(3, 3, "spades", "image"),
            Card(3, 3, "hearts", "image"),
            Card(3, 3, "diamonds", "image"),
        ]
        card = Card(3, 3, "hearts", "image")
        checked = [0 for x in range(len(cards))]
        self.assertEqual(self.calc.check_if_pick_is_allowed(
            cards, card, checked, 0, 0, book), True)

    def test_check_if_pick_is_allowed_yes_all_different(self):
        book = {}
        cards = [
            Card(2, 2, "spades", "image"),
            Card(3, 3, "hearts", "image"),
            Card(4, 4, "diamonds", "image"),
        ]
        card = Card(9, 9, "hearts", "image")
        checked = [0 for x in range(len(cards))]
        self.assertEqual(self.calc.check_if_pick_is_allowed(
            cards, card, checked, 0, 0, book), True)

    def test_check_if_pick_is_allowed_no_all_same(self):
        book = {}
        cards = [
            Card(3, 3, "spades", "image"),
            Card(3, 3, "hearts", "image"),
            Card(3, 3, "diamonds", "image"),
        ]
        card = Card(4, 4, "hearts", "image")
        checked = [0 for x in range(len(cards))]
        self.assertEqual(self.calc.check_if_pick_is_allowed(
            cards, card, checked, 0, 0, book), False)

    def test_check_if_pick_is_allowed_no_all_different(self):
        book = {}
        cards = [
            Card(2, 2, "spades", "image"),
            Card(3, 3, "hearts", "image"),
            Card(4, 4, "diamonds", "image"),
        ]
        card = Card(10, 10, "hearts", "image")
        checked = [0 for x in range(len(cards))]
        self.assertEqual(self.calc.check_if_pick_is_allowed(
            cards, card, checked, 0, 0, book), False)

    def test_check_if_pick_is_allowed_no_one_allowed_pair(self):
        book = {}
        cards = [
            Card(2, 2, "spades", "image"),
            Card(3, 3, "hearts", "image"),
            Card(4, 4, "diamonds", "image"),
        ]
        card = Card(5, 5, "hearts", "image")
        checked = [0 for x in range(len(cards))]
        self.assertEqual(self.calc.check_if_pick_is_allowed(
            cards, card, checked, 0, 0, book), False)

    def test_check_if_pick_is_allowed_no_one_same_card(self):
        book = {}
        cards = [
            Card(9, 9, "spades", "image"),
            Card(3, 3, "hearts", "image"),
            Card(4, 4, "diamonds", "image"),
        ]
        card = Card(9, 9, "hearts", "image")
        checked = [0 for x in range(len(cards))]
        self.assertEqual(self.calc.check_if_pick_is_allowed(
            cards, card, checked, 0, 0, book), False)
