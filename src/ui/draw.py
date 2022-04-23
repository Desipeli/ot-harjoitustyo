from ui.match_ended import MatchEnded


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
            self.draw_sweeps()
            self.draw_info_text_computer()
            self.draw_info_text_player()

            if len(self.info.match.deck.see_deck()) > 0:
                self.draw_deck()
            if len(self.info.match.player_hand) > 0:
                self.draw_hand(self.info.match.player_hand)
            if len(self.info.match.computer_hand) > 0:
                self.draw_hand(self.info.match.computer_hand)
            if len(self.info.match.table) > 0:
                self.draw_table()
            if self.info.match.winner:
                self.match_ended()

    def draw_points(self):
        font = self.info.font

    def draw_sweeps(self):
        font = self.info.font
        m = self.info.match
        screen_width = self.info.screen.get_width()
        screen_height = self.info.screen.get_height()
        # points
        p = m.points_player
        c = m.points_computer
        tp = font.render(f"Player's points: {p}", True, (200, 200, 200))
        tc = font.render(f"Computer's points: {c}", True, (200, 200, 200))
        self.info.screen.blit(
            tp, (screen_width - tp.get_width()-50, screen_height - tp.get_height() - 100))
        self.info.screen.blit(
            tc, (screen_width - tc.get_width()-50, tc.get_height() + 100))
        # sweeps
        value_player = m.sweep_player
        value_computer = m.sweep_computer
        player_text = font.render(
            f"Player's sweeps: {value_player}", True, (200, 200, 200))
        computer_text = font.render(
            f"Computer's sweeps: {value_computer}", True, (200, 200, 200))
        self.info.screen.blit(player_text, (screen_width - player_text.get_width() -
                              50, screen_height - player_text.get_height() - 50))
        self.info.screen.blit(computer_text, (screen_width -
                              computer_text.get_width()-50, player_text.get_height() + 50))

    def draw_table(self):
        i = 0
        for c in self.info.match.table:
            card_width = self.info.match.deck.get_back().image.get_width()
            x = (self.info.screen.get_width() -
                 len(self.info.match.table)*card_width)/2 + i*card_width
            y = self.info.screen.get_height()/2 - self.info.match.deck.get_back().image.get_height()/2
            if c in self.info.match.player_chosen_table_cards:
                y -= c.image.get_height()/3
            self.draw_card(c, (x, y))
            c.pos = (x, y)
            i += 1

    def draw_hand(self, hand):
        i = 0
        for c in hand:
            card_width = self.info.match.deck.get_back().image.get_width()
            if hand == self.info.match.player_hand:
                x = (self.info.screen.get_width() -
                     len(self.info.match.player_hand)*card_width)/2 + i*card_width
                y = self.info.screen.get_height()-self.info.match.deck.get_back().image.get_height()
                if c == self.info.match.player_chosen_hand_card:    # Change y for chosen card
                    y -= c.image.get_height()/3
            else:
                x = (self.info.screen.get_width(
                )-len(self.info.match.computer_hand)*card_width)/2 + i*card_width
                y = 0
            pos = (x, y)
            self.draw_card(c, pos)
            c.pos = pos
            i += 1

    def draw_card(self, card, pos):
        self.info.screen.blit(card.image, pos)

    def draw_deck(self):
        self.info.screen.blit(
            self.info.match.deck.get_back().image, self.info.deck_pos)

    def draw_game_buttons(self):
        m = self.info.match
        for button in self.info.game_buttons:
            if button.id == 3:
                cw = self.info.match.deck.get_back().image.get_width()
                button.pos = (self.info.screen.get_width(
                )/2 - (len(self.info.match.player_hand) * cw / 2) - cw, button.pos[1])
                # if m.check_if_player_can_pick_cards():
                #button.text = "pick cards"
                # else:
                #    button.text = "play to table"
                if m.round_ongoing:
                    button.text = "Play card"
                else:
                    button.text = "New round"
            button.draw()

    def draw_info_text_computer(self):
        font = self.info.font
        text = self.info.match.info_text_computer
        card_height = self.info.match.deck.get_back()
        info_text = font.render(text, True, (200, 200, 200))
        self.info.screen.blit(info_text, ((self.info.screen.get_width(
        ) / 2) - info_text.get_width() / 2, card_height.image.get_height() + 10))

    def draw_info_text_player(self):
        font = self.info.font
        text = self.info.match.info_text_player
        card_height = self.info.match.deck.get_back()
        info_text = font.render(text, True, (200, 200, 200))
        self.info.screen.blit(info_text, ((self.info.screen.get_width() / 2) - info_text.get_width() / 2,
                              self.info.screen.get_height() - card_height.image.get_height() - info_text.get_height() - 100))

    def match_ended(self):
        m = self.info.match
        m_e = MatchEnded(self.info.screen, m.winner)
        m_e.draw()
        for b in self.info.match_end_buttons:
            b.draw()
