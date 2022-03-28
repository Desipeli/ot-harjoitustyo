import pygame

class Draw:
    def __init__(self) -> None:
        self.game_stage = 0

    def draw(self, screen):
        if self.game_stage == 0:
            for b in self.menu_buttons:
                b.draw()
                print(b.center, b.size)

    pygame.display.flip()