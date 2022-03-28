import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode([640,400])

    running = True
    while running:
        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # Screen background color green (0, 81, 44)
        screen.fill((0, 81, 44))

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()