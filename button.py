import pygame


class Button:
    def __init__(
        self,
        x,
        y,
        width,
        height,
    ):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = "#303f50"
        self.hover_color = "#4b637e"
        self.rect = pygame.Rect(x, y, width, height) # Pratique pour les collisions
        self.text = "Cliquez ici"
        self.font = pygame.font.SysFont("Arial", 20)
        self.radius = 30

    def draw(self, screen):
        if self.is_hovered():
            color = self.hover_color
        else:
            color = self.color


        pygame.draw.rect(screen, color, (self.x, self.y, self.width, self.height))
        text_surf = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surf.get_rect(
            center=(self.x + self.width // 2, self.y + self.height // 2)
        )
        screen.blit(text_surf, text_rect)

    def is_hovered(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if (
            self.x < mouse_x < self.x + self.width
            and self.y < mouse_y < self.y + self.height
        ):
            return True
        return False

    def is_clicked(self):
        if self.is_hovered() and pygame.mouse.get_pressed()[0]:
            return True
        return False
