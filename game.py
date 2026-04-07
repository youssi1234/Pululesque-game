import pygame

from button import Button 

class Game:

    def __init__(self,etat, screen_width , screen_height):
        self.etat = etat
        self.button = Button(50 , 50 , 30 , 30 , (255, 255, 255) , "<-")
        bg = pygame.image.load("assets/sunset_clouds_over_the_sea_pixel_background/4.png").convert()
        self.bg = pygame.transform.scale(bg,(screen_width,screen_height))

    def draw(self,screen):

        screen.blit(self.bg , (0,0))
        self.button.draw(screen)

        if self.button.is_clicked():
            self.etat.switch_state("menu")