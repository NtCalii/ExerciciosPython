'''Faça um programa em python que abra e reproduza o áudio de um arquivo mp3.'''
#o arquivo da música precisa estar no projeto, basta copiar ele e colar no projeto.

import pygame

pygame.init()
pygame.mixer.music.load("ex021.mp3")
pygame.mixer.music.play()
input()
pygame.event.wait()
