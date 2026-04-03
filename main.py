import pygame
from button import Button

pygame.init()

size_screen = (600, 400)
pygame.display.set_caption("Pygame Window")
screen = pygame.display.set_mode(size_screen)


fluidity = 60
clock = pygame.time.Clock()

size_title = 60

font_title = pygame.font.Font("typo/PIXELMANIA.TTF", size_title)
title_text = font_title.render("PULULU", True, (255, 255, 255))
title_rect = title_text.get_rect(center=(300, 100))
shadow = font_title.render("PULULU", True, (215, 255, 40))


size_button = (300, 80)

button = Button(230, 250, size_button[0], size_button[1])
button.center(size_screen[0]) # Centrage du bouton en tenant compte de la taille du titre

shadow_brutalist = pygame.Surface((size_button[0], size_button[1]), pygame.SRCALPHA)
shadow_brutalist.fill((215, 255, 40, 255)) # Ombre pour un effet brutaliste

background_original = pygame.image.load("sky.jpg").convert_alpha()
background = pygame.transform.scale(background_original, size_screen)


running = True
while running:
    # 1. GESTION DES ÉVÉNEMENTS (Clavier/Souris)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if button.is_clicked():
            print("Button clicked!")


    # D'abord le fond (couche du dessous)
    screen.blit(background, (0, 0))

    # Ensuite le titre (couche du milieu)
    screen.blit(shadow, (title_rect.x + 3, title_rect.y + 3)) # Ombre pour le titre
    screen.blit(title_text, title_rect)
    screen.blit(shadow_brutalist, (button.rect.x + 5, button.rect.y + 5)) # Ombre pour le bouton

    # Enfin le bouton (couche du dessus)
    button.draw(screen)

    pygame.display.flip()
    clock.tick(fluidity)

pygame.quit()
