import pygame

class icon(pygame.sprite.Sprite):
    def __init__(self):
        self.key_Held = {}
        self.velocity = 1
        self.image = pygame.image.load('RikiLabs/assets/jeu.png')
        self.rect = self.image.get_rect()


    def move(self):
        if self.key_Held.get(pygame.K_RIGHT):
            self.rect.x += self.velocity
        elif self.key_Held.get(pygame.K_LEFT):
            self.rect.x -= self.velocity
        elif self.key_Held.get(pygame.K_UP):
            self.rect.y -= self.velocity
        elif self.key_Held.get(pygame.K_DOWN):
            self.rect.y += self.velocity
