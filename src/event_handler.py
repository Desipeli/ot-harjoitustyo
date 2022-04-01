import pygame
import sys
#pygame.init()

def check_event(event):
    if event.type == pygame.MOUSEBUTTONDOWN:
        print("MOI")
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()