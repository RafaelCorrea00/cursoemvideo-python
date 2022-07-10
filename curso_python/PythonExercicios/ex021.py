import pygame

# Inicializando o mixer PyGame
pygame.mixer.init()

# Iniciando o PyGame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play(loops=0, start=0.0)
pygame.event.wait()
