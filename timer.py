import pygame

"""
Timer object for timed game actions
"""
class Timer:

    """
    Initialize timer
    :param duration - duration of timer in milliseconds
    :param function - function to run when timer ends - default is None
    """
    def __init__(self, duration, function=None):
        self.duration = duration
        self.func = function
        self.start = 0
        self.active = False

    def activate(self):
        self.active = True
        self.start = pygame.time.get_ticks()

    def deactivate(self):
        self.active = False
        self.start = 0

    # check if timer over and deactivate if needed - call function if applicable
    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.start >= self.duration:
            self.deactivate()
            if self.func is not None:
                self.func()
