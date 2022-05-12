import sys
import pygame
from logic.match import Match
from logic.deck import Deck


class Events:
    """ This class handles pygame events. """

    def check_event(self, event, info):
        """ Check what kind of event occurred.

            Args:
                event: pygame event
        """

        self.info = info
        self.event = event
        if self.event.type == pygame.MOUSEBUTTONDOWN:
            self.check_clicks()
        if self.event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    def check_clicks(self):
        """ Check mouse click events for left mouse button. """

        # Menu
        if self.info.game_stage == 0 and self.event.button == 1:
            self.check_click_menu_buttons()
        # statistics
        elif self.info.game_stage == 3 and self.event.button == 1:
            self.check_click_stats()
        # Game tabel
        elif self.info.game_stage == 1:
            if self.event.button == 1 and self.info.match.turn:
                if self.info.match.round % 2 == 0 and len(self.info.match.computer_hand) == 4:
                    self.check_click_game_buttons()
                    self.check_click_match_end()
                else:
                    self.check_click_game_buttons()
                    self.check_click_player_hand()
                    self.check_click_table()
                    self.check_click_match_end()
        elif self.info.game_stage == 4:
            self.check_click_settings_buttons()

    def check_click_settings_buttons(self):
        for b in self.info.settings_buttons:
            if self.check_button(b):
                if b.id == 9:
                    self.info.game_stage = 0
                elif b.id == 8:
                    self.info.settings.open_cards_change()

    def check_click_menu_buttons(self):
        for b in self.info.menu_buttons:
            if self.check_button(b):
                if b.id == 0:
                    self.start_match()
                elif b.id == 2:
                    pygame.quit()
                    sys.exit()
                elif b.id == 1:
                    self.info.game_stage = 3
                elif b.id == 6:
                    self.info.game_stage = 1
                elif b.id == 7:
                    self.info.game_stage = 4

    def check_click_game_buttons(self):
        """ Check if any match buttons are clicked. """

        for b in self.info.game_buttons:
            if self.check_button(b):
                if b.id == 3:
                    self.info.match.player_action_button()
                if b.id == 5:
                    self.info.game_stage = 0
                    # Match object remains, so match can be continued

    def check_click_stats(self):
        """ Check if any buttons in stats view are clicked """

        for b in self.info.stats_buttons:
            if self.check_button(b):
                if b.id == 9:
                    self.info.game_stage = 0

    def check_click_table(self):
        """ Check if table card is clicked. """

        match = self.info.match
        if not match.turn:
            return
        for card in match.table:
            if self.check_click_surface(card):
                if card not in match.player_chosen_table_cards:
                    match.player_chosen_table_cards.append(card)
                else:
                    match.player_chosen_table_cards.remove(card)
                print("pöytä", [x.v_table for x in match.table])
                print("Pöytä valittu", card.v_table, [
                    x.v_table for x in match.player_chosen_table_cards])

    def check_click_player_hand(self):
        """ Check if player hand card is clicked. """

        match = self.info.match
        if not match.turn:
            return
        for card in match.player_hand:
            if self.check_click_surface(card):
                print(card.v_hand)
                match.player_chosen_hand_card = card

    def check_click_surface(self, s):
        """ Check if surface (for example image of a card) is clicked.

            Args:
                s: surface
        """

        p = self.event.pos
        if p[0] >= s.pos[0] and p[0] <= s.pos[0] + s.image.get_width():
            if p[1] >= s.pos[1] and p[1] <= s.pos[1] + s.image.get_height():
                return True
        return False

    def check_button(self, button):
        """ Check if button is clicked.

            Args:
                button: Button
        """

        if self.event.pos[0] >= button.center[0] and self.event.pos[0] <= button.center[0]+button.size[0]:
            if self.event.pos[1] >= button.center[1] and self.event.pos[1] <= button.center[1]+button.size[1]:
                return True
        return False

    def start_match(self):
        """ A new match object is created and first round started. """

        print("Match started!")
        match = Match(self.info)
        match.deck = Deck(self.info.cards.copy(), self.info.backs[0])
        self.info.match = match
        self.info.game_stage = 1
        match.start_round()

    def check_click_match_end(self):
        """ Checks if back to main menu button is pressed when game is over. """

        for b in self.info.match_end_buttons:
            if self.check_button(b):
                if b.id == 4 and self.info.match.winner:
                    self.info.match.back_to_main_menu()
