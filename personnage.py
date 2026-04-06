import pygame

class Personnage(pygame.sprite.Sprite):

    def __init__(self ,screen , nom , vie , atk):
        super(self.__init__)
        self.nom = nom
        self.vie = vie
        self.atk = atk

        self.images = []

        for i in range(6):
            chemin = f"assets/craftpix-net-622999-free-pixel-art-tiny-hero-sprites/rush-pink/{i+1}.PNG"
            brute = pygame.image.load(chemin).convert_alpha()
            image_redimensionnee = pygame.transform.scale(brute , (120 , 120))
            self.images.append(image_redimensionnee)

        # On charge 4 images de marche (ex: walk1.png, walk2.png...)
        # images = [pygame.image.load(f"assets/craftpix-net-622999-free-pixel-art-tiny-hero-sprites/{i+1}.PNG").convert_alpha() for i in range(4)]
        # self.images =[ pygame.transform.scale(images , (120 , 40)) for i in range(4)]

        self.rect = self.images[0].get_rect()
        self.rect.x = (screen.get_width() / 2) - (self.rect.width / 2)
        self.rect.y = (screen.get_height() / 2) - (self.rect.height / 2)

        self.index = 0
        self.animation_speed = 0.2  # Vitesse du changement d'image
        self.counter = 0        
        

    def draw(self , screen):
        if 