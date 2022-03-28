from re import S
import pygame

class Button:
    def __init__(self, screen,text: str, size: tuple, pos: tuple):
        self.font = pygame.font.SysFont("Corbel", 35)
        self.text_color = (200,200,200)
        self.bg_color = (0,0,0)
        self.text = text
        self.size = size
        self.pos = pos
        self.screen = screen
        self.t = self.font.render(self.text, True, self.text_color)
        self.center = (self.pos[0] - self.size[0] / 2, self.pos[1] - self.size[1] / 2)
        self.text_position = (self.pos[0] - self.t.get_width() / 2, self.pos[1] - self.t.get_height() / 2)

    def draw(self):
        self.__draw_background()
        self.__draw_text()

    def __draw_text(self):
        self.screen.blit(self.t, self.text_position)

    def __draw_background(self):
        pygame.draw.rect(self.screen, self.bg_color, [self.center[0], self.center[1], self.size[0], self.size[1]])