

class Calcs:

    def __init__(self) -> None:
        pass

    def card_value(self, card, p_col):
        value = 0
        if card.v_hand == 14 or card.v_hand == 15:
            value += 1
        elif card.v_hand == 16:
            value += 2
        if card.suit == "spades":
            # check if player has < half of spades
            if len([x for x in p_col if x.suit == "spades"]) < 7:
                print("player spades:", len(
                    [x for x in p_col if x.suit == "spades"]))
                value += 0.2
        return value