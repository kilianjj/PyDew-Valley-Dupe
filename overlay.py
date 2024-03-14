import pygame
import settings

class Overlay:

    def __init__(self, player):
        # setup
        self.display_surface = pygame.display.get_surface()
        self.player = player
        # seed and tool images
        overlay_path = "graphics/overlay/"
        self.tool_surfs = {tool: pygame.image.load(f"{overlay_path}{tool}.png").convert_alpha()
                           for tool in player.tools}
        self.seed_surfs = {seed: pygame.image.load(f"{overlay_path}{seed}.png").convert_alpha()
                           for seed in player.seeds}

    def display(self):
        tool_surf = self.tool_surfs[self.player.selected_tool]
        tool_rect = tool_surf.get_rect(midbottom=settings.OVERLAY_POSITIONS["tool"])
        seed_surf = self.seed_surfs[self.player.selected_seed]
        seed_rect = seed_surf.get_rect(midbottom=settings.OVERLAY_POSITIONS["seed"])
        self.display_surface.blit(tool_surf, tool_rect)
        self.display_surface.blit(seed_surf, seed_rect)
