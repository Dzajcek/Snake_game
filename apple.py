import pygame
import random

class Apple:

    def __init__(self, game):
        self.screen = game.screen
        self.color = (255, 0, 0)

    def update(self):
        x = random.randint(0, 39) * 20 
        y = random.randint(0, 29) * 20 
        self.rect = pygame.Rect(x, y, 20, 20)

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)