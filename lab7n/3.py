import pygame
import sys


pygame.init()


WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball")


WHITE = (255, 255, 255)
RED = (255, 0, 0)


br = 25
bx = (WIDTH - br) // 2
by = (HEIGHT - br) // 2
bs = 20


running = True
while running:
    screen.fill(WHITE)

   
    pygame.draw.circle(screen, RED, (bx, by), br)

  
    pygame.display.flip()

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if by - bs >= 0:
                    by -= bs
            elif event.key == pygame.K_DOWN:
                if by + bs <= HEIGHT - br:
                    by += bs
            elif event.key == pygame.K_LEFT:
                if bx - bs >= 0:
                    bx -= bs
            elif event.key == pygame.K_RIGHT:
                if bx + bs<= WIDTH - br:
                    bx += bs


pygame.quit()
sys.exit()
