import pygame

class UI:
    def __init__(self, screen):
        self.screen = screen

        # Load fonts
        self.font = pygame.font.SysFont("Arial", 16)
        
        # Set up player info column
        self.player_info_rect = pygame.Rect(0, 0, 200, self.screen.get_height())
        self.player_info_surface = pygame.Surface((self.player_info_rect.width, self.player_info_rect.height))
        self.player_info_surface.fill((255, 255, 255))
        
        # Set up buttons
        self.inventory_button_rect = pygame.Rect(0, 50, 200, 50)
        self.stats_button_rect = pygame.Rect(0, 100, 200, 50)
        self.army_button_rect = pygame.Rect(0, 150, 200, 50)

    def draw(self):
        # Draw player info column
        self.screen.blit(self.player_info_surface, self.player_info_rect)

        # Draw buttons
        pygame.draw.rect(self.player_info_surface, (0, 0, 255), self.inventory_button_rect)
        pygame.draw.rect(self.player_info_surface, (0, 0, 255), self.stats_button_rect)
        pygame.draw.rect(self.player_info_surface, (0, 0, 255), self.army_button_rect)

        # Draw button text
        inventory_text = self.font.render("Inventory", True, (255, 255, 255))
        stats_text = self.font.render("Stats", True, (255, 255, 255))
        army_text = self.font.render("Army", True, (255, 255, 255))
        self.player_info_surface.blit(inventory_text, self.inventory_button_rect)
        self.player_info_surface.blit(stats_text, self.stats_button_rect)
        self.player_info_surface.blit(army_text, self.army_button_rect)