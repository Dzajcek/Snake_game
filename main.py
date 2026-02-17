import pygame
from snake import Snake
from apple import Apple
import random

class Game:
    def __init__(self):
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Snake 1.0")

        self.my_snake = Snake(self)
        self.apple = Apple(self)
        self.running = True
        self.apple.update()

    def update(self):
        eaten = False
        if self.my_snake.body[0].colliderect(self.apple.rect):
            self.apple.update()
            eaten = True

        self.my_snake.update(food_eaten=eaten)

        for i in range(1, len(self.my_snake.body)):
            if self.my_snake.body[0].colliderect(self.my_snake.body[i]):
                self.running = False

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and self.my_snake.direction_y != 20:
                    self.my_snake.direction_y = -20
                    self.my_snake.direction_x = 0

                if event.key == pygame.K_s and self.my_snake.direction_y != -20:
                    self.my_snake.direction_y = 20
                    self.my_snake.direction_x = 0

                if event.key == pygame.K_d and self.my_snake.direction_x != -20:
                    self.my_snake.direction_x = 20
                    self.my_snake.direction_y = 0

                if event.key == pygame.K_a and self.my_snake.direction_x != 20:
                    self.my_snake.direction_x = -20
                    self.my_snake.direction_y = 0
    def main(self):

        while self.running:
            if self.my_snake.body[0].left < 0 or self.my_snake.body[0].right > 800 or self.my_snake.body[0].top < 0 or self.my_snake.body[0].bottom > 600:
                self.running = False

            self.check_events()
            self.update()

            self.screen.fill((0, 0, 0))
            self.my_snake.draw()
            self.apple.draw()

            pygame.display.flip()
            self.clock.tick(15)
        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.main()