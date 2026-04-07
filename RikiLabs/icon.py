import pygame
import utiles

class icon(pygame.sprite.Sprite):
    def __init__(self, screen):
        self.key_Held = {}
        self.velocity = 1
        self.image = pygame.image.load('RikiLabs/assets/jeu.png')
        self.rect = self.image.get_rect()
        self.rect.x = (screen.get_width() / 2) - (self.rect.width / 2)
        self.rect.y = (screen.get_height() / 2) - (self.rect.height / 2)


    def move(self, screen):
        
        if self.key_Held.get(pygame.K_RIGHT):
            if self.rect.x >= (screen.get_width() - self.rect.width) - utiles.marge_X(screen, 10):
                self.rect.x = (screen.get_width() - self.rect.width) - utiles.marge_X(screen, 10)
            else:
                self.rect.x += self.velocity

        elif self.key_Held.get(pygame.K_LEFT):
            if self.rect.x == utiles.marge_X(screen, 10):
                self.rect.x = utiles.marge_X(screen, 10)
            else:
                self.rect.x -= self.velocity

        elif self.key_Held.get(pygame.K_UP):
            if self.rect.y == utiles.marge_Y(screen, 10):
                self.rect.y = utiles.marge_Y(screen, 10)
            else:
                self.rect.y -= self.velocity

        elif self.key_Held.get(pygame.K_DOWN):
            if self.rect.y >= (screen.get_height() - self.rect.height) - utiles.marge_Y(screen, 10):
                self.rect.y = (screen.get_height() - self.rect.height) - utiles.marge_X(screen, 10)
            else:
                self.rect.y += self.velocity
