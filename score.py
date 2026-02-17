import pygame

class Score:
    def __init__(self, game):
        self.screen = game.screen
        self.points = 0

        self.label = pygame.Rect(20, 0, 100, 50)
        self.font = pygame.font.SysFont("Arial", 30)

    def draw(self):
        score_surface = pygame.Surface((self.label.width, self.label.height), pygame.SRCALPHA)

        background_color = (0, 0, 0, 0) 
        score_surface.fill(background_color)

        self.screen.blit(score_surface, (self.label.x, self.label.y))

        points_str = f"Score: {self.points}"
        text_surf = self.font.render(points_str, True, (255, 255, 255))
        
        text_rect = text_surf.get_rect(center=self.label.center)
        self.screen.blit(text_surf, text_rect)