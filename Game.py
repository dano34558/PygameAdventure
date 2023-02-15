import pygame
from Player import Player
from Army import Army
from Enemy import Enemy
from EventManager import EventManager
from Ui import UI
import pygame
import random
from Player import Player
from Enemy import Enemy
from EventManager import EventManager


class Game:
    def __init__(self):
        # initialize Pygame
        pygame.init()

        # set up window
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Pygame Adventure")

        # initialize game objects
        self.font = pygame.font.SysFont('Arial', 16)
        self.clock = pygame.time.Clock()
        self.player = Player('Player 1', 100, 10, 5)
        self.enemy = Enemy("stronk",Army(["hubert"]))
        self.event_manager = EventManager(self.player,self.enemy)
        self.ui = UI(self.screen, self.font, self.player, self.enemy, self.event_manager)

    def run(self):
        # main game loop
        while True:
            # handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.ui.run_event_button.rect.collidepoint(event.pos):
                        self.event_manager.run_random_event()

            # update game objects
            self.ui.update()

            # draw screen
            self.screen.fill((255, 255, 255))
            self.ui.draw()

            # update display
            pygame.display.flip()

            # tick clock
            self.clock.tick(60)
