import pygame
from event_handler import Events
from ui.draw import Draw


class Loop:

    def __init__(self, info) -> None:
        self.draw = Draw(info)
        self.info = info
        self.event = Events()
        self.clock = pygame.time.Clock()
        self.loop()

    def loop(self):

        while True:
            # Events
            self.events()
            self.info.screen.fill((0, 81, 44))
            self.draw.draw()
            # Game stage testing
            text_game_stage = self.info.font.render(
                f"Game stage: {self.info.game_stage}", True, (0, 0, 0))
            self.info.screen.blit(text_game_stage, (10, 10))
            pygame.display.flip()
            self.clock.tick(60)

    def events(self):
        for event in pygame.event.get():
            self.event.check_event(event, self.info)
