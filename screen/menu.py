import pygame
from composant.button import Button


class Menu:

    def __init__(self, etat , screen_width , screen_height):
        self.etat = etat

        # background
        bg = pygame.image.load("assets/sunset_clouds_over_the_sea_pixel_background/sky.jpg").convert_alpha()
        self.background = pygame.transform.scale(bg, (screen_width, screen_height))

        # titre
        self.font_title = pygame.font.Font("typo/PIXELMANIA.TTF", 60)
        self.title_text = self.font_title.render("PULULU", True, (255, 255, 255))
        self.title_rect = self.title_text.get_rect(center=(screen_width/2, 100))
        self.title_shadow = self.font_title.render("PULULU", True, (215, 255, 40))

        # bouton
        self.button = Button(230, 400, 300, 70 ,(255, 255, 255), "PlY BOY")
        self.button.center(screen_width)

    def draw(self, screen):
        

        screen.blit(self.background, (0, 0))

        screen.blit(self.title_shadow, (self.title_rect.x + 3, self.title_rect.y + 3))
        screen.blit(self.title_text, self.title_rect)

        self.button.draw(screen)

        if self.button.is_clicked():
            
            self.etat.switch_state("loading")

    def handle_events(self, events):
        pass