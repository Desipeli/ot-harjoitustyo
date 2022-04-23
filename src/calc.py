

class Calcs:

    def __init__(self) -> None:
        pass

    def card_value(self, card, p_col=None):
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

    def cardset_value(self, cardset, p_col):
        value = 0
        for c in cardset:
            value += self.card_value(c, p_col)
        return value

    def sub_pick_sum(self, sub_pick, checked):
        sp_value = 0
        for i in range(len(checked)):
            if checked[i] == 1:
                sp_value += sub_pick[i].v_table
        return sp_value

    def find_all_table_combinations(self, table, p_col):
        checked = [1 for x in range(len(table))]
        combinations_and_value = []
        self.table_combinations(0, checked, table, combinations_and_value, p_col)
        #print(combinations_and_value)
        return combinations_and_value

    def table_combinations(self, index, checked, table, combinations_and_value, p_col):
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
                self.table_combinations(index +1, checked, table, combinations_and_value, p_col)

    def check_if_pick_is_allowed(self, table, card, checked, index, current_sum, book):
        if index == len(checked):
            sub_pick = self.sub_pick_sum(table, checked)
            current_sum += sub_pick
            if current_sum > card.v_hand:
                #print(current_sum, "Liian iso summa")
                return False
            else: # Pick allowed or not enough
                new_table = table.copy()
                for i in range(len(checked) -1, -1, -1):
                    if checked[i] == 1:
                        new_table.pop(i)
                new_checked = [0 for x in range(len(new_table))]
                if current_sum == card.v_hand:
                    if len(new_table) == 0:
                        #print("löytyi!!!")
                        return True
                    else:
                        if len(new_table) == 0:
                            #print("Ei riitä kortit enää")
                            return False
                if sub_pick == card.v_hand:
                        if tuple(new_table) in book:
                            return book[tuple(new_table)]
                        book[tuple(new_table)] = None
                        result = self.check_if_pick_is_allowed(new_table, card, new_checked, 0, 0, book) # Start searching for remaining combination(s)
                        book[tuple(new_table)] = result
                        return result
                if current_sum < card.v_hand:
                    if tuple(new_table) in book:
                        return book[tuple(new_table)]
                    book[tuple(new_table)] = None
                    result = self.check_if_pick_is_allowed(new_table, card, new_checked, 0, current_sum, book) # Start searching for remaining combination(s)
                    book[tuple(new_table)] = result
                    return result
                return False
        else:
            #print(index, checked, table, book)
            result = False
            for i in range(2):
                checked[index] = i
                if tuple(table) not in book:
                    book[tuple(table)] = None
                result = self.check_if_pick_is_allowed(table, card, checked, index + 1, current_sum, book)
                book[tuple(table)] = result
                if result:
                    break
        if result is None:
            result = False
        return result

    def check_best_combination_for_computer(self, combinations, computer_cards, table):
        print()
        combinations = sorted(combinations) # Best combination is last (value, [indexes])
        computer_cards = sorted(computer_cards, key=lambda x: self.card_value(x), reverse=True) # Computer hand cards in order (best first)
        choice = [] # best choice here
        choice_hand = None # hand card used for best choice
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
                result = self.check_if_pick_is_allowed(sub_table, c, checked, 0, 0, {})
                if result:
                    found_one = True
                    choice = sub_table.copy()
                    choice_hand = c
                    break
        print("best choice: ")
        if found_one:
            print("hand card: ", choice_hand.v_hand, choice_hand.suit, "table cards: ")
            for c in choice:
                print(c.v_table, c.suit, end=" ")
            print()
            return choice_hand, choice
        else:
            print("no possible combinations")
        return False
