

class Calcs:
    """ Class that has different functions to check value of cards and if they can be picked """

    def __init__(self) -> None:
        pass

    def card_value(self, card, p_col=None):
        """ Check value(weight) of a card to help computer to choose which cards to pick

        Args:
            card: Card that is checked
            p_col: List of cards that player has collected

        Returns:
            Value(weight) of card
        """

        if p_col is None:
            p_col = []
        value = 0.1
        if card.v_hand == 14 or card.v_hand == 15:
            value += 1
        elif card.v_hand == 16:
            value += 2
        if card.suit == "spades":
            # check if player has < half of spades
            if len([x for x in p_col if x.suit == "spades"]) < 7:
                value += 0.2
        return value

    def sub_pick_sum(self, sub_pick, checked):
        """ Calculates table value of cards

            Args:
                sub_pick: A set of table cards
                checked: List of indexes of the set of table cards. 1 = selected

            Returns:
                Integer, that is sum of table values of cards
        """

        sp_value = 0
        for i in range(len(checked)):
            if checked[i] == 1:
                sp_value += sub_pick[i].v_table
        return sp_value

    def find_all_table_combinations(self, table, p_col):
        """ Start of checking combinations for cards on the table

            Args:
                table: List of cards on the table
                p_col: Cards that player has collected

            Returns:
                A list of tuples (value(weight), combination as indexes of table cards)
        """

        checked = [1 for x in range(len(table))]
        combinations_and_value = []
        self.table_combinations(
            0, checked, table, combinations_and_value, p_col)
        # print(combinations_and_value)
        return combinations_and_value

    def table_combinations(self, index, checked, table, combinations_and_value, p_col):
        """ Find different combinations from table combinations and add value to them for computer player

            Args: 
                index: which card is handled
                checked: List of table card indexes. 1 = card is included 0 = not included
                table: List of table cards
                combinations_and_values: List where combinations and their values(weight) are saved
                    (value, list of table card indexes)
                p_col: Cards collected by the player
        """

        if index == len(checked):
            value = 0
            table_indexes = []
            for c in range(len(checked)):
                if checked[c] == 1:
                    value += self.card_value(table[c], p_col)
                    table_indexes.append(c)
            table_indexes = tuple(table_indexes)
            combinations_and_value.append((value, table_indexes))
        else:
            for i in range(2):
                checked[index] = i
                self.table_combinations(
                    index + 1, checked, table, combinations_and_value, p_col)

    def check_if_pick_is_allowed(self, table, card, checked, index, current_sum, book):
        """ Checks if selected combination can be picked with selected card

            Args:
                table: List of table cards
                card: Card that is used to pick the combination
                checked: List of indexes of table cards. 1 = selected, 0 = not selected
                index: Current index of table cards
                current_sum: current sum of table values of table cards
                book: Used to check if combination is already checked

            Returns:
                True, if combination can be picked with selected card
                False if combination can not be picked with selected card
        """
        if index == len(checked):
            sub_pick = self.sub_pick_sum(table, checked)
            current_sum += sub_pick
            if current_sum > card.v_hand:
                return False
            else:  # Pick allowed or not enough
                new_table = table.copy()
                for i in range(len(checked) - 1, -1, -1):
                    if checked[i] == 1:
                        new_table.pop(i)
                new_checked = [0 for x in range(len(new_table))]
                if current_sum == card.v_hand:
                    if len(new_table) == 0:
                        return True
                    else:
                        if len(new_table) == 0:
                            return False
                if sub_pick == card.v_hand:
                    if tuple(new_table) in book:
                        return book[tuple(new_table)]
                    book[tuple(new_table)] = None
                    # Start searching for remaining combination(s)
                    result = self.check_if_pick_is_allowed(
                        new_table, card, new_checked, 0, 0, book)
                    book[tuple(new_table)] = result
                    return result
                if current_sum < card.v_hand:
                    if tuple(new_table) in book:
                        return book[tuple(new_table)]
                    book[tuple(new_table)] = None
                    # Start searching for remaining combination(s)
                    result = self.check_if_pick_is_allowed(
                        new_table, card, new_checked, 0, current_sum, book)
                    book[tuple(new_table)] = result
                    return result
                return False
        else:
            result = False
            for i in range(2):
                checked[index] = i
                if tuple(table) not in book:
                    book[tuple(table)] = None
                result = self.check_if_pick_is_allowed(
                    table, card, checked, index + 1, current_sum, book)
                book[tuple(table)] = result
                if result:
                    break
        if result is None:
            result = False
        return result

    def check_best_combination_for_computer(self, combinations, computer_cards, table):
        """ Find best combination of table cards for computer player to pick

            Args:
                combinations: combinations and their weight (weight, [combination])
                computer_cards: List of cards in computer player's hand
                table: List of table cards

            Returns:
                Tuple (list of chosen card, card that is used to pick them)
                False: Could not find any combination
        """

        print()
        # Best combination is last (value, [indexes])
        combinations = sorted(combinations)
        computer_cards = sorted(computer_cards, key=lambda x: self.card_value(
            x), reverse=True)  # Computer hand cards in order (best first)
        choice = []  # best choice here
        choice_hand = None  # hand card used for best choice
        found_one = False
        for comb in range(len(combinations)):
            if found_one:
                break
            best = combinations.pop()
            sub_table = []
            for i in best[1]:
                sub_table.append(table[i])
            checked = [0 for x in range(len(sub_table))]
            for c in computer_cards:
                result = self.check_if_pick_is_allowed(
                    sub_table, c, checked, 0, 0, {})
                if result:
                    found_one = True
                    choice = sub_table.copy()
                    choice_hand = c
                    break
        print("best choice: ")
        if found_one:
            print("hand card: ", choice_hand.v_hand,
                  choice_hand.suit, "table cards: ")
            for c in choice:
                print(c.v_table, c.suit, end=" ")
            print()
            return choice_hand, choice
        else:
            print("no possible combinations")
        return False
