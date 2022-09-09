import pygame, random
from pygame.locals import *

pygame.init()
window = pygame.display.set_mode((600,350))

KeyDown = False
PlayerY = 155
Walls = [[600, random.randint(0, 10),random.randint(0, 10)]]
SCORE = 0
GAME_OVER = False

while True:
	window.fill(pygame.Color(0,0,0))
	for Event in pygame.event.get():
		if Event.type == 256:
				quit()
		if Event.type == pygame.KEYDOWN:
			if Event.key == K_SPACE:
				if not GAME_OVER:
					PlayerY -= 50
				else:
					PlayerY = 155
					Walls = [[600, random.randint(0, 10),random.randint(0, 10)]]
					SCORE = 0
					GAME_OVER = False

	if GAME_OVER:
		window.blit(pygame.font.SysFont('Arial', 40).render("GAME OVER", True, (255,0,0)), (160, 60))
		window.blit(pygame.font.SysFont('Arial', 50).render(str(SCORE), True, (255,255,255)), ((300-(len(str(SCORE))*50)/2), 140))
		window.blit(pygame.font.SysFont('Arial', 15).render("Replay : SPACE", True, (255,255,255)), (10, 320))
	else:
		pygame.draw.rect(window, pygame.Color(200,0,200), [100, PlayerY, 20, 20])
		PlayerY += 2

		if Walls[len(Walls)-1][0] == 450:
			Walls += [[600, random.randint(0, 10),random.randint(0, 10)]]
		if Walls[0][0] == -60:
			Walls.remove(Walls[0])
		for posX in range(len(Walls)):
			posY = [(Walls[posX][1]*10)+20, (Walls[posX][2]*10)+20]
			if Walls[posX][0] == 120: SCORE += 1
			if Walls[posX][0] <= 120 and Walls[posX][0]+60 >= 100:
				if PlayerY <= posY[0] or PlayerY+20 >= 350-posY[1]:
					GAME_OVER = True
			window.blit(pygame.font.SysFont('Arial', 15).render(str(SCORE), True, (255,255,255)), (10, 165))
			pygame.draw.rect(window, pygame.Color(100,200,250), [Walls[posX][0], 0, 60, posY[0]])
			pygame.draw.rect(window, pygame.Color(100,200,250), [Walls[posX][0], 350-posY[1], 60, posY[1]])
			Walls[posX][0] -= 5

	pygame.time.wait(10)
	pygame.display.update()