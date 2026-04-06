import pygame
import utiles as utiles

class Icon(pygame.sprite.Sprite):
    def __init__(self, screen):
        self.key_Held = {}
        self.velocity = 5
        self.images = []

        for i in range(6):
            chemin = f"assets/craftpix-net-622999-free-pixel-art-tiny-hero-sprites/rush-pink/{i+1}.PNG"
            brute = pygame.image.load(chemin).convert_alpha()
            image_redimensionnee = pygame.transform.scale(brute , (70 , 70))
            self.images.append(image_redimensionnee)

        self.rect = self.images[0].get_rect()
        self.rect.x = (screen.get_width() / 2) - (self.rect.width / 2)
        self.rect.y = (screen.get_height() / 2) - (self.rect.height / 2)

        self.index = 0
        self.animation_speed = 0.2  # Vitesse du changement d'image
        self.counter = 0


    def move(self, screen):
        
        self.counter += self.animation_speed
        if self.counter >= len(self.images):
            self.counter = 0
        self.index = int(self.counter)

        if self.key_Held.get(pygame.K_RIGHT):
            if self.rect.x >= (screen.get_width() - self.rect.width) - utiles.marge_X(screen, 10):
                self.rect.x = (screen.get_width() - self.rect.width) - utiles.marge_X(screen, 10)
                
            else:
                self.rect.x += self.velocity

        elif self.key_Held.get(pygame.K_LEFT):
            if self.rect.x <= utiles.marge_X(screen, 10):
                self.rect.x = utiles.marge_X(screen, 10)
            else:
                self.rect.x -= self.velocity

        elif self.key_Held.get(pygame.K_UP):
            if self.rect.y <= utiles.marge_Y(screen, 10):
                self.rect.y = utiles.marge_Y(screen, 10)
            else:
                self.rect.y -= self.velocity

        elif self.key_Held.get(pygame.K_DOWN):
            if self.rect.y >= (screen.get_height() - self.rect.height) - utiles.marge_Y(screen, 10):
                self.rect.y = (screen.get_height() - self.rect.height) - utiles.marge_Y(screen, 10)
            else:
                self.rect.y += self.velocity

    def draw(self, screen):

        img = self.images[self.index]
        screen.blit(img, (self.rect.x , self.rect.y)) 
