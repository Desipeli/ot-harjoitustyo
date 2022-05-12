from re import M
import unittest
from logic.match import Match
from logic.deck import Deck
from card import Card
from info import Info


class TestDeck(unittest.TestCase):
    def setUp(self):
        self.info = Info()
        self.match = Match(self.info)
        self.match.deck = Deck([
            Card(14, 1, "spades", "image"),
            Card(4, 4, "spades", "image"),
            Card(8, 8, "spades", "image"),
            Card(14, 1, "diamonds", "image"),
            Card(9, 9, "diamonds", "image"),
            Card(13, 13, "clubs", "image"),
            Card(11, 11, "hearts", "image"),
            Card(6, 6, "hearts", "image"),
            Card(7, 7, "diamonds", "image"),
            Card(12, 12, "clubs", "image"),
            Card(5, 5, "hearts", "image"),
            Card(2, 2, "hearts", "image")
        ], "back")

    def test_start_round(self):
        self.assertEqual(self.match.round, 0)
        self.match.start_round()
        self.assertEqual(self.match.round, 1)
        self.assertEqual(self.match.round_ongoing, True)

    def test_deal_cards_true(self):
        m = self.match
        m.deal_cards(True)
        self.assertEqual(len(m.player_hand), 4)
        self.assertEqual(len(m.computer_hand), 4)
        self.assertEqual(len(m.table), 4)

    def test_deal_cards_false(self):
        m = self.match
        m.deal_cards(False)
        self.assertEqual(len(m.player_hand), 4)
        self.assertEqual(len(m.computer_hand), 4)
        self.assertEqual(len(m.table), 0)

    def test_deal_two_cards_to(self):
        m = self.match
        m.deal_two_cards_to(m.player_hand)
        self.assertEqual(len(m.player_hand), 2)
        m.deal_two_cards_to(m.computer_hand)
        m.deal_two_cards_to(m.computer_hand)
        self.assertEqual(len(m.computer_hand), 4)

    def test_check_if_player_can_pick_no_chosen(self):
        m = self.match
        self.assertEqual(m.check_if_player_can_pick_cards(), False)

    def test_check_if_player_can_pick_too_smol(self):
        m = self.match
        m.start_round()
        m.player_chosen_table_cards.append(m.table[0])
        m.player_chosen_hand_card = m.player_hand[1]
        self.assertEqual(m.check_if_player_can_pick_cards(), False)

    def test_chek_if_player_can_pick_too_big(self):
        m = self.match
        m.start_round()
        m.player_chosen_table_cards.append(m.table[0])
        m.player_chosen_hand_card = m.player_hand[0]
        self.assertEqual(m.check_if_player_can_pick_cards(), False)

    def test_check_if_player_can_pick_allowed(self):
        m = self.match
        m.table.append(Card(4, 4, "diamonds", "image"))
        m.player_hand.append(Card(4, 4, "clubs", "image"))
        m.player_chosen_table_cards.append(m.table[0])
        m.player_chosen_hand_card = m.player_hand[0]
        self.assertEqual(m.check_if_player_can_pick_cards(), True)

    def test_move_selected_cards_to_player(self):
        m = self.match
        m.player_hand.append(Card(10, 10, "clubs", "image"))
        m.player_chosen_hand_card = m.player_hand[0]
        m.table.append(Card(16, 10, "diamonds", "image"))
        m.player_chosen_table_cards.append(m.table[0])
        m.move_selected_cards_to_player()
        self.assertEqual(len(m.player_hand), 0)
        self.assertEqual(len(m.player_collected_cards), 2)
        self.assertEqual(len(m.table), 0)
        self.assertEqual(m.points_player, 2)
        self.assertEqual(m.player_chosen_hand_card, None)
        self.assertEqual(m.player_picked_last, True)

    def test_play_card_to_table(self):
        m = self.match
        m.player_hand.append(Card(16, 10, "diamonds", "image"))
        m.player_chosen_hand_card = m.player_hand[0]
        m.play_card_to_table()
        self.assertEqual(len(m.table), 1)
        self.assertEqual(m.player_chosen_hand_card, None)

    def test_change_turn_to_player_and_deal(self):
        m = self.match
        m.turn = False
        m.change_turn()
        self.assertEqual(m.turn, True)
        self.assertEqual(len(m.player_hand), 4)
        self.assertEqual(len(m.table), 0)
        self.assertEqual(len(m.computer_hand), 4)

    def test_change_turn_to_computer_and_deal(self):
        m = self.match
        m.turn = True
        m.change_turn()
        self.assertEqual(len(m.player_hand), 4)
        self.assertEqual(len(m.table), 1)
        self.assertEqual(len(m.computer_hand), 3)

    def test_change_turn_round_end(self):
        m = self.match
        m.deck = Deck([], "back")
        m.change_turn()
        self.assertEqual(m.round_ongoing, False)

    def test_move_selected_cards_to_computer(self):
        m = self.match
        m.computer_hand.append(Card(10, 10, "clubs", "image"))
        m.table.append(Card(16, 10, "diamonds", "image"))
        m.move_selected_cards_to_computer(m.computer_hand[0], m.table.copy())
        self.assertEqual(len(m.computer_hand), 0)
        self.assertEqual(len(m.computer_collected_cards), 2)
        self.assertEqual(len(m.table), 0)
        self.assertEqual(m.points_computer, 2)
        self.assertEqual(m.player_picked_last, False)

    def test_add_points_to_player_0(self):
        m = self.match
        c = Card(10, 10, "hearts", "image")
        m.add_points_to("player", c)
        self.assertEqual(m.points_player, 0)

    def test_add_points_to_player_ace(self):
        m = self.match
        c = Card(14, 14, "hearts", "image")
        m.add_points_to("player", c)
        self.assertEqual(m.points_player, 1)

    def test_add_points_to_player_2spades(self):
        m = self.match
        c = Card(15, 2, "spades", "image")
        m.add_points_to("player", c)
        self.assertEqual(m.points_player, 1)

    def test_add_points_to_player_10diamonds(self):
        m = self.match
        c = Card(16, 10, "diamonds", "image")
        m.add_points_to("player", c)
        self.assertEqual(m.points_player, 2)

    def test_round_end_points_more_cards_player(self):
        m = self.match
        for i in range(40):
            m.player_collected_cards.append(
                Card(1, 2, "hearts", "image")
            )
        m.round_end_points()
        self.assertEqual(m.points_player, 1)
