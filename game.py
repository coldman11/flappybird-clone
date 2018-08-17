import sys, pygame
from random import randint
from bird import Bird
from obstacle import Obstacle

pygame.init()
running = True
screen = pygame.display.set_mode((500, 500))

bird = Bird()
bird.rect.x = 50
bird.rect.y = 250
obstacle = Obstacle()
obstacle.setX(400)

myfont = pygame.font.SysFont("monospace", 40)

# render text
points = 0



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
        if bird.rect.y > 500 or bird.rect.y < 0:
            running = False

        obstacle.move(6)
        if obstacle.getX() < -50:
            obstacle.setX(550)
            obstacle.randomizeGap()
            points += 1

        if bird.rect.colliderect(obstacle.lowerRect) or bird.rect.colliderect(obstacle.upperRect):
            running = False

        screen.fill((0,0,0))
        screen.blit(bird.img, bird.rect)
        screen.blit(obstacle.upperImg, obstacle.upperRect)
        screen.blit(obstacle.lowerImg, obstacle.lowerRect)
        label = myfont.render(str(points), 1, (255,255,0))
        screen.blit(label, (0, 0))
        
        pygame.display.flip()



