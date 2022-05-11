from time import time
from cpl import Cpl
from calc import Calcs
from database_actions import update_wins


class Match:
    """ This class handles a single match """

    def __init__(self, info):
        """ Constructor

            Args:
                info: game information
        """
        self.info = info
        self.cpl = Cpl()
        self.calc = Calcs()
        self.player_hand = []
        self.computer_hand = []
        self.player_collected_cards = []
        self.computer_collected_cards = []
        self.deck = None
        self.table = []
        self.turn = True  # t = player, f = computer
        self.round = 0
        self.round_ongoing = True
        self.match_finished = False
        self.winner = None
        self.points_player = 0
        self.points_computer = 0
        self.player_chosen_hand_card = None
        self.player_chosen_table_cards = []
        self.info_text_computer = ""
        self.info_text_player = ""
        self.player_picked_last = False
        self.sweep_player = 0
        self.sweep_computer = 0
        self.info.game_log_text.append("Game started")

    def start_round(self):
        """ Start new round """

        self.deck.assemble_deck()
        self.deck.shuffle()
        self.round += 1
        self.round_ongoing = True
        self.info.game_log_text.append(f"Round {self.round}")
        self.deal_cards(True)

    def deal_cards(self, start_of_round):
        """ deal cards to both of the players

            Args:
                start_of_round: True if first deal of the round
        """

        print("Round: ", self.round)
        for i in range(2):
            if self.round % 2 == 1:  # Start by dealing player first
                self.info_text_player = "Your turn"
                self.deal_two_cards_to(self.player_hand)
                self.deal_two_cards_to(self.computer_hand)
                if start_of_round:
                    self.deal_two_cards_to(self.table)
            else:
                self.info_text_player = "computer's turn"
                self.deal_two_cards_to(self.computer_hand)
                self.deal_two_cards_to(self.player_hand)
                if start_of_round:
                    self.deal_two_cards_to(self.table)
        print(self.computer_hand)
        # self.computer_turn()

    def deal_two_cards_to(self, target):
        target.append(self.deck.pick_top())
        target.append(self.deck.pick_top())

    def check_if_player_can_pick_cards(self):
        """ Directs the selected cards to calcs module function

            Returns:
                True: Combination can be picked with selected card
                False: Can not be picked
        """

        if len(self.player_chosen_table_cards) > 0:  # Player has chosen cards from table
            for c in self.player_chosen_table_cards:
                if c.v_table > self.player_chosen_hand_card.v_hand:
                    self.info_text_player = "You can't pick cards of higher value"
                    return False
            # filter most of the cases
            if sum([x.v_table for x in self.player_chosen_table_cards]) % self.player_chosen_hand_card.v_hand == 0:
                checked = [0 for x in range(
                    len(self.player_chosen_table_cards))]
                print("start checking for combinations")
                begin_timer = time()
                result = self.calc.check_if_pick_is_allowed(
                    self.player_chosen_table_cards, self.player_chosen_hand_card, checked, 0, 0, {})
                end_timer = time()
                print("Time spent searching for combinations:",
                      end_timer-begin_timer, "s")
                return result
        return False

    def player_action_button(self):
        """ Controls the only button used to play the game
            Directs to different functions depending on the situation
        """

        if self.winner is not None:
            return
        if self.round_ongoing:
            if self.round % 2 == 0 and len(self.computer_hand) == 4:
                self.change_turn()
                return
            if self.player_chosen_hand_card == None:
                self.info_text_player = "Choose a card from hand"
                return
            if self.check_if_player_can_pick_cards():
                self.move_selected_cards_to_player()
            else:
                if len(self.player_chosen_table_cards) > 0:
                    return
                self.play_card_to_table()
            self.info_text_player = "Computer's turn"
            self.change_turn()
        else:
            self.start_round()

    def move_selected_cards_to_player(self):
        """ Moves selected cards to player and calculate points """

        # hand
        self.player_collected_cards.append(self.player_chosen_hand_card)
        self.add_points_to("player", self.player_chosen_hand_card)
        self.player_hand.remove(self.player_chosen_hand_card)
        # table
        #picked_cards = ""
        for c in self.player_chosen_table_cards:
            self.table.remove(c)
            self.add_points_to("player", c)
            self.player_collected_cards.append(c)
            #picked_cards += f"{c.v_table} of {c.suit}, "
        self.player_chosen_table_cards = []
        self.info_text_player = "Your turn"
        self.player_chosen_hand_card = None
        self.player_picked_last = True

    def play_card_to_table(self):
        """ card is moved from player to the table """

        self.table.append(self.player_chosen_hand_card)
        self.player_hand.remove(self.player_chosen_hand_card)
        self.info_text_player = "Your turn"
        self.player_chosen_hand_card = None

    def change_turn(self):
        """ This function handles turn changes and round/match endings """

        if len(self.player_hand) == 0 and len(self.computer_hand) == 0 and len(self.deck.see_deck()) > 0:
            self.check_if_match_ends()
            self.deal_cards(False)
        elif len(self.player_hand) == 0 and len(self.computer_hand) == 0 and len(self.deck.see_deck()) == 0:
            self.end_cards_to()
            self.info.game_log_text.append(f"Round ended!")
            self.round_end_points()
            self.info_text_player = "Round!"
            self.round_ongoing = False
            self.check_if_match_ends()
            print("Round ends")
        else:
            self.check_for_sweep()
        if self.turn:
            self.computer_turn()
        else:
            self.player_turn()

    def player_turn(self):
        """ Tell player it's his/her turn """

        self.turn = True
        self.info_text_player = "Your turn"

    def computer_turn(self):
        """ Computer's turn next. Direct to cpl for logic """

        self.turn = False
        begin_timer = time()
        result = self.cpl.play(
            self.table, self.computer_hand, self.player_collected_cards)
        end_timer = time()
        print("Duration of computers turn:", end_timer-begin_timer, "s")
        if result:
            if result[0] == "card_to_table":
                self.computer_card_to_table(result[1])
            elif result[0] == "cards_to_computer":
                self.move_selected_cards_to_computer(result[1], result[2])
        self.change_turn()

    def computer_card_to_table(self, card):
        """ Computer plays card to table

            Args:
                card: Card which computer plays to table
        """

        self.table.append(card)
        self.computer_hand.remove(card)
        self.info.game_log_text.append(f"Computer played {card.v_hand} of {card.suit} to the table")
        self.info.game_log_text.append(f"")
        self.info_text_computer = f"Computer played {card.v_hand} of {card.suit} to table"
        print("computer played", card.v_hand, card.suit, " to table")

    def move_selected_cards_to_computer(self, hand_card, table_cards):
        """ move cards chosen by computer to its pile and add points
        
            Args:
                hand_card: hand card to be moved
                table_cards: table cards to be moved
        """

        self.computer_hand.remove(hand_card)
        self.computer_collected_cards.append(hand_card)
        picked_cards = ""
        self.info.game_log_text.append("Computer picked: ")
        for card in table_cards:
            self.table.remove(card)
            self.computer_collected_cards.append(card)
            self.add_points_to("computer", card)
            picked_cards += f"{card.v_table} of {card.suit} ,"
            self.info.game_log_text.append(f"   {card.v_table} of {card.suit}")
        self.info_text_computer = f"Computer picked [{picked_cards}] with {hand_card.v_hand} of {hand_card.suit}"
        self.info.game_log_text.append(f"With {hand_card.v_hand} of {hand_card.suit}")
        self.info.game_log_text.append(f"")
        self.add_points_to("computer", hand_card)
        self.player_picked_last = False

    def print_hands(self):
        """ Print hand cards to terminal """

        print("player col:", [(c.v_hand, c.suit)
              for c in self.player_collected_cards])
        print("computer col:", [(c.v_hand, c.suit)
              for c in self.computer_collected_cards])

    def add_points_to(self, who, card):
        """ Add points to player or computer

            Args:
                who: string containing "player" or "computer"
                card: card object to be valued
        """

        points = 0
        if card.v_hand == 14 or card.v_hand == 15:
            points += 1
        elif card.v_hand == 16:
            points += 2
        if who == "player":
            self.points_player += points
        else:
            self.points_computer += points

    def end_cards_to(self):
        """ Decides who gets the remaining table cards when hands are empty """

        if len(self.table) == 0:
            return
        picked_cards = ""
        for c in self.table:
            picked_cards += f" {c.v_table} of {c.suit}, "
            if self.player_picked_last:
                self.player_collected_cards.append(c)
                self.add_points_to("player", c)
            else:
                self.computer_collected_cards.append(c)
                self.add_points_to("computer", c)
        if self.player_picked_last:
            self.info_text_computer = f"Player got remaining cards: {picked_cards}"
            self.info.game_log_text.append(f"Player got the remaining cards")
        else:
            self.info_text_computer = f"Computer got remaining cards: {picked_cards}"
            self.info.game_log_text.append(f"Computer got the remaining cards")
        self.info.game_log_text.append(f"")
        self.table.clear()

    def round_end_points(self):
        """ Calculate and gives points from cards, spades and sweeps """

        if len(self.player_collected_cards) > len(self.computer_collected_cards):
            self.info.game_log_text.append(f"Player collected more cards: +1 point")
            self.points_player += 1
        elif len(self.player_collected_cards) < len(self.computer_collected_cards):
            self.info.game_log_text.append(f"Computer got 1 point from collecting more cards")
            self.points_computer += 1
        player_spades = 0
        for c in self.player_collected_cards:
            if c.suit == "spades":
                player_spades += 1
        if player_spades > 6:
            self.info.game_log_text.append(f"Player collected more spades: +2 point")
            self.points_player += 2
        else:
            self.points_computer += 2
            self.info.game_log_text.append(f"Computer got 2 points from collecting more spades")
        self.points_computer += self.sweep_computer
        self.points_player += self.sweep_player
        if self.sweep_computer > 0:
            self.info.game_log_text.append(f"Computer got {self.sweep_computer} points from sweeps")
        elif self.sweep_player > 0:
            self.info.game_log_text.append(f"Player got {self.sweep_player} points from sweeps")
        self.sweep_computer = 0
        self.sweep_player = 0
        self.player_collected_cards.clear()
        self.computer_collected_cards.clear()

    def check_for_sweep(self):
        """ Check if sweep is made after pick """

        if max(self.points_computer, self.points_player) < 10 and len(self.table) == 0 and len(self.deck.see_deck()) > 0:
            print("sweep")
            if self.player_picked_last:
                if self.sweep_computer == 0:
                    self.sweep_player += 1
                else:
                    self.sweep_computer -= 1
            else:
                if self.sweep_player == 0:
                    self.sweep_computer += 1
                else:
                    self.sweep_player -= 1

    def check_if_match_ends(self):
        """ Checks if player or computer has at least 16 points for win """
        if self.winner:
            return
        player_total = self.points_player + self.sweep_player
        computer_total = self.points_computer + self.sweep_computer
        if max(player_total, computer_total) >= 16 and player_total != computer_total:  # Match ends
            saved_to_db = update_wins(player_total, computer_total)
            if player_total > computer_total:
                print("Player wins with", player_total, "points")
                self.info.game_log_text.append(f"Player wins with {player_total}")
                self.winner = "player"
            else:
                print("Computer wins with", computer_total, "points")
                self.info.game_log_text.append(f"Computer wins with {computer_total}")
                self.winner = "computer"
            if not saved_to_db:
                self.info.game_log_text.append("Could not save points to database")
                self.info.game_log_text.append("Did you run poetry run invoke build?")

    def back_to_main_menu(self):
        self.info.game_stage = 0
