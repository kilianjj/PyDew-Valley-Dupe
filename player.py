import pygame
import support
from timer import Timer
import settings

"""
Class for the player object
"""
class Player(pygame.sprite.Sprite):

    """
    Initialize player object with position and sprite grouping
    Load animations
    Set default status, movement, selections, and timers
    """
    def __init__(self, pos, group):
        # setup
        super().__init__(group)
        self.animations = self.import_assets()
        self.import_assets()
        self.group = group
        self.status = "down_idle"
        self.frame_index = 0
        self.image = self.animations[self.status][self.frame_index]
        # image
        self.rect = self.image.get_rect(center=pos)
        # movement attributes
        self.direction = pygame.math.Vector2(0, 0)
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 200
        # item
        self.tools = ["axe", "hoe", "water"]
        self.tool_index = 0
        self.selected_tool = self.tools[self.tool_index]
        # timers
        self.timers = {
            "tool_use": Timer(350, self.use_tool),
            "tool_switching": Timer(200, None),
            "seed_use": Timer(200, self.use_seed),
            "seed_switching": Timer(200, None)
        }
        # seeds
        self.seeds = ["corn", "tomato"]
        self.seed_index = 0
        self.selected_seed = self.seeds[self.seed_index]

    # load in the animation assets and store in dictionary that is passed to self.animations
    @staticmethod
    def import_assets():
        animations = {'up': [], 'down': [], 'left': [], 'right': [], 'right_idle': [], 'left_idle': [],
                           'up_idle': [], 'down_idle': [], 'right_hoe': [], 'left_hoe': [], 'up_hoe': [],
                           'down_hoe': [], 'right_axe': [], 'left_axe': [], 'up_axe': [], 'down_axe': [],
                           'right_water': [], 'left_water': [], 'up_water': [], 'down_water': []}
        for animation in animations.keys():
            path = "graphics/character/" + animation
            animations[animation] = support.import_folder(path)
        return animations

    # switch the image of player based on current frame index
    def animate(self, dt):
        self.frame_index += 4 * dt
        if self.frame_index >= len(self.animations[self.status]):
            self.frame_index = 0
        self.image = self.animations[self.status][int(self.frame_index)]

    # process keyboard inputs and change player status, direction, etc
    def input(self):
        # prevent movement when using tool or seeds
        if not self.timers["tool_use"].active and not self.timers["seed_use"].active:
            # vertical movement
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                self.direction.y = -1
                self.status = "up"
            elif keys[pygame.K_DOWN]:
                self.direction.y = 1
                self.status = "down"
            else:
                self.direction.y = 0
            # horizontal movement
            if keys[pygame.K_LEFT]:
                self.direction.x = -1
                self.status = "left"
            elif keys[pygame.K_RIGHT]:
                self.direction.x = 1
                self.status = "right"
            else:
                self.direction.x = 0
            # using tools
            if keys[pygame.K_SPACE]:
                self.timers["tool_use"].activate()
                self.direction = pygame.math.Vector2()
                # start tool animation from 0
                self.frame_index = 0
            # changing tools
            if keys[pygame.K_q] and not self.timers["tool_switching"].active:
                self.tool_index = self.tool_index + 1 if self.tool_index + 1 < len(self.tools) else 0
                self.selected_tool = self.tools[self.tool_index]
                self.timers["tool_switching"].activate()
            # using seeds
            if keys[pygame.K_s]:
                self.timers["seed_use"].activate()
                self.direction = pygame.math.Vector2()
            # changing seeds
            if keys[pygame.K_a] and not self.timers["seed_switching"].active:
                self.seed_index = self.seed_index + 1 if self.seed_index + 1 < len(self.seeds) else 0
                self.selected_seed = self.seeds[self.seed_index]
                self.timers["seed_switching"].activate()

    # get the status of player
    def get_status(self):
        # idle states
        if self.direction.magnitude() == 0:
            self.status = self.status.split("_")[0] + "_idle"
        if self.timers["tool_use"].active:
            self.status = self.status.split("_")[0] + "_" + self.selected_tool

    def use_tool(self):
        pass

    def use_seed(self):
        pass

    # change position of player based on their direction
    def move(self, dt):
        # normalize direction vector to ensure uniform speeds
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        # horizontal movement
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.centerx = self.pos.x
        # vertical movement
        self.pos.y += self.direction.y * self.speed * dt
        self.rect.centery = self.pos.y

    # called constantly in update method - update all the seed/tool use/switching timers
    def update_timers(self):
        for timer in self.timers.values():
            timer.update()

    # update player: take inputs, get status, update timers, move, animate
    def update(self, dt):
        self.input()
        self.get_status()
        self.update_timers()
        self.move(dt)
        self.animate(dt)
