import pygame
from icon import Icon

class Perso(pygame.sprite.Sprite):
    def __init__(self, screen):
        self.icon_player = Icon(screen)
