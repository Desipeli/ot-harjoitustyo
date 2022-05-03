import pygame


class Button:
    """ Class for creating game buttons """

    def __init__(self, id: int, screen, text: str, size: tuple, pos: tuple):
        """ Constructor

            Args:
                id: Id of button object
                screen: Pygame display
                text: Text shown in button
                size: Tuple having the size of the button
                pos: Position of the button (x, y)
        """

        self.id = id
        self.font = pygame.font.SysFont("Corbel", 35)
        self.text_color = (200, 200, 200)
        self.bg_color = (0, 0, 0)
        self.text = text
        self.size = size
        self.pos = pos
        self.screen = screen
        self.t = self.font.render(self.text, True, self.text_color)
        self.__set_center()

    def draw(self):
        """ Draw button's components """

        self.__set_center()
        self.__draw_background()
        self.__draw_text()

    def __draw_text(self):
        """ Draw text on the button """

        self.t = self.font.render(self.text, True, self.text_color)
        self.screen.blit(self.t, self.text_position)

    def __set_center(self):
        """ Center the button """

        self.center = (self.pos[0] - self.size[0] / 2,
                       self.pos[1] - self.size[1] / 2)
        self.text_position = (
            self.pos[0] - self.t.get_width() / 2, self.pos[1] - self.t.get_height() / 2)

    def __draw_background(self):
        """ Draw background of the button """

        pygame.draw.rect(self.screen, self.bg_color, [
                        self.center[0], self.center[1], self.size[0], self.size[1]])
