import pygame

class Snake:

    def __init__(self, game):
        self.screen = game.screen
        self.color = (0, 255, 0)
        self.body = [pygame.Rect(400, 300, 20, 20)]
        self.direction_x = 0
        self.direction_y = 0

    def update(self):
        new_head = self.body[0].copy()
        new_head.x += self.direction_x
        new_head.y += self.direction_y
        
        if self.direction_x != 0 or self.direction_y != 0:
            self.body.insert(0, new_head)
            self.body.pop()

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(self.screen, self.color, segment)
