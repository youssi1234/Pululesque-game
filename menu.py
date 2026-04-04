import pygame
from button import Button
from etat import Etat



class Menu:

    def __init__(self, etat):
        self.etat = etat

        # background
        bg = pygame.image.load("sky.jpg").convert_alpha()
        self.background = pygame.transform.scale(bg, (600, 400))

        # titre
        self.font_title = pygame.font.Font("typo/PIXELMANIA.TTF", 60)
        self.title_text = self.font_title.render("PULULU", True, (255, 255, 255))
        self.title_rect = self.title_text.get_rect(center=(300, 100))
        self.title_shadow = self.font_title.render("PULULU", True, (215, 255, 40))

        # bouton
        self.button = Button(230, 250, 300, 70)
        self.button.center(600)

    def draw(self, screen):

        screen.blit(self.background, (0, 0))

        screen.blit(self.title_shadow, (self.title_rect.x + 3, self.title_rect.y + 3))
        screen.blit(self.title_text, self.title_rect)

        self.button.draw(screen)

        if self.button.is_clicked():
            self.etat.switch_state("game")

    def handle_events(self, events):
        pass