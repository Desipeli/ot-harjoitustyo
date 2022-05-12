import pygame
from event_handler import Events
from ui.draw import Draw


class Loop:

    def __init__(self, info) -> None:
        """ Constructor of loop class

            Args:
                info: Info-object that stores app's information
        """

        self.draw = Draw(info)
        self.info = info
        self.event = Events()
        self.clock = pygame.time.Clock()
        self.loop()

    def loop(self):
        while True:
            self.events()
            self.info.screen.fill((0, 81, 44))
            self.draw.draw()
            pygame.display.flip()
            self.clock.tick(60)

    def events(self):
        """ Event check. Calls check_event module that handles events """

        for event in pygame.event.get():
            self.event.check_event(event, self.info)
