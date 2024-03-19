import pygame
from pygame import mixer
import sys

pygame.init()
mixer.init()

# Screen dimensions
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 400

# Colors
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
mixer.music.load('sound/Can You Hear The Music.mp3')

class Button(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect(topleft=(x, y))

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

def redraw_screen():
    screen.fill(WHITE)
    for button in buttons:
        button.draw(screen)
    pygame.display.update()

buttons = [
    Button("png/p.png", 200, 100),
    Button("png/s.png", 350, 100),
    Button("png/n.png", 500, 100),
    Button("png/previous.png", 650, 100)
]

run = True
current_track_index = 0
music_files = ['1.mp3','2.mp3','3.mp3']
paused = False

while run:
    redraw_screen()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  
                pos = pygame.mouse.get_pos()
                for button in buttons:
                    if button.is_clicked(pos):
                        if button == buttons[0]: 
                            if paused:
                                mixer.music.unpause()
                            else:
                                mixer.music.load(music_files[current_track_index])
                                mixer.music.play()
                            paused = False
                        elif button == buttons[1]: 
                            mixer.music.stop()
                            paused = False
                        elif button == buttons[2]: 
                            current_track_index = (current_track_index + 1) % len(music_files)
                            mixer.music.load(music_files[current_track_index])
                            mixer.music.play()
                            paused = False
                        elif button == buttons[3]: 
                            current_track_index = (current_track_index - 1) % len(music_files)
                            mixer.music.load(music_files[current_track_index])
                            mixer.music.play()
                            paused = False
