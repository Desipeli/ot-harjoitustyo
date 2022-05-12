from logic.calc import Calcs


class Cpl:
    """ This class has the computer player logic """

    def __init__(self):
        """ Constructor """

        self.calcs = Calcs()

    def play(self, table, computer_hand, player_collected):
        """ Computer's turn starts

            Args:
                table: table cards
                computer_hand: computer's hand cards
                player_collected: Cards collected by the player. Needed to calculate weights for table cards

            Returns:
                False: Computer has no hand cards
                If can not pick any cards: ("card_to_table", card to played to the table)
                If can pick cards: ("cards_to_computer", hand card used to pick, combination of cards to pick)
        """

        if len(computer_hand) < 1:
            return False
        if len(table) < 1:
            return self.choose_which_card_to_table(computer_hand, player_collected)
        else:
            return self.decide_what_cards_to_pick(table, computer_hand, player_collected)

    def choose_which_card_to_table(self, computer_hand, player_collected):
        """ Checks which hand card has lowest weight

            Args:
                computer_hand: computer's hand cards
                player_collected: cards collected by the player

            Returns:
                tuple: ("card_to_table", card with lowest weight)
        """
        weakest_card = computer_hand[0]
        for card in computer_hand:
            if self.calcs.card_value(card, player_collected) < self.calcs.card_value(weakest_card, player_collected):
                weakest_card = card
        return ("card_to_table", weakest_card)

    def decide_what_cards_to_pick(self, table, computer_hand, player_collected):
        """ Checks which combination should be picked and with which card. If no possible
         combinations, check which card should be played to the table

            Args:
                table: List of table cards
                computer_hand: Computer's hand cards
                player_collected: Cards collected by the player

            Returns:
                if can be picked: ("cards_to_computer", computer's hand card used to pick,
                    list of cards to pick)
                else: ("card_to_table", card with lowest weight)
        """

        all_combinations = self.calcs.find_all_table_combinations(
            table.copy(), player_collected)
        result = self.calcs.check_best_combination_for_computer(
            all_combinations, computer_hand, table)
        if result:
            hand_card = result[0]
            table_cards = result[1]
            return ("cards_to_computer", hand_card, table_cards)
        else:  # No possible combinations, play card to table
            return self.choose_which_card_to_table(computer_hand, player_collected)
