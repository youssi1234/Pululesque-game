import pygame

class Icon(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.key_Held = {}
        self.velocity = 1
        self.images_run = []
        self.images_idle = []
        self.images_run_back = []
        self.images_idle_back = []
        self.last_direction = "right"
        self.size_image = (25, 25)

        for i in range(6):
            brute = pygame.image.load(f"assets/craftpix-net-622999-free-pixel-art-tiny-hero-sprites/rush-pink/{i+1}.PNG").convert_alpha()
            self.images_run.append(pygame.transform.scale(brute, self.size_image))
        for i in range(4):
            brute = pygame.image.load(f"assets/craftpix-net-622999-free-pixel-art-tiny-hero-sprites/idle-pink/{i+1}.PNG").convert_alpha()
            self.images_idle.append(pygame.transform.scale(brute, self.size_image))

        for i in range(6): self.images_run_back.append(pygame.transform.flip(self.images_run[i], True, False))
        for i in range(4): self.images_idle_back.append(pygame.transform.flip(self.images_idle[i], True, False))

        self.current_images = self.images_idle
        self.image = self.current_images[0]
        self.rect = self.image.get_rect()
        
        # Position de départ au centre
        self.rect.x = (screen.get_width() / 2) - (self.rect.width / 2)
        self.rect.y = (screen.get_height() / 2) - (self.rect.height / 2)
        
        # On crée la variable old_position dès le début pour éviter les erreurs
        self.old_position = self.rect.copy()

        self.index = 0
        self.animation_speed = 0.2
        self.counter = 0

    def direction(self):
        is_moving = any(self.key_Held.get(key) for key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT])
        if self.key_Held.get(pygame.K_RIGHT): self.last_direction = "right"
        elif self.key_Held.get(pygame.K_LEFT): self.last_direction = "left"

        if is_moving:
            self.current_images = self.images_run if self.last_direction == "right" else self.images_run_back
        else:
            self.current_images = self.images_idle if self.last_direction == "right" else self.images_idle_back

    def count(self):
        self.counter += self.animation_speed
        if self.counter >= len(self.current_images): self.counter = 0
        self.index = int(self.counter)
        self.image = self.current_images[self.index]

    def position(self):
        # Calcul de la vitesse diagonale (v)
        is_diag = (self.key_Held.get(pygame.K_UP) or self.key_Held.get(pygame.K_DOWN)) and \
                  (self.key_Held.get(pygame.K_LEFT) or self.key_Held.get(pygame.K_RIGHT))
        
        # Attention : v = velocity * 0.7 (multiplication, pas division !)
        v = self.velocity * 0.7 if is_diag else self.velocity
        
        # AXE X (Libre, sans marge)
        if self.key_Held.get(pygame.K_RIGHT):
            self.rect.x += v
        elif self.key_Held.get(pygame.K_LEFT):
            self.rect.x -= v

        # AXE Y (Libre, sans marge)
        if self.key_Held.get(pygame.K_UP):
            self.rect.y -= v
        elif self.key_Held.get(pygame.K_DOWN):
            self.rect.y += v

    def move(self):
        self.count()
        self.direction()
        self.position()

    def save_location(self):
        self.old_position = self.rect.copy()

    def back_to_old_position(self):
        self.rect = self.old_position.copy()
