import sys, pygame
from random import randint
from bird import Bird
from obstacle import Obstacle

pygame.init()
running = True
screen = pygame.display.set_mode((500, 500))

obstacleimg = pygame.image.load('obstacle.png')
obstaclerect = obstacleimg.get_rect()
obstaclerect.x = 450
obstaclerect.y = randint(250,500)

# create bird

bird = Bird()
obstacle = Obstacle()
obstacle.setX(400)

jump = 100
flyingSpeed = 3

clock=pygame.time.Clock()

def gameOver():
    running = False

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    while running:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    bird.vy = -10

        if bird.vy <= 10:
            bird.vy += 1
        bird.rect = bird.rect.move([0,bird.vy])

        obstacle.move(3)
        if obstacle.getX() < -50:
            obstacle.setX(550)
            obstacle.randomizeGap()

        if bird.rect.colliderect(obstacle.lowerRect) or bird.rect.colliderect(obstacle.upperRect):
            running = False

        screen.fill((0,0,0))
        screen.blit(bird.img, bird.rect)
        screen.blit(obstacle.upperImg, obstacle.upperRect)
        screen.blit(obstacle.lowerImg, obstacle.lowerRect)
        
        pygame.display.flip()



