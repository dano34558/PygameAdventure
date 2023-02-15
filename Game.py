import pygame
from Player import Player
from Army import Army
from Enemy import Enemy
from EventManager import EventManager

class Game:
    def __init__(self):
        self.width = 640
        self.height = 480
        self.fps = 60
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.player = Player("Player 1",(0,0))
        self.enemy = Enemy("Enemy", Army(""))
        self.event_manager = EventManager(self.player, self.enemy)
        self.font = pygame.font.SysFont('Arial', 16)
        self.run_event_button = pygame.Rect(20, 400, 200, 50)
        self.done = False
    
    def run(self):
        while not self.done:
            self._handle_events()
            self._update()
            self._draw()
            pygame.display.flip()
            self.clock.tick(self.fps)

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if self.run_event_button.collidepoint(pos):
                    self.event_manager.run_event()

    def _update(self):
        pass

    def _draw(self):
        self.screen.fill((255, 255, 255))

        # Draw player stats
        text = self.font.render(f"Player: {self.player.name}", True, (0, 0, 0))
        self.screen.blit(text, (20, 20))
        text = self.font.render(f"Gold: {self.player.gold}", True, (0, 0, 0))
        self.screen.blit(text, (20, 40))
        text = self.font.render(f"Experience: {self.player.experience}", True, (0, 0, 0))
        self.screen.blit(text, (20, 60))

        # Draw army stats
        text = self.font.render("Army", True, (0, 0, 0))
        self.screen.blit(text, (20, 100))
        y = 120
        for soldier in self.player.army:
            text = self.font.render(f"{soldier.name} ({soldier.type}), Level {soldier.level}, Health {soldier.health}/{soldier.max_health}", True, (0, 0, 0))
            self.screen.blit(text, (20, y))
            y += 20

        # Draw run event button
        pygame.draw.rect(self.screen, (0, 255, 0), self.run_event_button)
        text = self.font.render("Run Event", True, (0, 0, 0))
        self.screen.blit(text, (30, 415))

    def _quit(self):
        pygame.quit()

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Adventure Game")
    game = Game()
    game.run()
    game._quit()
