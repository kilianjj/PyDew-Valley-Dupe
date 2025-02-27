import pygame
from player import Player
from settings import *

"""
A class for managing visual elements of the game
"""
class Level:

	"""
	Set display surface to screen
	Create the player object
	"""
	def __init__(self):
		# get the display surface
		self.display_surface = pygame.display.get_surface()
		# sprite groups
		self.all_sprites = pygame.sprite.Group()
		self.setup()

	def setup(self):
		self.player = Player((600, 600), self.all_sprites)

	def run(self, dt):
		self.display_surface.fill('black')
		self.all_sprites.draw(self.display_surface)		# draw game elements
		self.all_sprites.update(dt)			# updates all elements of game
