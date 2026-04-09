import pygame

from composant.button import Button 
from composant.icon import Icon
from screen.map import Map
class Game:

    def __init__(self,etat, screen):
        self.etat = etat
        self.button = Button(50 , 50 , 30 , 30 , (255, 255, 255) , "<-")
        self.icon_player = Icon(screen)
        self.map = Map(screen , self.icon_player)

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                self.icon_player.key_Held[event.key] = True
            elif event.type == pygame.KEYUP:
                self.icon_player.key_Held[event.key] = False

    def draw(self, screen):
        
        self.map.draw()
        self.button.draw(screen)

        if self.button.is_clicked():
            self.etat.switch_state("menu")

    def update(self):
        self.icon_player.save_location() # 1. Sauvegarde
        self.icon_player.move()          # 2. Avance
        
        # 3. Vérifie et recule si collision
        for wall in self.map.walls:
            if self.icon_player.rect.colliderect(wall):
                self.icon_player.back_to_old_position()
                break # On arrête de vérifier dès qu'on touche un mur
        
        self.map.update() # 4. Met à jour la caméra après le mouvement corrigé

