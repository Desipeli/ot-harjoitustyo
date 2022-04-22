

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

    def check_pick():
        pass
    
    #def check_if_pick_is_allowed(self, table, card, checked, index):
    #    result = False
    #    print(index, checked, table)
    #    sub_pick = self.check_if_sub_pick_is_allowed(table, card, checked) # Check current combination
    #    if sub_pick == 0: # Pick was allowed
    #        print("Sai pikata")
    #        for i in range(len(checked)-1, -1, -1):
    #            if checked[i] == 1:
    #                print("POP", table, i)
    #                table.pop(i)
    #        checked = [0 for x in range(len(table))]
    #        index = 0
    #    elif sub_pick == -1: # Not allowed
    #        return False
    #    else: # Sub pick allowed
    #        if len(checked) == 0: # No more cards left to check
    #            print("LÖYTYI!")
    #            return True
    #        else:
    ##               checked[index] = i
     #               if index < len(checked) - 1:
    #                    result = self.check_if_pick_is_allowed(table, card, checked, index + 1)
    #    return result

    
    #def check_if_sub_pick_is_allowed(self, sub_pick, card, checked):
    #    sp_value = 0
    #    for i in range(len(checked)):
    #        if checked[i] == 1:
    #            sp_value += sub_pick[i].v_table
    #    #print("value subpick", sp_value, " value card", card.v_hand)
    #    if sp_value == card.v_hand:
    #        return (0, sp_value)
    #    if sp_value > card.v_hand:
    ##        return (-1, sp_value)
    #    if sp_value < card.v_hand:
    #        return (1, sp_value)

    def sub_pick_sum(self, sub_pick, checked):
        sp_value = 0
        for i in range(len(checked)):
            if checked[i] == 1:
                sp_value += sub_pick[i].v_table
        return sp_value

    def find_all_table_combinations(self, table, p_col):
        checked = [1 for x in range(len(table))]
        combinations_and_value = {}
        self.table_combinations(0, checked, table, combinations_and_value, p_col)
        print(combinations_and_value)
        return combinations_and_value

    def table_combinations(self, index, checked, table, combinations_and_value, p_col):
        if index == len(checked):
            value = 0
            cards_key = []
            for c in range(len(checked)):
                if checked[c] == 1:
                    value += self.card_value(table[c], p_col)
                    cards_key.append(c)   
            cards_key = tuple(cards_key)
            combinations_and_value[cards_key] = value
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


if __name__ == "__main__":
    pass
    #calc = Calcs()
    #from card import Card
    #p_card1 = Card(9,9, "diamonds", "image")
    #table1 = [
    #    Card(14, 1, "spades", "image"),
    #    Card(4, 4, "hearts", "image"),
    #    Card(4, 4, "spades", "image"),
    #    Card(5, 5, "hearts", "image")
    #]
    #calc.find_combinations([Card(10,10,"spades","image")], table, [])
    
    #calc.find_all_table_combinations(table1, [])
    #book = {}
    #re = calc.check_if_pick_is_allowed([Card(1, 1, "hearts", "image"), Card(1, 1, "hearts", "image"), Card(7, 7, "hearts", "image"), Card(9, 9, "hearts", "image"), Card(9, 9, "hearts", "image")], p_card1, [0, 1, 0], 0, 0, book)
    #print(book)
    #print(len(book))
    #print(re)