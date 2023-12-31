import pygame
from pygame.locals import * 
from constantes import *

class hero:
	def __init__(self,right,left,up,down):
		#sprite du perso
		self.right = pygame.image.load(droite).convert_alpha()
		self.left = pygame.image.load(gauche).convert_alpha()
		self.up = pygame.image.load(haut).convert_alpha()
		self.down = pygame.image.load(bas).convert_alpha()
		
		#position
		self.x=0
		self.y=0
		self.direction = self.right
	
	def move(self,direction):
		#deplacement du perso
		if direction == 'right':