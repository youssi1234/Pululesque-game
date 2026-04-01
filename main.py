import pygame
pygame.init()
pygame.display.set_caption("Pygame Window")
screen = pygame.display.set_mode((800, 600))

running = True
while running: 
    for event in pygame.event.get():
        screen.fill((0,0,0))
        pygame.display.flip()
        if event.type == pygame.QUIT:
            running = False
pygame.quit()