import pygame
from RikiLabs.entity.icon import icon
from RikiLabs.map.map import map

class game(pygame.sprite.Sprite):
    def __init__(self, screen):
        self.icon_player = icon(screen)
        self.mapEx = map(screen)