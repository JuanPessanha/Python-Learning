import pygame
pygame.mixer.init()
pygame.mixer.music.load('c:/save.mp3')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)