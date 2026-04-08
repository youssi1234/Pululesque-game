import pygame
import composant.utiles as utiles

class Icon(pygame.sprite.Sprite):
    def __init__(self, screen):
        self.key_Held = {}
        self.velocity = 2
        self.images_run = []
        self.images_idle = []
        self.images_run_back = []
        self.images_idle_back = []
        self.last_direction = "right"  # Par défaut, le personnage regarde vers la droite
        self.size_image = (25, 25)
        self.marge = 3

        for i in range(6):
            brute = pygame.image.load(f"assets/craftpix-net-622999-free-pixel-art-tiny-hero-sprites/rush-pink/{i+1}.PNG").convert_alpha()
            self.images_run.append(pygame.transform.scale(brute, self.size_image))
            
        for i in range(4):
            brute = pygame.image.load(f"assets/craftpix-net-622999-free-pixel-art-tiny-hero-sprites/idle-pink/{i+1}.PNG").convert_alpha()
            self.images_idle.append(pygame.transform.scale(brute, self.size_image))

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

    def position(self, screen):
    # 1. On prépare les limites en nombres ENTIERS (int)
        # Cela évite que le perso reste coincé à cause des chiffres après la virgule
        m_x = int(utiles.marge_X(screen, self.marge))
        m_y = int(utiles.marge_Y(screen, self.marge))
        
        limite_droite = int(screen.get_width() - self.rect.width - m_x)
        limite_bas = int(screen.get_height() - self.rect.height - m_y)

        # 2. GESTION DE L'AXE HORIZONTAL (X)
        if self.key_Held.get(pygame.K_RIGHT):
            if self.rect.x >= limite_droite:
                self.rect.x = limite_droite
            else:
                self.rect.x += self.velocity
                
        elif self.key_Held.get(pygame.K_LEFT):
            if self.rect.x <= m_x:
                self.rect.x = m_x
            else:
                self.rect.x -= self.velocity

        # 3. GESTION DE L'AXE VERTICAL (Y)
        # On utilise un nouveau "if" (pas de elif ici) pour permettre les diagonales
        if self.key_Held.get(pygame.K_UP):
            if self.rect.y <= m_y:
                self.rect.y = m_y
            else:
                self.rect.y -= self.velocity
                
        elif self.key_Held.get(pygame.K_DOWN):
            if self.rect.y >= limite_bas:
                self.rect.y = limite_bas
            else:
                self.rect.y += self.velocity


    def move(self, screen):
        self.direction()
        self.count()
        self.position(screen)

    def draw(self, screen):

        img = self.current_images[self.index]
        screen.blit(img, (self.rect.x , self.rect.y)) 
