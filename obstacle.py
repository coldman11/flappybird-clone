import pygame, sys
from random import randint

class Obstacle():
    def __init__(self):
        # obstacle parts
        self.lowerImg = pygame.image.load('obstacle.png')
        self.lowerRect = self.lowerImg.get_rect()
        self.upperImg = pygame.image.load('obstacle.png')
        self.upperRect = self.upperImg.get_rect()
        # gap
        self.gapHeight = 200
        self.randomizeGap()

    def setX(self, x):
        self.lowerRect.x = x
        self.upperRect.x = x

    def getX(self):
        return self.lowerRect.x

    def move(self, speed):
        self.lowerRect = self.lowerRect.move([-speed,0])
        self.upperRect = self.upperRect.move([-speed,0])

    def randomizeGap(self):
        self.gapY = randint(0,500 - self.gapHeight)
        self.lowerRect.y = self.gapY + self.gapHeight
        self.upperRect.y = self.gapY - self.upperRect.height