import pygame
from pygame.locals import *

pygame.init()
fenetre = pygame.display.set_mode((640, 480))

# chargement et collage des images
background= pygame.image.load("background.jpg").convert()
fenetre.blit(background,(0,0))

perso = pygame.image.load("perso.png").convert_alpha()
position_perso = perso.get_rect()
fenetre.blit(perso, position_perso)

pygame.display.flip()

# tant que continuer = 1 , boucle infinie
continuer=1
pygame.key.set_repeat(400, 30)
while continuer:
	for event in pygame.event.get():   
		if event.type == QUIT:     
			continuer = 0 
		if event.type == KEYDOWN:
			if event.key == K_DOWN:	
				position_perso = position_perso.move(0,3)
		if event.type == KEYDOWN:
			if event.key == K_UP:	
				position_perso = position_perso.move(0,-3)
		if event.type == KEYDOWN:
			if event.key == K_RIGHT:	
				position_perso = position_perso.move(3,0)
		if event.type == KEYDOWN:
			if event.key == K_LEFT:	
				position_perso = position_perso.move(-3,0)
	#Re-collage
	fenetre.blit(background, (0,0))	
	fenetre.blit(perso, position_perso)
	#Rafraichissement
	pygame.display.flip()