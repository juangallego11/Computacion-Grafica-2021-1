#LIBRERIAS UTILIZADAS
import pygame
import sys
from pygame.locals import *
import math
import numpy as np
from random import randint

#DECLARACION DE VARIABLES GLOBALES
ancho = 900
alto = 600
reloj = pygame.time.Clock()
listaEnemigo = []
Negro = [0,0,0]
Blanco = [255, 255, 255]

"""CLASE QUE IMPLEMENTA EL MENU DISEÑADO"""
class Menu():
	def menuInicial(self,venta):
		venta.fill(Negro)
		ImagenInicial = pygame.image.load('images/inicio.png')
		venta.blit(ImagenInicial, [0,0])
		pygame.display.update()
		reloj.tick(15)
		intro = True
		while intro:
			for evento in pygame.event.get():			
				if evento.type == QUIT:
					sys.exit()
				mouse=pygame.mouse.get_pos()
				x= mouse[0]
				y=mouse[1]
				if evento.type == pygame.MOUSEBUTTONDOWN:
					if(x >=407 and y>=407 and x<=577 and y<=450):
						SpaceInvader(venta)

"""CLASE PARA LOS OBJETOS: NAVES"""
class naveEspacial(pygame.sprite.Sprite):

	def __init__(self,ancho,alto):
		pygame.sprite.Sprite.__init__(self)

		self.ImagenNave = pygame.image.load('images/nave.png')
		self.ImagenExplosion = pygame.image.load("images/explosion.jpg")
		self.rect = self.ImagenNave.get_rect()
		self.rect.centerx = int(ancho/2)
		self.rect.centery = int(alto-30)

		self.listaDisparo = []
		self.Vida = True
		self.salud = 3

		self.velocidad = 20

		self.sonidoDisparo = pygame.mixer.Sound("sonidos/balas.ogg")
		self.sonidoExplosion = pygame.mixer.Sound("sonidos/bomba.wav")

	def movimientoDerecha(self): #FUNCION MOVIMIENTO DER
		self.rect.right += self.velocidad
		self.__movimiento()

	def movimientoIzquierda(self): #FUNCION MOVIMIENTO IZQ
		self.rect.left -= self.velocidad
		self.__movimiento()

	def __movimiento(self):
		if self.Vida == True:
			if self.rect.left <= 0:
				self.rect.left = 0
			elif self.rect.right>870:
				self.rect.right = 840

	def disparar(self, x, y):
		miProyectil = Proyectil(x,y,"images/disparoa.jpg", True)
		self.listaDisparo.append(miProyectil)
		self.sonidoDisparo.play()

	def destruccion(self):
		self.sonidoExplosion.play()
		self.Vida = False
		self.velocidad = 0
		self.ImagenNave = self.ImagenExplosion
	
	def dibujar(self, superficie):
		superficie.blit(self.ImagenNave, self.rect)

"""CLASE QUE CONTROLA LOS PROYECTILES DE LAS NAVES"""
class Proyectil(pygame.sprite.Sprite):
	def __init__(self, posx, posy, ruta, personaje):
		pygame.sprite.Sprite.__init__(self)

		self.imageProyectil = pygame.image.load(ruta) 

		self.rect = self.imageProyectil.get_rect()

		self.velocidadDisparoPersonaje = 4
		self.velocidadDisparoEnemigo = 2

		self.rect.top = posy
		self.rect.left = posx

		self.disparoPersonaje = personaje

	def  trayectoria(self):
		if self.disparoPersonaje == True:
			self.rect.top = self.rect.top - self.velocidadDisparoPersonaje
		else:
			self.rect.top = self.rect.top + self.velocidadDisparoEnemigo

	def dibujar(self, superficie):
		superficie.blit(self.imageProyectil, self.rect)

"""CLASE QUE CONTROLA LA ANIMACION DE LAS NAVES INVASORAS"""
class Invasor(pygame.sprite.Sprite):
	def __init__(self, posx, posy, distancia, imagenUno, imagenDos):
		pygame.sprite.Sprite.__init__(self)

		self.imagenA = pygame.image.load(imagenUno) 
		self.imagenB = pygame.image.load(imagenDos) 

		self.listaImagenes = [self.imagenA, self.imagenB]
		self.posImagen = 0

		self.imagenInvasor = self.listaImagenes[self.posImagen]
		self.rect = self.imagenInvasor.get_rect()

		self.listaDisparo = []
		self.velocidad = 1
		self.rect.top = posy
		self.rect.left = posx

		self.rangoDisparo = 1
		self.tiempoCambio = 1

		self.conquista = False

		self.derecha = True
		self.contador = 0
		self.Maxdescenso = self.rect.top + 40

		self.limiteDerecha = posx + distancia
		self.limiteIzquierda = posx - distancia


	def dibujar(self, superficie):
		self.imagenInvasor = self.listaImagenes[self.posImagen]
		superficie.blit(self.imagenInvasor, self.rect)

	def comportamiento(self, tiempo):
		if self.conquista == False:
			self.__movimientos()
			self.__ataque()
			if self.tiempoCambio == tiempo:
				self.posImagen += 1
				self.tiempoCambio += 1

				if self.posImagen > len(self.listaImagenes)-1:
					self.posImagen = 0

	def __movimientos(self): #MOVIMIENTO DE LOS INVASORES
		if self.contador < 3 : 
			self.__movimientoLateral()
		else:
			self.__descenso()

	def __descenso(self): # DESCENSO DE LOS INVASORES
		if self.Maxdescenso == self.rect.top:
			self.contador = 0
			self.Maxdescenso = self.rect.top + 40
		else:
			self.rect.top += 1

	def __movimientoLateral(self):
		if self.derecha == True:
			self.rect.left = self.rect.left + self.velocidad
			if self.rect.left > self.limiteDerecha:
				self.derecha = False
				self.contador += 1
		else:
			self.rect.left = self.rect.left - self.velocidad
			if self.rect.left < self.limiteIzquierda:
				self.derecha = True

	def __ataque(self): # ATAQUE DE LOS INVASORES
		if (randint(0,300) < self.rangoDisparo):
			self.__disparo()

	def __disparo(self): #PROYECTIL INVASOR
		x,y = self.rect.center
		miProyectil = Proyectil(x,y,"images/disparob.jpg", False)
		self.listaDisparo.append(miProyectil)

def detenerTodo():
	for enemigo in listaEnemigo:
		for disparo in enemigo.listaDisparo:
			enemigo.listaDisparo.remove(disparo)
		listaEnemigo.remove(enemigo)

def cargarEnemigos():
	posx = 100
	for x in range(1,5):
		enemigo = Invasor(posx,100,40,'images/marcianoA.jpg', 'images/marcianoB.jpg') # CARGA UN ENEMIGO DIF CON EL METODO APPEND
		listaEnemigo.append(enemigo)
		posx = posx + 200

	posx = 100
	for x in range(1,5):
		enemigo = Invasor(posx,0,40,'images/Marciano2A.jpg', 'images/Marciano2B.jpg') # CARGA UN ENEMIGO DIF CON EL METODO APPEND
		listaEnemigo.append(enemigo)
		posx = posx + 200

	posx = 100
	for x in range(1,5):
		enemigo = Invasor(posx,-100,40,'images/Marciano3A.jpg', 'images/Marciano3B.jpg') # CARGA UN ENEMIGO DIF CON EL METODO APPEND
		listaEnemigo.append(enemigo)
		posx = posx + 200

"""CLASE GAME OVER, SE ACTIVA CON LA PERDIDA DE LAS 3 VIDAS"""
class gameOver():
	def cargarGameOver(self, venta):
		venta.fill(Negro)
		game_over = pygame.image.load('images/game_over.png')#CARGA LA IMAGEN DE PERDIDA
		venta.blit(game_over, [-15,0])
		pygame.display.flip()
		intro = True
		while intro:
			for evento in pygame.event.get():			
				if evento.type == QUIT:
					sys.exit()
				mouse=pygame.mouse.get_pos()
				x= mouse[0]
				y=mouse[1]
				if evento.type == pygame.MOUSEBUTTONDOWN:
					if(x >=365 and y>=301 and x<=564 and y<=347):
						detenerTodo()
						SpaceInvader(venta)
					if(x >=369 and y>=365 and x<=563 and y<=419):
						creditos = Creditos()
						creditos.mostrarCreditos(venta)
					if(x >=384 and y>=436 and x<=546 and y<=473):
						sys.exit()
						
"""CREDITOS DE AUTOR"""
class Creditos():
	def mostrarCreditos(self, venta):
		creditos = pygame.image.load('images/creditos.png')
		venta.blit(creditos,[0,0])
		pygame.display.flip()
		credit = True;
		while credit:
			for evento in pygame.event.get():			
				if evento.type == QUIT:
					sys.exit()
				mouse=pygame.mouse.get_pos()
				x= mouse[0]
				y=mouse[1]
				if evento.type == pygame.MOUSEBUTTONDOWN:
					if(x >= 717 and y>=18 and x<=827 and y<=57):
						game_over = gameOver()
						game_over.cargarGameOver(venta)

"""CLASE GANADOR, DETIENE O REINICIA EL JUEGO"""
class Ganador():
	def mostrarGanador(self,venta):
		venta.fill(Negro)
		game_over = pygame.image.load('images/ganador.png').convert_alpha()
		venta.blit(game_over, [0,20])
		pygame.display.flip()
		ganador = True
		while ganador:
			for evento in pygame.event.get():			
				if evento.type == QUIT:
					sys.exit()
				mouse=pygame.mouse.get_pos()
				x= mouse[0]
				y=mouse[1]
				if evento.type == pygame.MOUSEBUTTONDOWN:
					if(x >= 380 and y>=400 and x<=511 and y<=436):
						detenerTodo()
						SpaceInvader(venta)
					if(x >= 417 and y>=461 and x<=476 and y<=488):
						sys.exit()


def SpaceInvader(venta):
	pygame.init()
	pygame.display.set_caption("Space Invaders UTP")
	gameover = gameOver()
	ImagenFondo = pygame.image.load('images/Fondo.jpg') #FONDO NEGRO

	#CARGA LAS VIDAS
	vida1 = pygame.image.load('images/vida.png')
	vida2 = pygame.image.load('images/vida.png')
	vida3 = pygame.image.load('images/vida.png')

	pygame.mixer.music.load('sonidos/intro.mp3') # FUNCION PARA REPRODUCIR EL SONIDO DEL INTRO
	pygame.mixer.music.play(3)
	puntaje = 0
	Fuente=pygame.font.Font(None,34)
	pygame.display.flip()
	reloj.tick(0.8)
	enJuego = True
	jugador = naveEspacial(ancho,alto)
	detenerTodo()
	cargarEnemigos()
	
	while enJuego:
		reloj.tick(300)
		t_puntaje = 'Score: {0000}'.format(puntaje)
		txt_puntaje = Fuente.render(t_puntaje, True, Blanco)
		tiempo = int (pygame.time.get_ticks()/1000)

		for evento in pygame.event.get():
			if evento.type == QUIT:
				pygame.quit()

			if enJuego == True:
				if evento.type == pygame.KEYDOWN:
					if evento.key == K_LEFT:
						jugador.movimientoIzquierda() #LEE LA TECLA IZQ

					elif evento.key == K_RIGHT:
						jugador.movimientoDerecha() #LEE LA TECLA DER

					elif evento.key == K_s:
						x,y = jugador.rect.center
						jugador.disparar(x,y) #LEE LA TECLA PARA DISPARAR

		venta.blit(ImagenFondo, (0,0))
		jugador.dibujar(venta)		
		

		if len(jugador.listaDisparo)>0:
			for x in jugador.listaDisparo:
				x.dibujar(venta)
				x.trayectoria()

				if x.rect.top < -10:
					jugador.listaDisparo.remove(x)
				else:
					for enemigo in listaEnemigo:
						if x.rect.colliderect(enemigo.rect):
							listaEnemigo.remove(enemigo)
							jugador.listaDisparo.remove(x)
							puntaje+=40


		if len(listaEnemigo) > 0:
			for enemigo in listaEnemigo:
				enemigo.comportamiento(tiempo)
				enemigo.dibujar(venta)

				if enemigo.rect.colliderect(jugador.rect):
					gameover.cargarGameOver(venta)
					detenerTodo()

				if len(enemigo.listaDisparo)>0:
					for x in enemigo.listaDisparo:
						x.dibujar(venta)
						x.trayectoria()

						if x.rect.colliderect(jugador.rect):
							enemigo.listaDisparo.remove(x)
							jugador.salud -=1
							
							
						if x.rect.top > 900:
							enemigo.listaDisparo.remove(x)
						else:
							for disparo in jugador.listaDisparo:
								if x.rect.colliderect(disparo.rect):
									jugador.listaDisparo.remove(disparo)
									enemigo.listaDisparo.remove(x)
									puntaje+=40
		if len(listaEnemigo) == 0:
			ganador = Ganador()
			ganador.mostrarGanador(venta)
			enJuego = False

		if(jugador.salud == 3):
			venta.blit(vida1, (780,570))
			venta.blit(vida2, (820,570))
			venta.blit(vida3, (860,570))
		if(jugador.salud == 2):
			venta.blit(vida1, (820,570))
			venta.blit(vida2, (860,570))
		if(jugador.salud ==1):
			venta.blit(vida1, (860,570))
		if(jugador.salud == 0):
			gameover.cargarGameOver(venta)
			detenerTodo()

			
		venta.blit(txt_puntaje, [10,578])
		pygame.display.update()



if __name__ == '__main__':
	venta = pygame.display.set_mode((ancho,alto))
	menu = Menu()
	menu.menuInicial(venta)
