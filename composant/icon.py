import pygame
import composant.utiles as utiles

class Icon(pygame.sprite.Sprite):
    def __init__(self, screen):
        self.key_Held = {}
        self.velocity = 10
        self.images_run = []
        self.images_idle = []
        self.images_run_back = []
        self.images_idle_back = []
        self.last_direction = "right"  # Par défaut, le personnage regarde vers la droite

        for i in range(6):
            brute = pygame.image.load(f"assets/craftpix-net-622999-free-pixel-art-tiny-hero-sprites/rush-pink/{i+1}.PNG").convert_alpha()
            self.images_run.append(pygame.transform.scale(brute, (70, 70)))
            
        for i in range(4):
            brute = pygame.image.load(f"assets/craftpix-net-622999-free-pixel-art-tiny-hero-sprites/idle-pink/{i+1}.PNG").convert_alpha()
            self.images_idle.append(pygame.transform.scale(brute, (70, 70)))

        for i in range(6):
            self.images_run_back.append(pygame.transform.flip(self.images_run[i], True, False))
            
        for i in range(4):
            self.images_idle_back.append(pygame.transform.flip(self.images_idle[i], True, False))

        self.current_images = self.images_idle

        self.rect = self.images_run[0].get_rect()
        self.rect.x = (screen.get_width() / 2) - (self.rect.width / 2)
        self.rect.y = (screen.get_height() / 2) - (self.rect.height / 2)

        self.index = 0
        self.animation_speed = 0.2
        self.counter = 0

    def direction(self):

        # ito ilay fonction any le ntenenko anla teo 
        is_moving = any(self.key_Held.get(key) for key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT])
        
        # reto ndray mila raisiko par cas ilay izy iverifiena ny touche appuyé
        is_moving_up = self.key_Held.get(pygame.K_UP)
        is_moving_down = self.key_Held.get(pygame.K_DOWN)
        is_moving_left = self.key_Held.get(pygame.K_LEFT)
        is_moving_right = self.key_Held.get(pygame.K_RIGHT)

        if is_moving_right:
            self.last_direction = "right"
        elif is_moving_left:
            self.last_direction = "left"

        if is_moving:
            self.current_images = self.images_run if self.last_direction == "right" else self.images_run_back
        else:
            self.current_images = self.images_idle if self.last_direction == "right" else self.images_idle_back

    def count(self):
        self.counter += self.animation_speed
        if self.counter >= len(self.current_images):
            self.counter = 0
        self.index = int(self.counter)

    def position(self,screen):

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

        if self.key_Held.get(pygame.K_UP):
            if self.rect.y <= utiles.marge_Y(screen, 10):
                self.rect.y = utiles.marge_Y(screen, 10)
            else:
                self.rect.y -= self.velocity

        elif self.key_Held.get(pygame.K_DOWN):
            if self.rect.y >= (screen.get_height() - self.rect.height) - utiles.marge_Y(screen, 10):
                self.rect.y = (screen.get_height() - self.rect.height) - utiles.marge_Y(screen, 10)
            else:
                self.rect.y += self.velocity

    def move(self, screen):
        self.direction()
        self.count()
        self.position(screen)

    def draw(self, screen):

        img = self.current_images[self.index]
        screen.blit(img, (self.rect.x , self.rect.y)) 
