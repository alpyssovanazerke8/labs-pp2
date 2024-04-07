import pygame
import random
import sys

pygame.init()

W, H = 1200, 800
FPS = 60

screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
clock = pygame.time.Clock()
done = False
bg = (0, 0, 0)

# Paddle
paddleW = 150
paddleH = 25
paddleSpeed = 20
paddle = pygame.Rect(W // 2 - paddleW // 2, H - paddleH - 30, paddleW, paddleH)

# Ball
ballRadius = 20
ballSpeed = 6
ball_rect = int(ballRadius * 2 ** 0.5)
ball = pygame.Rect(random.randrange(ball_rect, W - ball_rect), H // 2, ball_rect, ball_rect)
dx, dy = 1, -1

# Game score
game_score = 0
game_score_fonts = pygame.font.SysFont('comicsansms', 40)
game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (0, 0, 0))
game_score_rect = game_score_text.get_rect()
game_score_rect.center = (210, 20)

# Catching sound
collision_sound = pygame.mixer.Sound('catch.mp3')

# Pause screen
pause_font = pygame.font.SysFont('comicsansms', 40)
pause_text = pause_font.render('Pause', True, (255, 255, 255))
pause_text_rect = pause_text.get_rect()

pause_text_rect.center = (W // 2, H // 2)

# Set transparency level for pause screen
pause_surface = pygame.Surface((W, H), pygame.SRCALPHA)
pause_surface.set_alpha(128) 

# Create unbreakable bricks
unbreakable_block_list = [pygame.Rect(10 + 120 * i, 50 + 70 * j,
                                      100, 50) for i in range(10) for j in range(1)]

# Block settings
block_list = [pygame.Rect(10 + 120 * i, 50 + 70 * j,
                           100, 50) for i in range(10) for j in range(2, 5)]
color_list = [(random.randrange(0, 255), 
               random.randrange(0, 255),  
               random.randrange(0, 255))
              for i in range(10) for j in range(4)]

# Game over Screen
losefont = pygame.font.SysFont('comicsansms', 40)
losetext = losefont.render('Game Over', True, (255, 255, 255))
losetextRect = losetext.get_rect()
losetextRect.center = (W // 2, H // 2)

# Win Screen
winfont = pygame.font.SysFont('comicsansms', 40)
wintext = losefont.render('You win yay', True, (0, 0, 0))
wintextRect = wintext.get_rect()
wintextRect.center = (W // 2, H // 2)

# Additional Features
time_elapsed = 0  
speed_increase_rate = 0.01 
paddle_shrink_rate = 0.001  

paused = False

# Define function to display main menu
def main_menu():
    menu_font = pygame.font.SysFont('comicsansms', 40)
    menu_options = ["Play", "Settings", "Quit"]
    selected_option = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % len(menu_options)
                elif event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % len(menu_options)
                elif event.key == pygame.K_RETURN:
                    if selected_option == 0:  # Play
                        return
                    elif selected_option == 1:  # Settings
                        settings_menu()
                    elif selected_option == 2:  # Quit
                        pygame.quit()
                        sys.exit()
        
        screen.fill((0, 0, 0))
        for i, option in enumerate(menu_options):
            color = (255, 255, 255) if i == selected_option else (128, 128, 128)
            text = menu_font.render(option, True, color)
            text_rect = text.get_rect(center=(W // 2, H // 2 + 50 * i))
            screen.blit(text, text_rect)
        
        pygame.display.flip()
        clock.tick(FPS)

# Define function to display settings menu
def settings_menu():
    # Define initial settings values
    ball_speed = ballSpeed
    paddle_speed = paddleSpeed
    ball_color_index = 0  # Index for selecting ball color
    
    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]  # Define available ball colors
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    ball_color_index = (ball_color_index - 1) % len(colors)
                elif event.key == pygame.K_DOWN:
                    ball_color_index = (ball_color_index + 1) % len(colors)
                elif event.key == pygame.K_RETURN:
                    if selected_setting == 0:  # Apply changes
                        ballSpeed = ball_speed
                        paddleSpeed = paddle_speed
                        return
                    elif selected_setting == 1:  # Back to main menu
                        return

        screen.fill((0, 0, 0))
        # Display settings options and their current values
        text_color = (255, 255, 255) if selected_setting == 0 else (128, 128, 128)
        pygame.draw.rect(screen, text_color, pygame.Rect(100, 100, 200, 50), 3)
        color_text = game_score_fonts.render("Ball Color", True, (255, 255, 255))
        screen.blit(color_text, (100, 50))
        pygame.draw.rect(screen, colors[ball_color_index], pygame.Rect(100, 100, 200, 50))
        
        pygame.display.flip()
        clock.tick(FPS)

# Game loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                paused = not paused

    if paused:
        # Draw semi-transparent background
        screen.blit(pause_surface, (0, 0))
        
        # Draw "Pause" text
        screen.blit(pause_text, pause_text_rect)
        
        pygame.display.flip()
        clock.tick(FPS)
        continue

    screen.fill(bg)
    ball_speed = ballSpeed
    paddle_speed = paddleSpeed
    ball_color_index = 0
    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
    
    # Draw unbreakable blocks
    [pygame.draw.rect(screen, (255, 0, 0), unbreakable_block) for unbreakable_block in unbreakable_block_list]

    # Draw regular blocks
    [pygame.draw.rect(screen, color_list[color], block)
     for color, block in enumerate (block_list)]

    pygame.draw.rect(screen, pygame.Color(255, 255, 255), paddle)
    pygame.draw.circle(screen, colors[ball_color_index], ball.center, ballRadius)

    ball.x += ballSpeed * dx
    ball.y += ballSpeed * dy

    # Check for collisions with walls and paddle
    if ball.centerx < ballRadius or ball.centerx > W - ballRadius:
        dx = -dx
    if ball.centery < ballRadius + 50: 
        dy = -dy
    if ball.colliderect(paddle) and dy > 0:
        dx, dy = dx, -dy

    # Check for collisions with regular blocks
    hitIndex = ball.collidelist(block_list)
    if hitIndex != -1:
        hitRect = block_list.pop(hitIndex)
        hitColor = color_list.pop(hitIndex)
        dx, dy = dx, -dy
        game_score += 1
        collision_sound.play()

    # Check for collisions with unbreakable blocks
    unbreakable_hitIndex = ball.collidelist(unbreakable_block_list)
    if unbreakable_hitIndex != -1:
        dx, dy = dx, -dy

    # Update game score text
    game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (255, 255, 255))
    screen.blit(game_score_text, game_score_rect)
    
    # Game Over Conditions
    if ball.bottom > H:
        screen.fill((0, 0, 0))
        screen.blit(losetext, losetextRect)
    elif not len(block_list):
        screen.fill((255,255, 255))
        screen.blit(wintext, wintextRect)

    # Move paddle
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddleSpeed
    if key[pygame.K_RIGHT] and paddle.right < W:
        paddle.right += paddleSpeed

    # Increase ball speed with time
    time_elapsed += 1 / FPS
    ballSpeed += speed_increase_rate * time_elapsed

    # Shrink paddle with time
    paddleW -= paddle_shrink_rate * time_elapsed
    paddle.width = max(int(paddleW), 10)  
    
    pygame.display.flip()
    clock.tick(FPS)

    # Display main menu at the beginning and pause menu when paused
    if not paused:
        main_menu()

pygame.quit()
