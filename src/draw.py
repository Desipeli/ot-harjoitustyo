
import pygame

from deck import Deck

class Draw:
    def __init__(self, info):
        self.info = info

    def draw(self):
        # draw menu buttons
        if self.info.game_stage == 0:
            for b in self.info.menu_buttons:
                b.draw()
        

        # draw deck only if cards left
        if self.info.game_stage == 1:
            self.draw_game_buttons()
            self.draw_points()
            if len(self.info.match.deck.see_deck()) > 0:
                self.draw_deck()
            if len(self.info.match.player_hand) > 0:
                self.draw_hand(self.info.match.player_hand)
            if len(self.info.match.computer_hand) > 0:
                self.draw_hand(self.info.match.computer_hand)
            if len(self.info.match.table) > 0:
                self.draw_table()
    
    def draw_points(self):
        font = self.info.font
        p = self.info.match.points_player
        c = self.info.match.points_computer
        tp = font.render(f"player: {p}", True, (200,200,200))
        tc = font.render(f"computer: {c}", True, (200,200,200))
        self.info.screen.blit(tp, (1100, 100))
        self.info.screen.blit(tc, (1100, 200))

    def draw_table(self):
        i = 0
        for c in self.info.match.table:
            card_width = self.info.match.deck.get_back().image.get_width()
            x = (self.info.screen.get_width()-len(self.info.match.table)*card_width)/2 + i*card_width
            y = self.info.screen.get_height()/2 - self.info.match.deck.get_back().image.get_height()/2
            if c in self.info.match.player_chosen_table_cards:
                y -= c.image.get_height()/3
            self.draw_card(c, (x,y))
            c.pos = (x,y)
            i += 1

    def draw_hand(self, hand):
        i = 0
        for c in hand:
            card_width = self.info.match.deck.get_back().image.get_width()          
            if hand == self.info.match.player_hand:
                x = (self.info.screen.get_width()-len(self.info.match.player_hand)*card_width)/2 + i*card_width
                y = self.info.screen.get_height()-self.info.match.deck.get_back().image.get_height()
                if c == self.info.match.player_chosen_hand_card:    # Change y for chosen card
                    y -= c.image.get_height()/3
            else:
                x = (self.info.screen.get_width()-len(self.info.match.computer_hand)*card_width)/2 + i*card_width
                y = 0
            pos = (x, y)
            self.draw_card(c, pos)
            c.pos = pos
            i += 1       

    def draw_card(self, card, pos):
        self.info.screen.blit(card.image, pos)

    def draw_deck(self):
        self.info.screen.blit(self.info.match.deck.get_back().image, self.info.deck_pos)
    
    def draw_game_buttons(self):
        m = self.info.match
        for button in self.info.game_buttons:
            if button.id == 3:
                cw = self.info.match.deck.get_back().image.get_width()
                button.pos = (self.info.screen.get_width()/2 - (len(self.info.match.player_hand) * cw / 2) - cw, button.pos[1])
                if m.check_if_player_can_pick_cards():
                    button.text = "pick cards"
                else:
                    button.text = "play to table"
            button.draw()

