import pygame
from button import Button

pygame.init()
pygame.display.set_caption("Pygame Window")
screen = pygame.display.set_mode((600, 400))

fluidity = 60
clock = pygame.time.Clock()

font_title = pygame.font.SysFont("THE FONT (FREE VERSION)", 60)
title_text = font_title.render("Pululu.Corp", True, (255, 255, 255))
title_rect = title_text.get_rect(center=(300, 200))
shadow = font_title.render("Pululu.Corp", True, (0, 0, 0))

button = Button(230, 300, 100, 80)

background_original = pygame.image.load("sky.jpg").convert_alpha()
background = pygame.transform.scale(background_original, (600, 400))


running = True
while running:
    # 1. GESTION DES ÉVÉNEMENTS (Clavier/Souris)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if button.is_clicked():
            print("Button clicked!")

    # Tandremana tsara fa kay le izy mande par ordre d'affichage otrany photoshop na gimp, 
    # le izy affiche d'abord le fond, ensuite le titre, 
    # et enfin le bouton par dessus les deux autres. 
    # Raha ovaina ny ordre dia mety tsy hiseho tsara ilay bouton 
    # na ilay titre satria mety ho afenina amin'ny sary hafa izy ireo.


    # D'abord le fond (couche du dessous)
    screen.blit(background, (0, 0))

    # Ensuite le titre (couche du milieu)
    screen.blit(shadow, (title_rect.x + 3, title_rect.y + 3)) # Ombre pour le titre
    screen.blit(title_text, title_rect)

    # Enfin le bouton (couche du dessus)
    button.draw(screen)

    # 3. MISE À JOUR DE L'ÉCRAN
    pygame.display.flip()
    clock.tick(fluidity)

pygame.quit()
