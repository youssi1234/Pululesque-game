import pygame

class map(pygame.sprite.Sprite):
    def __init__(self, screen):
        self.velocity = 1
        self.image = pygame.image.load('RikiLabs/assets/mapEx.jpg')
        self.rect = self.image.get_rect()
        self.rect.x = (screen.get_width()/2) - (self.rect.width/2)
        self.rect.y = (screen.get_height()/2) - (self.rect.height/2)