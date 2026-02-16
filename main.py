import pygame
from snake import Snake
from apple import Apple

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Snake test")
running = True


class Game:
    def __init__(self, screen):
        self.screen = screen
        

game_instance = Game(screen)
my_snake = Snake(game_instance)
apple = Apple(game_instance)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and my_snake.direction_y != 20:
                my_snake.direction_y = -20
                my_snake.direction_x = 0

            if event.key == pygame.K_s and my_snake.direction_y != -20:
                my_snake.direction_y = 20
                my_snake.direction_x = 0

            if event.key == pygame.K_d and my_snake.direction_x != -20:
                my_snake.direction_x = 20
                my_snake.direction_y = 0

            if event.key == pygame.K_a and my_snake.direction_x != 20:
                my_snake.direction_x = -20
                my_snake.direction_y = 0
    
    if my_snake.body[0].left < 0 or my_snake.body[0].right > 800 or my_snake.body[0].top < 0 or my_snake.body[0].bottom > 600:
        running = False


    my_snake.update()

    screen.fill((0, 0, 0))
    my_snake.draw()
    apple.draw()

    pygame.display.flip()
    clock.tick(15)
    

pygame.quit()