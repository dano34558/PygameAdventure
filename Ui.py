import pygame

class UI:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.font = pygame.font.SysFont("Arial", 20)

    def draw_text(self, text, x, y, color=(255, 255, 255)):
        text_surface = self.font.render(text, True, color)
        self.screen.blit(text_surface, (x, y))

    def draw_button(self, text, x, y, width, height, color=(255, 255, 255)):
        pygame.draw.rect(self.screen, color, (x, y, width, height))
        self.draw_text(text, x + 10, y + 10)

    def update(self):
        pygame.display.update()

    def clear(self):
        self.screen.fill((0, 0, 0))

    def get_events(self):
        return pygame.event.get()