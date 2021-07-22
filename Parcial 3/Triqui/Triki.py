import pygame
import time
import math
import sys
import numpy as np

windows=pygame
AZUL=(0,0,255)
ROJO=(255,0,0)
AMARILLO=(255,255,0)
BLANCO=(255,255,255)
NEGRO=(0,0,0)
pygame.init()
pantalla = pygame.display.set_mode ((820,561))
tablero = np.zeros((3, 3))
Fuente=pygame.font.Font(None,34)
gano1=Fuente.render("Ganador: Jugador X",False,NEGRO)
gano2=Fuente.render("Ganador: Jugador O",False,NEGRO)
empate=Fuente.render("Empate",False,NEGRO)

def inicio (): #MUESTRA IMAGEN DE BIENVENDIA
    presentacion = pygame.image.load("C:/Users/fbdav/Desktop/triki/Images/Bienvenidos.png")
    pantalla.blit(presentacion,(0,0))
    pygame.display.update()
    time.sleep(1)

def menu(): #MUESTRA EL MENU
    menu = pygame.image.load("C:/Users/fbdav/Desktop/triki/Images/Menu.png")
    pantalla.blit(menu,(0,0))
    pygame.display.update()
    running = True
    while running:
        for eventos in pygame.event.get():
            if eventos.type == pygame.QUIT:
                exit()
            if eventos.type == pygame.MOUSEBUTTONDOWN:
                x, y = eventos.pos        
                if (x >=209 and y >=202 and x <= 735 and y <=273):
                    jugar("o")
                if (x >=211 and y >=304 and x <= 726 and y <=387):
                    creditos()
                if (x >=219 and y >=411 and x <= 737 and y <=491):
                    sys.exit()
        pantalla.blit(menu,(0,0))
        pygame.display.update()

def creditos(): #MUESTRA LOS CREDITOS DEL AUTOR
    creditos = pygame.image.load("C:/Users/fbdav/Desktop/triki/Images/creditos.png")
    pantalla.blit(creditos,(0,0))
    pygame.display.update()
    running = True
    while running:
        for eventos in pygame.event.get():
            if eventos.type == pygame.QUIT:
                exit()
            if eventos.type == pygame.MOUSEBUTTONDOWN:
                x, y = eventos.pos
                if (x >=645 and y >=477 and x <= 779 and y <=504):
                    menu()

def jugar(turno): #FUNCION QUE CONTROLA LOS TURNOS
    juego = pygame.image.load("C:/Users/fbdav/Desktop/triki/Images/Juego.png")
    pantalla.blit(juego,(0,0))
    pygame.display.update()
    while True:
        for eventos in pygame.event.get():
            if eventos.type == pygame.QUIT:
                exit()
            if eventos.type == pygame.MOUSEBUTTONDOWN:
                x, y = eventos.pos
                #FILA 1
                if (x >=232 and y >=56 and x <= 416 and y <=208):
                    print ("Jugo ",turno, " en (0,0)")
                    if (turno == "x"):
                        juega_turno = pygame.image.load("C:/Users/fbdav/Desktop/triki/Images/x.png")
                        tablero[0][0] = 1
                        validarJugada()
                        turno="o"
                    else:
                        juega_turno = pygame.image.load("C:/Users/fbdav/Desktop/triki/Images/o.png")
                        tablero[0][0] = 4
                        validarJugada()
                        turno="x"
                    pantalla.blit(juega_turno,(280,90))
                    pygame.display.update()    
                if (x >=424 and y >=56 and x <= 580 and y <=208):
                    print ("Jugo ",turno, " en (0,1)")
                    if (turno == "x"):
                        juega_turno = pygame.image.load("C:/Users/fbdav/Desktop/triki/Images/x.png")
                        tablero[0][1] = 1
                        validarJugada()
                        turno="o"
                    else:
                        juega_turno = pygame.image.load("C:/Users/fbdav/Desktop/triki/Images/o.png")
                        tablero[0][1] = 4
                        validarJugada()
                        turno="x"
                    pantalla.blit(juega_turno,(450,90))
                    pygame.display.update()
                if (x >=589 and y >=56 and x <= 754 and y <=208):
                    print ("Jugo ",turno, " en (0,2)")
                    if (turno == "x"):
                        juega_turno = pygame.image.load("C:/Users/fbdav/Desktop/triki/Images/x.png")
                        tablero[0][2] = 1
                        validarJugada()
                        turno="o"
                    else:
                        juega_turno = pygame.image.load("C:/Users/fbdav/Desktop/triki/Images/o.png")
                        tablero[0][2] = 4
                        validarJugada()
                        turno="x"
                    pantalla.blit(juega_turno,(620,87))
                    pygame.display.update()
                #FILA2 
                if (x >=232 and y >=220 and x <= 416 and y <=358):
                    print ("Jugo ",turno, " en (1,0)")
                    if (turno == "x"):
                        juega_turno = pygame.image.load("C:/Users/fbdav/Desktop/triki/Images/x.png")
                        tablero[1][0] = 1
                        validarJugada()
                        turno="o"
                    else:
                        juega_turno = pygame.image.load("C:/Users/fbdav/Desktop/triki/Images/o.png")
                        tablero[1][0] = 4
                        validarJugada()
                        turno="x"
                    pantalla.blit(juega_turno,(280,235))
                    pygame.display.update()
                if (x >=424 and y >=219 and x <= 580 and y <=359):
                    print ("Jugo ",turno, " en (1,1)")
                    if (turno == "x"):
                        juega_turno = pygame.image.load("C:/Users/fbdav/Desktop/triki/Images/x.png")
                        tablero[1][1] = 1
                        validarJugada()
                        turno="o"
                    else:
                        juega_turno = pygame.image.load("C:/Users/fbdav/Desktop/triki/Images/o.png")
                        tablero[1][1] = 4
                        validarJugada()
                        turno="x"
                    pantalla.blit(juega_turno,(450,235))
                    pygame.display.update()
                if (x >=589 and y >=219 and x <= 754 and y <=359):
                    print ("Jugo ",turno, " en (1,2)")
                    if (turno == "x"):
                        juega_turno = pygame.image.load("C:/Users/fbdav/Desktop/triki/Images/x.png")
                        tablero[1][2] = 1
                        validarJugada()
                        turno="o"
                    else:
                        juega_turno = pygame.image.load("C:/Users/fbdav/Desktop/triki/Images/o.png")
                        tablero[1][2] = 4
                        validarJugada()
                        turno="x"
                    pantalla.blit(juega_turno,(620,235))
                    pygame.display.update()
                #FILA 3
                if (x >=232 and y >=368 and x <= 416 and y <=517):
                    print ("Jugo ",turno, " en (2,0)")
                    if (turno == "x"):
                        juega_turno = pygame.image.load("C:/Users/fbdav/Desktop/triki/Images/x.png")
                        tablero[2][0] = 1
                        validarJugada()
                        turno="o"
                    else:
                        juega_turno = pygame.image.load("C:/Users/fbdav/Desktop/triki/Images/o.png")
                        tablero[2][0] = 4
                        validarJugada()
                        turno="x"
                    pantalla.blit(juega_turno,(280,385))
                    pygame.display.update()
                if (x >=424 and y >=368 and x <= 578 and y <=515):
                    print ("Jugo ",turno, " en (2,1)")
                    if (turno == "x"):
                        juega_turno = pygame.image.load("C:/Users/fbdav/Desktop/triki/Images/x.png")
                        tablero[2][1] = 1
                        validarJugada()
                        turno="o"
                    else:
                        juega_turno = pygame.image.load("C:/Users/fbdav/Desktop/triki/Images/o.png")
                        tablero[2][1] = 4
                        validarJugada()
                        turno="x"
                    pantalla.blit(juega_turno,(450,385))
                    pygame.display.update()
                if (x >=589 and y >=369 and x <= 754 and y <=518):
                    print ("Jugo ",turno, " en (2,2)")
                    if (turno == "x"):
                        juega_turno = pygame.image.load("C:/Users/fbdav/Desktop/triki/Images/x.png")
                        tablero[2][2] = 1
                        validarJugada()
                        turno="o"
                    else:
                        juega_turno = pygame.image.load("C:/Users/fbdav/Desktop/triki/Images/o.png")
                        tablero[2][2] = 4
                        validarJugada()
                        turno="x"
                    pantalla.blit(juega_turno,(620,385))
                    pygame.display.update()
                if (x >=45 and y >=447 and x <= 169 and y <=493):
                    limpiarMatriz()
                    jugar("o")
                                         
    pygame.display.update()
    time.sleep(10)

def limpiarMatriz(): #FUNCION QUE LIMPIA LA MATRIZ Y VUELVE A INCIAR EL JUEGO
    for i in range(3):
        for j in range(3):
            tablero[i][j] = 0
        
def validarJugada():
    if((tablero[0][0] + tablero[0][1] + tablero[0][2]) == 3):
        pantalla.blit(gano1,[4,250])
        limpiarMatriz()
    if((tablero[0][0] + tablero[0][1] + tablero[0][2]) == 12):
        pantalla.blit(gano2,[4,250])
        limpiarMatriz()

    if((tablero[0][0] + tablero[1][0] + tablero[2][0]) == 3):
        pantalla.blit(gano1, [4, 250])
        limpiarMatriz()
    if((tablero[0][0] + tablero[1][0] + tablero[2][0]) == 12):
        pantalla.blit(gano2, [4, 250])
        limpiarMatriz()
    
    if((tablero[0][0] + tablero[1][1] + tablero[2][2]) == 3):
        pantalla.blit(gano1, [4, 250])
        limpiarMatriz()
    if((tablero[0][0] + tablero[1][1] + tablero[2][2]) == 12):
        pantalla.blit(gano2, [4, 250])
        limpiarMatriz()
    
    if((tablero[0][1] + tablero[1][1] + tablero[2][1]) == 3):
        pantalla.blit(gano1, [4, 250])
        limpiarMatriz()
    if((tablero[0][1] + tablero[1][1] + tablero[2][1]) == 12):
        pantalla.blit(gano2, [4, 250])
        limpiarMatriz()
    
    if((tablero[1][0] + tablero[1][1] + tablero[1][2]) == 3):
        pantalla.blit(gano1, [4, 250])
        limpiarMatriz()
    if((tablero[1][0] + tablero[1][1] + tablero[1][2]) == 12):
        pantalla.blit(gano2, [4, 250])
        limpiarMatriz()
    
    if((tablero[0][2] + tablero[1][2] + tablero[2][2]) == 3):
        pantalla.blit(gano1, [4, 250])
        limpiarMatriz()
    if((tablero[0][2] + tablero[1][2] + tablero[2][2]) == 12):
        pantalla.blit(gano2, [4, 250])
        limpiarMatriz()
        
    if((tablero[2][0] + tablero[2][1] + tablero[2][2]) == 3):
        pantalla.blit(gano1, [4, 250])
        limpiarMatriz()
    if((tablero[2][0] + tablero[2][1] + tablero[2][2]) == 12):
        pantalla.blit(gano2, [4, 250])
        limpiarMatriz()
 
    if((tablero[2][0] + tablero[1][1] + tablero[0][2]) == 3):
        pantalla.blit(gano1, [4, 250])
        limpiarMatriz()
    if((tablero[2][0] + tablero[1][1] + tablero[0][2]) == 12):
        pantalla.blit(gano2, [4, 250])
        limpiarMatriz()

                  

def main():
    inicio()
    menu()

main()
