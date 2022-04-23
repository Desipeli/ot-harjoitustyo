import pygame


class MatchEnded:
    def __init__(self, screen, winner="player"):
        self.screen = screen
        self.winner = winner
        self.font = pygame.font.SysFont("Corbel", 35)
        self.header_color = (200, 200, 200)
        self.points_color = (200, 200, 200)
        self.bg_width = self.screen.get_width() * 0.8
        self.bg_height = self.screen.get_height() / 2

    def draw(self):
        self.__draw_background()
        self.__draw_text()

    def __draw_background(self):
        pygame.draw.rect(self.screen, (0, 41, 24), [self.screen.get_width(
        )/2 - self.bg_width/2, self.screen.get_height()/2 - self.bg_height/2, self.bg_width, self.bg_height])

    def __draw_text(self):
        text = ""
        if self.winner == "player":
            text = "Congratulations, You won!"
        else:
            text = "Better luck next time!"
        rendered = self.font.render(text, True, (self.header_color))
        t_pos = (self.screen.get_width()/2 - rendered.get_width()/2,
                 self.screen.get_height()/2 - rendered.get_height()/2)
        self.screen.blit(rendered, t_pos)
