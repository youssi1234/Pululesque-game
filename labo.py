import pygame

pygame.init()

# Créer la fenêtre
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mon premier jeu")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    screen.fill((255, 0, 0))  # fond rouge

    pygame.draw.rect(screen, (255, 255, 255), (100, 100, 100, 50))
    pygame.draw.circle(screen, (0, 255, 0), (400, 300), 50)

    pygame.display.flip()

pygame.quit()