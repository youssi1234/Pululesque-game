import pygame

class Personnage:

    def __init__(self , x , y , width , height , nom , vie , atk):
        self.nom = nom
        self.vie = vie
        self.atk = atk
        self.image = pygame.image.load("").convert()
        self.rect_original = pygame.Rect(
            x, y, width, height
        )
        self.rect = self.rect_original.copy()


    def draw(self , screen):
        