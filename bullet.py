 
 import pygame
 from pygame.sprite import Sprite

 class Bullet(Sprite):
 	"""Overall class to manage bullets fired from ship"""

 	def __init__(self, ai_game):
 		"""Create a bullet object at the ship's current position"""
 		super.__init__()
 		self.screen = self.ai_game.screen
 		self.settings = self.ai_game.settings
 		self.color = self.settings.bullet_color

 		# Create a bullet at (0,0) and then set it's correct position
 		self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
 		 self.settings.bullet_height)
 		self.rect.midtop = ai_game.ship.rect.midtop

 		# Store the bullet's position as decimal value
 		self.y = float(self.rect.y)

 	def upadte(self):
 		"""Move the bullet up the sceen"""
 		#Update the decimal position of the bullet
 		self.y -= self.settings.bullet_speed
 		#Update the rect position
 		self.rect.y = self.y

 	def draw_bullet(self):
 		"""Draw the bullet to the screen"""
 		pygame.draw.rect(self.screen, self.color, self.rect)