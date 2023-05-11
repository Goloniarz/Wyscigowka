import pygame
import random
from pygame.locals import *

size = width, height = (1200, 800)
road_width = int(width / 1.6)
roadmark_width = int(width / 80)
right_lane = width / 2 + road_width / 4
left_lane = width / 2 - road_width / 4
speed = 1
score = 0
level = 1

pygame.init()
pygame.display.set_caption('Wyscigowka')

run = True
screen = pygame.display.set_mode(size)
screen.fill((0, 255, 0))

font = pygame.font.Font(None, 36)

car = pygame.image.load("car.png")
car_loc = car.get_rect()
car_loc.center = right_lane, height * 0.8

car2 = pygame.image.load("othercar.png")
car2_loc = car2.get_rect()
car2_loc.center = left_lane, height * 0.2

counter = 0

while run:
    counter += 1
    if counter == 1024:
        speed += 0.25
        counter = 0
        level += 1
        print("LEVEL UP", level)
        
    car2_loc[1] += speed
    if car2_loc[1] > height:
        if random.randint(0, 1) == 0:
            car2_loc.center = right_lane, -200
        else:
            car2_loc.center = left_lane, -200

    if car_loc[0] == car2_loc[0] and car2_loc[1] > car_loc[1] - 250:
        print("Game Over")
        break

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == KEYDOWN:
            if event.key in [K_a, K_LEFT]:
                car_loc = car_loc.move([-int(road_width / 2), 0])
            if event.key in [K_d, K_RIGHT]:
                car_loc = car_loc.move([int(road_width / 2), 0])

    pygame.draw.rect(screen, (50, 50, 50), (width / 2 - road_width / 2, 0, road_width, height))
    pygame.draw.rect(screen, (255, 240, 60), (width / 2 - roadmark_width / 2, 0, roadmark_width, height))
    pygame.draw.rect(screen, (255, 255, 255), (width / 2 - road_width / 2 + roadmark_width * 2, 0, roadmark_width, height))
    pygame.draw.rect(screen, (255, 255, 255), (width / 2 + road_width / 2 - roadmark_width * 2, 0, roadmark_width, height))

    screen.blit(car, car_loc)
    screen.blit(car2, car2_loc)

    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    
    level_text = font.render("Level: " + str(level), True, (255, 255, 255))
    screen.blit(level_text, (10, 50))

    pygame.display.update()

    score += 1

pygame.quit()
