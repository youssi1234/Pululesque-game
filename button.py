import pygame


class Button:
    def __init__(self , x, y, width, height):

        self.rect_original = pygame.Rect(x, y, width, height)  # Garder une copie de la position originale
        self.rect = self.rect_original.copy()  # Pratique pour les collisions
        self.color = (255, 255, 255)  # Couleur de base du bouton (steel blue)
        self.hover_color = (220, 220, 220)  # Couleur du bouton au survol
        self.text = "Cliquez ici"
        self.font = pygame.font.Font("typo/PIXELIFYSANS-BOLD.TTF", 20)

    def draw(self, screen):
        if self.is_hovered():
            color = self.hover_color
        else:
            color = self.color

        pygame.draw.rect(screen, color, self.rect )
        text_surf = self.font.render(self.text, True, (0, 0, 0))
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)

    def is_hovered(self):
        self.rect.x = self.rect_original.x
        self.rect.y = self.rect_original.y
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            # scale le boutton + 5
            self.rect.x -= 5
            self.rect.y -= 5
            return True
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)
        return False

    def is_clicked(self):
        if self.is_hovered() and pygame.mouse.get_pressed()[0]:
            return True
        return False

    def center(self, screen_width):
        """Centre uniquement l'horizontale"""
        self.rect_original.x = (screen_width - self.rect_original.width) // 2
        
