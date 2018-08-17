import pygame, sys

class Bird():
    def __init__(self):
        self.img = pygame.image.load('redbird-midflap.png')
        self.rect = self.img.get_rect()
        self.vy = 3
