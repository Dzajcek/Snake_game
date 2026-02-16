import pygame
import random

class Apple:

    def __init__(self, game):
        self.screen = game.screen
        self.color = (255, 0, 0)
        self.x = random.randint(0, 780)
        self.y = random.randint(0, 580)
        self.rect = pygame.Rect(self.x, self.y, 20, 20)
        
        
    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)