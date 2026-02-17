import pygame
from snake import Snake
from apple import Apple
from score import Score

class Game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Snake 1.0")

        self.my_snake = Snake(self)
        self.apple = Apple(self)
        self.score = Score(self)
        self.running = True
        self.apple.update()

        self.font = pygame.font.SysFont("Arial", 30)
        self.state = "MENU"

    def update(self):
        eaten = False
        if self.my_snake.body[0].colliderect(self.apple.rect):
            self.apple.update()
            self.score.points += 1
            eaten = True

        self.my_snake.update(food_eaten=eaten)

        for i in range(1, len(self.my_snake.body)):
            if self.my_snake.body[0].colliderect(self.my_snake.body[i]):
                self.running = False

    def check_game_events(self):
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

    def check_menu_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if self.start_button.collidepoint(mouse_pos):
                    self.reset_game()
                    self.state = "GAME"
                elif self.quit_button.collidepoint(mouse_pos):
                    pygame.quit()
                    exit()

    def reset_game(self):
        self.score.points = 0
        self.my_snake = Snake(self)
        self.apple.update()
        self.running = True

    def draw_button(self, text, rect, color):
        pygame.draw.rect(self.screen, color, rect)
        
        text_surf = self.font.render(text, True, (255, 255, 255))
        
        text_rect = text_surf.get_rect(center=rect.center)
        self.screen.blit(text_surf, text_rect)


    def main(self):
        self.start_button = pygame.Rect(300, 200, 200, 50)
        self.quit_button = pygame.Rect(300, 300, 200, 50)

        while True:
            if self.state == "MENU":
                self.check_menu_events()
                self.screen.fill((0, 0, 0))
                self.score.draw()
                
                self.draw_button("START", self.start_button, (0, 255, 0))
                self.draw_button("QUIT", self.quit_button, (255, 0, 0))
                
                pygame.display.flip()

            elif self.state == "GAME":
                    if not self.running:
                        self.state = "MENU"
                        continue

                    if self.my_snake.body[0].left < 0 or self.my_snake.body[0].right > 800 or \
                        self.my_snake.body[0].top < 0 or self.my_snake.body[0].bottom > 600:
                            self.running = False

                    self.check_game_events()
                    self.update()

                    self.screen.fill((0, 0, 0))
                    self.my_snake.draw()
                    self.apple.draw()
                    self.score.draw()

                    pygame.display.flip()
                    self.clock.tick(15)

if __name__ == "__main__":
    game = Game()
    game.main()