


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

    def find_all_table_combinations(self, table):
        checked = [1 for x in range(len(table))]
        combinations_and_value = {}
        self.table_combinations(0, checked, table, combinations_and_value)
        print(combinations_and_value)
        return combinations_and_value

    def table_combinations(self, index, checked, table, combinations_and_value):
        if index == len(checked):
            value = 0
            cards_key = []
            for c in range(len(checked)):
                if checked[c] == 1:
                    value += self.card_value(table[c])
                    cards_key.append(c)   
            cards_key = tuple(cards_key)
            combinations_and_value[cards_key] = value
        else:
            for i in range(2):
                checked[index] = i
                self.table_combinations(index +1, checked, table, combinations_and_value)

if __name__ == "__main__":
    calc = Calcs()
    from card import Card
    p_card1 = Card(9,9, "diamonds", "image")
    table1 = [
        Card(14, 1, "spades", "image"),
        Card(4, 4, "hearts", "image"),
        Card(4, 4, "spades", "image"),
        Card(8, 8, "hearts", "image")
    ]
    #calc.find_combinations([Card(10,10,"spades","image")], table, [])
    calc.find_all_table_combinations(table1)