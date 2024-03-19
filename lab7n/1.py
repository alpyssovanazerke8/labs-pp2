import pygame
import sys
import time
import datetime
import pytz

pygame.init()

mickey_image = pygame.image.load(r'C:\Users\Nazdr\OneDrive\Рабочий стол\pp2\lab7\main-clock.png')  
mickey_right_hand = pygame.image.load(r'C:\Users\Nazdr\OneDrive\Рабочий стол\pp2\lab7\right-hand.png')  
mickey_left_hand = pygame.image.load(r'C:\Users\Nazdr\OneDrive\Рабочий стол\pp2\lab7\left-hand.png')   

def draw_clock():
    screen.fill((255, 255, 255))  


    almaty_timezone = pytz.timezone('Asia/Almaty')
    current_time = datetime.datetime.now(almaty_timezone)
   
    minutes_angle = -current_time.minute * 6
    seconds_angle = -current_time.second * 6

    mickey_width, mickey_height = mickey_image.get_size()
    screen.blit(mickey_image, (WIDTH // 2 - mickey_width // 2, HEIGHT // 2 - mickey_height // 2))

    rotated_right_hand = pygame.transform.rotate(mickey_right_hand, minutes_angle)
    rotated_left_hand = pygame.transform.rotate(mickey_left_hand, seconds_angle)
    screen.blit(rotated_right_hand, (WIDTH // 2 - rotated_right_hand.get_width() // 2, HEIGHT // 2 - rotated_right_hand.get_height() // 2))
    screen.blit(rotated_left_hand, (WIDTH // 2 - rotated_left_hand.get_width() // 2, HEIGHT // 2 - rotated_left_hand.get_height() // 2))

    pygame.display.flip()

WIDTH, HEIGHT = 900, 900 
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Mickey Mouse Clock")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            WIDTH, HEIGHT = event.w, event.h
            screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

    draw_clock()

    
    time.sleep(1)

pygame.quit()
sys.exit()