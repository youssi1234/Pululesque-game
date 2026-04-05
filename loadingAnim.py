import pygame 

class LoadingAnim:
    def __init__(self):

        self.images = []
        for i in range(6):
            chemin = f"assets/craftpix-net-622999-free-pixel-art-tiny-hero-sprites/walk-pink/{i+1}.PNG"
            brute = pygame.image.load(chemin).convert_alpha()
            image_redimensionnee = pygame.transform.scale(brute , (120 , 120))
            self.images.append(image_redimensionnee)

        # On charge 4 images de marche (ex: walk1.png, walk2.png...)
        # images = [pygame.image.load(f"assets/craftpix-net-622999-free-pixel-art-tiny-hero-sprites/{i+1}.PNG").convert_alpha() for i in range(4)]
        # self.images =[ pygame.transform.scale(images , (120 , 40)) for i in range(4)]

        self.index = 0
        self.animation_speed = 0.2  # Vitesse du changement d'image
        self.counter = 0

    def draw(self, screen):
        # 1. Calculer quelle image afficher
        self.counter += self.animation_speed
        if self.counter >= len(self.images):
            self.counter = 0
        self.index = int(self.counter)

        # 2. Afficher l'image en bas à droite (600x400 est ton écran)
        img = self.images[self.index]
        screen.blit(img, (460, 260)) 
