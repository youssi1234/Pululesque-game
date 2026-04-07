import pygame
from RikiLabs.entity.icon import icon

class game(pygame.sprite.Sprite):
    def __init__(self, screen):
        self.icon_player = icon(screen)
