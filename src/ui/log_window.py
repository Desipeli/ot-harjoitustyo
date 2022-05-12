import pygame


class LogWindow:
    """ Small ingame window to show info on actions of computer player """

    def __init__(self, screen):
        """ Constructor

            Args:
                screen: Pygame display
        """

        self.screen = screen
        self.font = pygame.font.SysFont("Corbel", 24)
        self.header_color = (200, 200, 200)
        self.points_color = (200, 200, 200)
        self.top = self.screen.get_height()*0.62
        self.bottom = self.screen.get_height() - self.top - 5
        self.left = 5
        self.right = self.screen.get_width()/3
        self.message_count = int(self.bottom/self.font.get_height())
        print(self.message_count, self.font.get_height())

    def draw(self, text):
        """ Draw log. First background, the text """

        self.__draw_background()
        self.__draw_text(text)

    def __draw_background(self):
        pygame.draw.rect(self.screen, (20, 20, 20), [
                         self.left, self.top, self.right, self.bottom])

    def __draw_text(self, texts):
        """ Draw the last n lines of log. Depends on size of window and font

            Args:
                texts: List containing strings. Each to own row.
        """

        if len(texts) > self.message_count:
            texts = texts[-self.message_count:]
        i = 0
        for t in texts:
            rendered = self.font.render(t, True, (self.header_color))
            t_pos = (self.left, self.top + i * self.font.get_height())
            self.screen.blit(rendered, t_pos)
            i += 1
