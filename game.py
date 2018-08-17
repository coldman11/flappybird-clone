import sys, pygame
from random import randint
from bird import Bird

pygame.init()
running = True
screen = pygame.display.set_mode((500, 500))

obstacleimg = pygame.image.load('obstacle.png')
obstaclerect = obstacleimg.get_rect()
obstaclerect.x = 450
obstaclerect.y = randint(250,500)

# create bird

bird = Bird()

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

        #keys = pygame.key.get_pressed()  #checking pressed keys
        
        #if keys[pygame.K_UP]:
            #birdrect = birdrect.move([0,-jump])
        if bird.vy <= 10:
            bird.vy += 1
        bird.rect = bird.rect.move([0,bird.vy])
        #obstaclerect = obstaclerect.move([-flyingSpeed,0])

        #if obstaclerect.x < 0:
            #obstaclerect.x = 500
            #obstaclerect.y = randint(250,500)

        #if birdrect.colliderect(obstaclerect):
            #running = False

        
        screen.fill((0,0,0))
        screen.blit(bird.img, bird.rect)
        #screen.blit(obstacleimg, obstaclerect)
        pygame.display.flip()



