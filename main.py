import pygame
import sys
from settings import *
from level import Level

"""
Initialize the game object with screen measurements and clock
Create the level object that manages visual objects
"""
class Game:
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
		pygame.display.set_caption('Stardupe Valley')
		self.clock = pygame.time.Clock()
		self.level = Level()

	def run(self):
		# loop while true until game is closed
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
			dt = self.clock.tick() / 1000		# seconds between frames
			self.level.run(dt)
			pygame.display.update()

if __name__ == '__main__':
	game = Game()
	game.run()
