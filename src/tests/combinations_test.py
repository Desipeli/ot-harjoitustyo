import unittest
from calc import Calcs
from card import Card

class TestCalc(unittest.TestCase):
    def setUp(self):
        self.calc = Calcs()
        self.cards = [
            Card(14, 1, "spades", "image"),
            Card(14, 1, "hearts", "image"),
            Card(16, 10, "diamonds", "image"),
            Card(13, 13, "spades", "image"),
        ]
    
    def test_table_combinations_count(self):
        result = self.calc.find_all_table_combinations(self.cards)
        self.assertEqual(len(result), 16)
