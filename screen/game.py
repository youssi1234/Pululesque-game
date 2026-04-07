import pygame

from composant.button import Button 
from composant.icon import Icon

class Game:

    def __init__(self,etat, screen_width , screen_height , screen):
        self.etat = etat
        self.button = Button(50 , 50 , 30 , 30 , (255, 255, 255) , "<-")
        bg = pygame.image.load("assets/fond/10.png").convert()
        self.bg = pygame.transform.scale(bg,(screen_width,screen_height))
        self.icon_player = Icon(screen)

    def draw(self,screen):

        screen.blit(self.bg , (0,0))
        self.button.draw(screen)
        self.icon_player.draw(screen)

        if self.button.is_clicked():
            self.etat.switch_state("menu")


    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                self.icon_player.key_Held[event.key] = True
            elif event.type == pygame.KEYUP:
                self.icon_player.key_Held[event.key] = False