import os
from card import Card
import pygame

def load_cards():
    path = "images/cards/"
    cards = []
    scale = (103,150)
    for file in os.listdir(path):
        f = file.split("_")
        v_hand = int(f[0])
        v_table = int(f[0])
        image = pygame.image.load(f"{path}{file}")
        if v_hand == 1:
            v_hand = 14
        elif v_hand == 2:
            if f[2] == "clubs.png":
                v_hand = 15
        if v_hand == 10:
            if f[2] == "diamonds.png":
                v_hand = 16
        image = pygame.transform.scale(image, scale)
        c = Card(v_hand, v_table, f[2].split(".")[0],image)
        cards.append(c)
    return cards