#JUAN DAVID GALLEGO RANGEL 1112627876


import math
import numpy as np
#import matplotlib.pyplot as plt
import pygame
import time
from librerias import *
windows=pygame


bgcolor= 255,255,255
gris=np.array([155,155,155])
blanco= 255,255,255
verde=np.array([0,255,0])
naranja=np.array([239,127,26])
amarillo=np.array([255,255,0])
rojo=np.array([255,0,0])
verde=np.array([0,255,0])
azul=np.array([0,0,255])
blanco=np.array([255,255,255])
linecolor = 0,0,0
screen = pygame.display.set_mode((700,560))


screen.fill(bgcolor)

draw_line_bres(screen,linecolor,[20,20],[680,20])
draw_line_bres(screen,linecolor,[20,540],[680,540])
draw_line_bres(screen,linecolor,[20,20],[20,540])
draw_line_bres(screen,linecolor,[680,20],[680,540])
draw_line_bres(screen,linecolor,[120,20],[120,540])
draw_line_bres(screen,linecolor,[580,20],[580,540])

#cuadro 1
draw_line_bres(screen,linecolor,[30,30],[110,30])
draw_line_bres(screen,linecolor,[30,30],[30,90])
draw_line_bres(screen,linecolor,[30,90],[110,90])
draw_line_bres(screen,linecolor,[110,30],[110,90])
draw_line_bres(screen,linecolor,[40,40],[100,80])

#cuadro 2
draw_line_bres(screen,linecolor,[30,100],[110,100])
draw_line_bres(screen,linecolor,[30,100],[30,160])
draw_line_bres(screen,linecolor,[30,160],[110,160])
draw_line_bres(screen,linecolor,[110,100],[110,160])
Rectangulo_Relleno(screen,blanco,linecolor,[50,110],[90,150])

#cuadro 3
draw_line_bres(screen,linecolor,[30,170],[110,170])
draw_line_bres(screen,linecolor,[30,170],[30,230])
draw_line_bres(screen,linecolor,[30,230],[110,230])
draw_line_bres(screen,linecolor,[110,170],[110,230])
Rectangulo_Relleno(screen,linecolor,linecolor,[50,180],[90,220])

#cuadro 4
draw_line_bres(screen,linecolor,[30,240],[110,240])
draw_line_bres(screen,linecolor,[30,240],[30,290])
draw_line_bres(screen,linecolor,[30,290],[110,290])
draw_line_bres(screen,linecolor,[110,240],[110,290])
circleBres(screen, linecolor,70,265,20)

#cuadro 5
draw_line_bres(screen,linecolor,[30,300],[110,300])
draw_line_bres(screen,linecolor,[30,300],[30,350])
draw_line_bres(screen,linecolor,[30,350],[110,350])
draw_line_bres(screen,linecolor,[110,300],[110,350])
triangulorec(screen,linecolor,50,340,40,30)

#cuadro 6
draw_line_bres(screen,linecolor,[30,360],[110,360])
draw_line_bres(screen,linecolor,[30,360],[30,410])
draw_line_bres(screen,linecolor,[30,410],[110,410])
draw_line_bres(screen,linecolor,[110,360],[110,410])
triangulo(screen,linecolor,50,400,40,30)

#cuadro 7
draw_line_bres(screen,linecolor,[30,420],[110,420])
draw_line_bres(screen,linecolor,[30,420],[30,470])
draw_line_bres(screen,linecolor,[30,470],[110,470])
draw_line_bres(screen,linecolor,[110,420],[110,470])
pentagono(screen,linecolor,50,460,40,440)

#cuadro 8
draw_line_bres(screen,linecolor,[30,480],[110,480])
draw_line_bres(screen,linecolor,[30,480],[30,530])
draw_line_bres(screen,linecolor,[30,530],[110,530])
draw_line_bres(screen,linecolor,[110,480],[110,530])
draw_line_bres(screen,linecolor,[50,500],[80,500])
draw_line_bres(screen,linecolor,[50,510],[80,510])
draw_line_bres(screen,linecolor,[50,500],[50,510])
draw_line_bres(screen,linecolor,[80,500],[80,510])
draw_line_bres(screen,linecolor,[60,500],[60,510])
draw_line_bres(screen,linecolor,[70,500],[70,510])
draw_line_bres(screen,linecolor,[80,500],[90,505])
draw_line_bres(screen,linecolor,[80,510],[90,505])


#cuadro 1 color amarillo
Rectangulo_Relleno(screen,amarillo,linecolor,[590,30],[670,90])

#cuadro 2 color azul
Rectangulo_Relleno(screen,azul,linecolor,[590,100],[670,160])


#cuadro 3 color rojo
Rectangulo_Relleno(screen,rojo,linecolor,[590,170],[670,230])

#cuadro 4 color verde
Rectangulo_Relleno(screen,verde,linecolor,[590,240],[670,290])

#cuadro 5 color naranja
Rectangulo_Relleno(screen,naranja,linecolor,[590,300],[670,350])

#cuadro 6 color blanco
Rectangulo_Relleno(screen,blanco,linecolor,[590,360],[670,410])

#cuadro 7 color gris
Rectangulo_Relleno(screen,gris,linecolor,[590,420],[670,470])

#cuadro 8 color negro
Rectangulo_Relleno(screen,linecolor,linecolor,[590,480],[670,530])

def SeleccionarColor(x,y, figura, color):
    if (x>=590 and y >= 30 and x <= 670 and y <= 90):
        color = amarillo
    
    if (x>=590 and y >= 100 and x <= 670 and y <= 160):
        color = azul

    if (x>=590 and y >= 170 and x <= 670 and y <= 230):
        color = rojo

    if (x>=590 and y >= 240 and x <= 670 and y <= 290):
        color = verde

    if (x>=590 and y >= 300 and x <= 670 and y <= 350):
        color = naranja

    if (x>=590 and y >= 360 and x <= 670 and y <= 410):
        color = blanco

    if (x>=590 and y >= 420 and x <= 670 and y <= 470):
        color = gris

    if (x>=590 and y >= 480 and x <= 670 and y <= 530):
        color = linecolor
    return (color)


def SeleccionarFigura(x,y,figura, color):
    if (x>=30 and y >= 30 and x <= 110 and y <= 90):
        figura ="linea"
    if(x>=30 and y >= 100 and x <= 110 and y <= 160):
        figura ="cuadro"
    if(x>=30 and y >= 170 and x <= 110 and y <= 230):
        figura ="cuadro2"
    if(x>=30 and y >= 240 and x <= 110 and y <= 290):
        figura ="circulo"
    if(x>=30 and y >= 300 and x <= 110 and y <= 350):
        figura ="rectangulo"
    if(x>=30 and y >= 360 and x <= 110 and y <= 410):
        figura ="triangulo"
    if(x>=30 and y >= 420 and x <= 110 and y <= 470):
        figura ="pentagono"
    if(x>=30 and y >= 480 and x <= 110 and y <= 530):
        figura ="lapiz"

    return (figura)



def main():
    figura ="lapiz"
    color = blanco
    cont = 0

    while True:
        for eventos in pygame.event.get():
            if eventos.type == pygame.QUIT:
                exit()
            if eventos.type == pygame.MOUSEBUTTONDOWN:
                x, y = eventos.pos
                if (x >= 20 and y >= 20 and x <= 690 and y <= 570):
                    color = SeleccionarColor(x,y,figura,color)
                    figura = SeleccionarFigura(x,y, figura,color)
                    print ("x --> ", x, "y --> ", y," ", figura," ", color)
                if ( x >= 120 and y >= 20 and x <= 580 and y <= 540):
                    if (figura =="linea"):
                        if ( cont < 2):
                            if ( cont == 0):
                                p1 = list(eventos.pos)
                                x1 = p1[0]
                                y1 = p1[1]
                                print ("dibuja linea punto", cont+1, "x --> ", x1, "y -->", y1)
                                print(cont)
                            if (cont == 1):
                                p2 = list(eventos.pos)
                                x2 = p2[0]
                                y2 = p2[1]
                                print ("dibuja linea punto ", cont+1, "x --> ", x2, "y --> ", y2)
                                draw_line_bres2(screen,color, [x1,y1], [x2,y2])
                            cont += 1
                            if ( cont == 2):
                                cont = 0
                    if (figura =="cuadro"):
                        if ( cont < 2):
                            if ( cont == 0):
                                p1 = list(eventos.pos)
                                x1 = p1[0]
                                y1 = p1[1]
                                print ("dibuja linea punto", cont+1, "x --> ", x1, "y -->", y1)
                                print(cont)
                            if (cont == 1):
                                p2 = list(eventos.pos)
                                x2 = p2[0]
                                y2 = p2[1]
                                print ("dibuja linea punto ", cont+1, "x --> ", x2, "y --> ", y2)
                                Rectangulo_Borde(screen,color, [x1,y1], [x2,y2])
                            cont += 1
                            if ( cont == 2):
                                cont = 0
                    if (figura =="cuadro2"):
                        if ( cont < 2):
                            if ( cont == 0):
                                p1 = list(eventos.pos)
                                x1 = p1[0]
                                y1 = p1[1]
                                print ("dibuja linea punto", cont+1, "x --> ", x1, "y -->", y1)
                                print(cont)
                            if (cont == 1):
                                p2 = list(eventos.pos)
                                x2 = p2[0]
                                y2 = p2[1]
                                print ("dibuja linea punto ", cont+1, "x --> ", x2, "y --> ", y2)
                                Rectangulo_Relleno(screen,color,color, [x1,y1], [x2,y2])
                            cont += 1
                            if ( cont == 2):
                                cont = 0
                    if (figura =="circulo"):
                        if ( cont < 2):
                            if ( cont == 0):
                                p1 = list(eventos.pos)
                                x1 = p1[0]
                                y1 = p1[1]
                                print ("dibuja linea punto", cont+1, "x --> ", x1, "y -->", y1)
                                print(cont)
                            if (cont == 1):
                                p2 = list(eventos.pos)
                                x2 = p2[0]
                                y2 = p2[1]
                                print ("dibuja linea punto ", cont+1, "x --> ", x2, "y --> ", y2)
                                circleBres(screen, color,x1,y1,10)
                            cont += 1
                            if ( cont == 2):
                                cont = 0
                    if (figura =="rectangulo"):
                        if ( cont < 2):
                            if ( cont == 0):
                                p1 = list(eventos.pos)
                                x1 = p1[0]
                                y1 = p1[1]
                                print ("dibuja linea punto", cont+1, "x --> ", x1, "y -->", y1)
                                print(cont)
                            if (cont == 1):
                                p2 = list(eventos.pos)
                                x2 = p2[0]
                                y2 = p2[1]
                                print ("dibuja linea punto ", cont+1, "x --> ", x2, "y --> ", y2)
                                triangulorec(screen,color,x1,y1,x2,y2)
                            cont += 1
                            if ( cont == 2):
                                cont = 0  
                    if (figura =="triangulo"):
                        if ( cont < 2):
                            if ( cont == 0):
                                p1 = list(eventos.pos)
                                x1 = p1[0]
                                y1 = p1[1]
                                print ("dibuja linea punto", cont+1, "x --> ", x1, "y -->", y1)
                                print(cont)
                            if (cont == 1):
                                p2 = list(eventos.pos)
                                x2 = p2[0]
                                y2 = p2[1]
                                print ("dibuja linea punto ", cont+1, "x --> ", x2, "y --> ", y2)
                                triangulo(screen,color,x1,y1,x2,y2)
                            cont += 1
                            if ( cont == 2):
                                cont = 0    
                    if (figura =="pentagono"):
                        if ( cont < 2):
                            if ( cont == 0):
                                p1 = list(eventos.pos)
                                x1 = p1[0]
                                y1 = p1[1]
                                print ("dibuja linea punto", cont+1, "x --> ", x1, "y -->", y1)
                                print(cont)
                            if (cont == 1):
                                p2 = list(eventos.pos)
                                x2 = p2[0]
                                y2 = p2[1]
                                print ("dibuja linea punto ", cont+1, "x --> ", x2, "y --> ", y2)
                                pentagono(screen,color,300,500,200,440)
                            cont += 1
                            if ( cont == 2):
                                cont = 0                     
            if eventos.type == pygame.MOUSEMOTION:
                if(figura =="lapiz"):
                    if pygame.mouse.get_pressed() == (1,0,0):
                        p1 = list(eventos.pos)
                        x1 = p1[0]
                        y1 = p1[1]
                        draw_line_bres2(screen,color, [x1,y1], [x1,y1])
    
        pygame.display.update()



pygame.display.flip()

pygame.display.update()

time.sleep(5)
main()