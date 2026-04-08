import pygame
import RikiLabs.utiles as utiles

class icon(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.key_Held = {}
        self.velocity = 3
        self.image = pygame.image.load('RikiLabs/assets/jeu.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


    def move(self):
        
        if self.key_Held.get(pygame.K_RIGHT):
            self.rect.x += self.velocity

        elif self.key_Held.get(pygame.K_LEFT):
            self.rect.x -= self.velocity

        elif self.key_Held.get(pygame.K_UP):
            self.rect.y -= self.velocity

        elif self.key_Held.get(pygame.K_DOWN):
            self.rect.y += self.velocity