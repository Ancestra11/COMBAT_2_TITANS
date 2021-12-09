import pygame
from pygame.locals import *

class Commands :

	def __init__(self, pg) :

		#pygame.sprite.Sprite.__init__(self)
		self.pg = pg
		self.x_Img_NoRay = 120
		self.y_Img_NoRay = 410

		self.pg.display.update()
		self.pg.key.set_repeat(2, 50) # ( Délai avant de continuer mouvement, temps entre chaque déplacement)

	def Jumping(self) :

		pass

	def Moving(self) :
		
		running = True
		while running == True :

			self.pg.key.set_repeat(2, 50) # ( Délai avant de continuer mouvement, temps entre chaque déplacement)

			for event in self.pg.event.get() :

				if event.type == KEYDOWN and event.key == K_RIGHT and self.x_Img_NoRay + 10 < 1210 :
					self.x_Img_NoRay = self.x_Img_NoRay + 10

				if event.type == KEYDOWN and event.key == K_LEFT and self.x_Img_NoRay - 10 > -15 :
					self.x_Img_NoRay = self.x_Img_NoRay - 10

				if event.type == KEYDOWN and event.key == KEYUP and self.y_Img_NoRay - 10 > 30 :
					self.y_Img_NoRay = self.y_Img_NoRay - 10

				if event.type == pg.QUIT :
					running = False

				pg.display.update()

		pg.quit()

	def Hitting(self) :

		pass