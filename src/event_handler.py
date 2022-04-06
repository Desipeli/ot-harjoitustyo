import pygame
import sys
from match import Match
from deck import Deck

class Events:

    def check_event(self, event, info):
        self.info = info
        self.event = event
        if self.event.type == pygame.MOUSEBUTTONDOWN:
            self.check_clicks()
        if self.event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    
    def check_clicks(self):
        # Menu
        if self.info.game_stage == 0 and self.event.button == 1:
            for b in self.info.menu_buttons:
                if self.check_button(b):
                    if b.text == "Play":
                        self.start_match()        
        # Game tabel
        elif self.info.game_stage == 1:
            if self.event.button == 1:
                self.check_click_deck()
                self.check_click_player_hand()
                self.check_click_table()



    def check_click_table(self):
        match = self.info.match
        for card in match.table:
            if self.check_click_surface(card):
                print("pöytä", [x.v_table for x in match.table])
                print("Pöytä valittu",card.v_table, [x.v_table for x in match.player_chosen_table_cards])
                if card not in match.player_chosen_table_cards:
                    match.player_chosen_table_cards.append(card)
                else:
                    match.player_chosen_table_cards.remove(card)

    def check_click_player_hand(self):
        match = self.info.match
        for card in match.player_hand:
            if self.check_click_surface(card): # Player chose a card in hand
                print(card.v_hand)
                match.player_chosen_hand_card = card
            
    
    def check_click_surface(self, s): # This can be used to check if player clicked a card
            p = self.event.pos
            if p[0] >= s.pos[0] and p[0] <= s.pos[0] + s.image.get_width():
                if p[1] >= s.pos[1] and p[1] <= s.pos[1] + s.image.get_height():
                    return True
            return False

    def check_button(self, button):
        if self.event.pos[0] >= button.center[0] and self.event.pos[0] <= button.center[0]+button.size[0]:
            if self.event.pos[1] >= button.center[1] and self.event.pos[1] <= button.center[1]+button.size[1]:
                return True
        return False

    # This is for test purpose only
    def check_click_deck(self):
        if self.event.pos[0] >= self.info.deck_pos[0] and self.event.pos[0] <= self.info.deck_pos[0] + self.info.match.deck.get_back().image.get_width():
            if self.event.pos[1] >= self.info.deck_pos[1] and self.event.pos[1] <= self.info.deck_pos[1] + self.info.match.deck.get_back().image.get_height():
                deck = self.info.match.deck
                card = deck.pick_top()
                if card:
                    print(card.v_hand, card.suit)
                    self.info.match.player_hand.append(card)
                card = deck.pick_top()
                if card:
                    self.info.match.computer_hand.append(card)
                card = deck.pick_top()
                if card:
                    self.info.match.table.append(card)

    def start_match(self):
        print("Match started!")
        match = Match(self.info)
        match.deck = Deck(self.info.cards.copy(), self.info.backs[0])
        self.info.match = match
        self.info.game_stage = 1
        match.start_round()
        
        