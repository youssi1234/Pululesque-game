import pygame

class icon(pygame.sprite.Sprite):
    def __init__(self):
        self.key_Held = {}
        self.velocity = 1
        self.image = pygame.image.load('RikiLabs/assets/jeu.png')
        self.rect = self.image.get_rect()


    def move(self, screen):
        
        if self.key_Held.get(pygame.K_RIGHT):
            if self.rect.x == screen.get_width():
                self.rect.x = screen.get_width()
            else:
                self.rect.x += self.velocity

        elif self.key_Held.get(pygame.K_LEFT):
            if self.rect.x == 0:
                self.rect.x = 0
            else:
                self.rect.x -= self.velocity

        elif self.key_Held.get(pygame.K_UP):
            if self.rect.y == 0:
                self.rect.y = 0
            else:
                self.rect.y -= self.velocity

        elif self.key_Held.get(pygame.K_DOWN):
            if self.rect.y == screen.get_height():
                self.rect.y = screen.get_height()
            else:
                self.rect.y += self.velocity
