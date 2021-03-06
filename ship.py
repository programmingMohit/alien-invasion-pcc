"""Module containing the ship class"""

import pygame

class Ship():
	"""A class to manage the ship."""

	def __init__(self,ai_game):
		"""Initialize the ship and it's starting position"""

		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_rect = ai_game.screen.get_rect()
		# Movement flags
		self.moving_right = False
		self.moving_left = False

		# Load the ship image and get it's rect

		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()

		# Starts each new ship at the bottom of the screen

		self.rect.midbottom = self.screen_rect.midbottom


		# Store a decimal value for ship's horizontal  position
		self.x = float(self.rect.x)

	def blitme(self):
		"""Draw the ship at it's current location."""
		self.screen.blit(self.image,self.rect)

	def update(self):
		"""Updates the ship's position based on the movement flag"""
		# Update the ship's x value not the rect
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.settings.ship_speed
		if self.moving_left and self.rect.left > 0:
			self.x -= self.settings.ship_speed

		# Update rect object from self.x
		self.rect.x = self.x