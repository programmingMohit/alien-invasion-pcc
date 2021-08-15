#Program containing a class for inital values of settings of the game

class Settings:
	"""A class to store all setting for the game Alien Invasion"""

	def __init__(self):
		"""Initializing the settings of the game"""
		# Screen settings
		self.screen_width = 1200
		self.screen_height = 700
		self.bg_color = (230,230,230)

		# Ship settings
		self.ship_speed = 1.5

		#Bullet settings
		self.bullet_speed = 1.0
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)