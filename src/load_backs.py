import os
from card import Card
import pygame


def load_backs(path="src/images/back/"):
    backs = []
    scale = (103, 150)
    for file in os.listdir(path):
        print(path+file)
        f = file.split("_")
        if f[0] == "back":
            num = f[1].split(".")[0]
            image = pygame.transform.scale(pygame.image.load(path+file), scale)
            backs.append(Card(num, num, "back", image))
    return backs
