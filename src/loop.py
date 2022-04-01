import pygame
from event_handler import Events
from draw import Draw       

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
            # Screen background color green (0, 81, 44)
            self.info.screen.fill((0, 81, 44))

            self.draw.draw()

            # Game stage testing
            text_game_stage = self.info.font.render(f"Game stage: {self.info.game_stage}", True, (0,0,0))
            self.info.screen.blit(text_game_stage, (10,10))

            # cardtest
            #self.info.screen.blit(self.info.cards[0].image, (200,200))
            #self.info.screen.blit(self.info.backs[0].image, (200,400))

            pygame.display.flip()
            self.clock.tick(60)

    def events(self):
        for event in pygame.event.get():
            self.event.check_event(event, self.info)
