import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    radius = 15
    mode = 'blue'
    points = []
    drawing_rect = False
    drawing_circle = False
    eraser_mode = False

    while True:
        
        pressed = pygame.key.get_pressed()
        
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    pygame.quit()
                    return
                if event.key == pygame.K_F4 and alt_held:
                    pygame.quit()
                    return
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key == pygame.K_e:
                    eraser_mode = not eraser_mode
                elif event.key == pygame.K_c:
                    drawing_circle = True
                elif event.key == pygame.K_t:
                    drawing_rect = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and not eraser_mode: # left click grows radius
                    radius = min(200, radius + 1)
                elif event.button == 3 and not eraser_mode: # right click shrinks radius
                    radius = max(1, radius - 1)
                elif event.button == 1 and eraser_mode: # left click erases
                    pygame.draw.circle(screen, (0, 0, 0), event.pos, radius)
                elif event.button == 3 and eraser_mode: # right click erases larger area
                    pygame.draw.rect(screen, (0, 0, 0), (event.pos[0] - radius, event.pos[1] - radius, radius * 2, radius * 2))
                elif event.button == 1 and drawing_circle: # left click to draw circle
                    pygame.draw.circle(screen, get_color(mode), event.pos, radius)
                elif event.button == 1 and drawing_rect: # left click to draw rectangle
                    start_pos = event.pos
                    drawing_rect = False
                elif event.button == 3: # right click cancels drawing rectangle or circle
                    drawing_rect = False
                    drawing_circle = False
            
            if event.type == pygame.MOUSEMOTION:
                if drawing_rect: # update rectangle position while drawing
                    end_pos = event.pos
                    pygame.draw.rect(screen, get_color(mode), (start_pos[0], start_pos[1], end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]), 3)
                elif drawing_circle: # update circle position while drawing
                    radius = abs(start_pos[0] - event.pos[0])
                    pygame.draw.circle(screen, get_color(mode), start_pos, radius, 3)

        screen.fill((0, 0, 0))
        
        pygame.display.flip()
        
        clock.tick(60)

def get_color(color_mode):
    if color_mode == 'blue':
        return (0, 0, 255)
    elif color_mode == 'red':
        return (255, 0, 0)
    elif color_mode == 'green':
        return (0, 255, 0)

main()

