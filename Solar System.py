import pygame
import time
import math
import random
from PIL import Image
# sizes = 695508, 69911, 58232, 25362, 24622, 6371, 6052, 3390, 2440

width = 1000
height = 700

display = pygame.display.set_mode((width, height))

info = pygame.display.Info()

sunImage = pygame.image.load('Images\\Sun.png')
pygame.display.toggle_fullscreen = True
pygame.display.set_caption("Solar System")

class Planet:
    def __init__(self, size, satellites):
        self.size = size
        self.satellites = satellites
        self.x = 0
        self.y = 0
        self.speed = 0.0031
        self.color = (100, 142, 24)
        self.radians = 5.1
        image = 0

    def draw(self):
        display.blit(self.image, (self.x, self.y))

    def move(self):
        self.radians += self.speed
        self.x = self.x + math.cos(self.radians)
        self.y = self.y + math.sin(self.radians)

class Moon:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.speed = 0


totalSize = 850000

sunSize = 400000
sunPos = (info.current_w//2, info.current_h//2)

planets = [Planet(2440, 3), Planet(6052, 3), Planet(6371, 1), Planet(3390, 2),
Planet(69911, 79), Planet(58232, 300), Planet(25362, 27), Planet(24622, 13)]
nextPos = (info.current_w//2, info.current_h//2)

circleSize = ((sunSize * height // 2) // totalSize) // 2 + 5
print(circleSize)
sunSize = ((sunSize * height // 2) // totalSize) // 2 + 5
pygame.draw.circle(display, (100, 142, 24), nextPos, circleSize, circleSize)

nextPos = (nextPos[0] - circleSize - 30, nextPos[1] - 100)

planets[2].speed = 0.0031

speed = 0.0031

images = ["Images\\1.png", "Images\\2.png", "Images\\3.png", "Images\\4.png",
"Images\\5.png", "Images\\6.png", "Images\\7.png", "Images\\8.png"]

n = 0
for planet in planets:
    circleSize = ((planet.size * height // 2) // totalSize) // 2 + 5
    planet.size = circleSize
    planet.x = nextPos[0]
    planet.y = nextPos[1]
    img = Image.open(images[n])
    img = img.resize((circleSize + 30, circleSize + 30), Image.ANTIALIAS)
    img.save(images[n])
    img = pygame.image.load(images[n])
    planet.image = img
    planet.draw()
    planet.speed = speed
    speed += 0.0001
    nextPos = (nextPos[0] - circleSize - 30, nextPos[1])
    n += 1


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    display.fill((0, 0, 0))

    display.blit(sunImage, sunPos)

    for planet in planets:
        planet.move()
        planet.draw()

    pygame.display.update()
