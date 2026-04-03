import pygame
pygame.init()
pygame.display.set_caption("Pygame Window")
screen = pygame.display.set_mode((600, 400))

background_original = pygame.image.load("sky.jpg").convert()
background = pygame.transform.scale(background_original, (600, 400))

running = True
while running: 
    for event in pygame.event.get():
        screen.blit(background, (0, 0))
        button = pygame.draw.rect(screen, (255, 0, 0), (230, 50, 100, 80))

        if button.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                print("Button clicked!")
        
        pygame.display.flip()
        if event.type == pygame.QUIT:
            running = False
pygame.quit()