import math
import numpy as np
import matplotlib.pyplot as plt
import pygame
import time
windows=pygame

def punto(windows, color, p_ini):
    pygame.draw.line(windows,color, p_ini, p_ini,1)



def draw_line_bres(windows, color, p_ini, p_fin):
    x1=p_ini[0]
    y1=p_ini[1]
    x2=p_fin[0]
    y2=p_fin[1]
    dy=y2-y1
    dx= x2-x1
    stepY = -1 if dy < 0 else 1
    dy = math.fabs(dy)
    stepX = -1 if dx < 0 else 1
    dx = math.fabs(dx)

    if dx > dy:
        p = 2 * dy - dx
        incE = 2 * dy
        incNE = 2 * (dy - dx)
        x = x1
        y = y1
        xEnd = x2
        stepX = 1
        punto(windows, color,[x,y])
        while x != xEnd:
            if x < xEnd:
                x += stepX
            else:
                x -= stepX
            if p < 0:
                p += incE
            else:
                p += incNE
                y += stepY
            punto(windows, color, [x,y])
    
    else:
        p = 2 * dx - dy
        incE = 2 * dx
        incNE = 2 * (dx - dy)
        x = x1
        y = y1
        yEnd = y2
        stepY = 1
        punto(windows, color, [x,y])
        while y != yEnd:
            if y < yEnd:
                y += stepY
            else:
                y -= stepY
            if p < 0:
                p += incE
            else:
                p += incNE
                x += stepX
            punto(windows, color, [x,y])


def Rectangulo_Relleno(windows,colorb,colorr,pos_ini,pos_fin):
    X0= pos_ini[0]
    Y0= pos_ini[1]
    X1= pos_fin[0]
    Y1= pos_fin[1]
    draw_line_bres(windows, colorb, [X0, Y0],[X1,Y0])
    draw_line_bres(windows, colorb, [X0, Y1],[X1,Y1])
    draw_line_bres(windows, colorb, [X0, Y0],[X0,Y1])
    draw_line_bres(windows, colorb, [X1, Y0],[X1,Y1])
    Y0= Y0 +1
    t=Y0-1
    j = (Y1 + Y0-1)/ 2
    h = (X1+X0)/2
    while Y0 < Y1:
        if t < j:
            draw_line_bres(windows, colorr, [X0+1, Y0],[h,Y0])
            Y0=Y0+1
            t=t+1
        else:
            draw_line_bres(windows, colorr, [h, Y0],[X1,Y0])
            Y0=Y0+1


def Figura_Dos(windows,colorb,colorr,pos_ini,pos_fin):
    X0= pos_ini[0]
    Y0= pos_ini[1]
    X1= pos_fin[0]
    Y1= pos_fin[1]
    draw_line_bres(windows, colorb, [X0, Y0],[X1,Y0])
    draw_line_bres(windows, colorb, [X0, Y1],[X1,Y1])
    draw_line_bres(windows, colorb, [X0, Y0],[X0,Y1])
    draw_line_bres(windows, colorb, [X1, Y0],[X1,Y1])
    Y0= Y0 +1
    t=50
    j=150
    p=250
    q=250
    while Y0 < 150:
            draw_line_bres(windows, colorr, [X0+1, Y0],[200,Y0])
            Y0=Y0+1
    while p < 350:
            draw_line_bres(windows, colorr, [X0+1, p],[200,p])
            p=p+1
    while q < 350:
            draw_line_bres(windows, colorr, [300, q],[400,q])
            q=q+1
    while t < 150:
            draw_line_bres(windows, colorr, [300, t],[400,t])
            t=t+1
    while j < 250:
            draw_line_bres(windows, colorr, [200, j],[300,j])
            j=j+1
   

def Figura_Tres(windows,colorb,colorr,pos_ini,pos_fin):
    X0= pos_ini[0]
    Y0= pos_ini[1]
    X1= pos_fin[0]
    Y1= pos_fin[1]
    draw_line_bres(windows, colorb, [X0, Y0],[X1,Y0])
    draw_line_bres(windows, colorb, [X0, Y1],[X1,Y1])
    draw_line_bres(windows, colorb, [X0, Y0],[X0,Y1])
    draw_line_bres(windows, colorb, [X1, Y0],[X1,Y1])
    Y0= Y0 +1
    t=150
    j=150
    p=250
    q=150
    while Y0 < 150:
            draw_line_bres(windows, colorr, [200, Y0],[300,Y0])
            Y0=Y0+1
    while p < 350:
            draw_line_bres(windows, colorr, [200, p],[300,p])
            p=p+1
    while j < 250:
            draw_line_bres(windows, colorr, [200, j],[300,j])
            j=j+1
    while t < 250:
            draw_line_bres(windows, colorr, [100, t],[200,t])
            t=t+1 
    while q < 250:
            draw_line_bres(windows, colorr, [300, q],[400,q])
            q=q+1   


def Figura_Cuatro(windows,colorb,colorr,pos_ini,pos_fin):
    X0= pos_ini[0]
    Y0= pos_ini[1]
    X1= pos_fin[0]
    Y1= pos_fin[1]
    draw_line_bres(windows, blanco, [X0, Y0],[X1,Y0])
    draw_line_bres(windows, blanco, [X0, Y1],[X1,Y1])
    draw_line_bres(windows, blanco, [X0, Y0],[X0,Y1])
    draw_line_bres(windows, blanco, [X1, Y0],[X1,Y1])
    Y0= Y0 +1
    t=150
    j=250
    p=350
    q=450
    while Y0 < 150:
            draw_line_bres(windows,colorr, [X0, Y0],[200,Y0])
            Y0=Y0+1
    while t < 250:
            draw_line_bres(windows,colorr, [X0, t],[300,t])
            t=t+1
    while j < 350:
            draw_line_bres(windows,colorr, [X0, j],[400,j])
            j=j+1
    while p < 450:
            draw_line_bres(windows,colorr, [X0, p],[500,p])
            p=p+1
    while q < 550:
            draw_line_bres(windows,colorr, [X0, q],[600,q])
            q=q+1
  

def Figura_Cinco(windows,colorb,colorr,pos_ini,pos_fin):
    X0= pos_ini[0]
    Y0= pos_ini[1]
    X1= pos_fin[0]
    Y1= pos_fin[1]
    draw_line_bres(windows, blanco, [X0, Y0],[X1,Y0])
    draw_line_bres(windows, blanco, [X0, Y1],[X1,Y1])
    draw_line_bres(windows, blanco, [X0, Y0],[X0,Y1])
    draw_line_bres(windows, blanco, [X1, Y0],[X1,Y1])
    Y0= Y0 +1
    t=100
    j=200
    p=300
    q=400
    s=500
    while Y0 < 100:
            draw_line_bres(windows,colorr, [350, Y0],[450,Y0])
            Y0=Y0+1
    while t < 200:
            draw_line_bres(windows,colorr, [300, t],[500,t])
            t=t+1
    while j < 300:
            draw_line_bres(windows,colorr, [250, j],[550,j])
            j=j+1
    while p < 400:
            draw_line_bres(windows,colorr, [200, p],[600,p])
            p=p+1
    while q < 500:
            draw_line_bres(windows,colorr, [150, q],[650,q])
            q=q+1
    while s < 600:
            draw_line_bres(windows,colorr, [100, s],[700,s])
            s=s+1


def triangulorec(windows,colorb,x_ini,y_ini,base,altu):
    X0= x_ini
    Y0= y_ini
    draw_line_bres(windows, colorb, [X0, Y0],[X0+base,Y0])
    draw_line_bres(windows, colorb, [X0, Y0],[X0,Y0-altu])
    draw_line_bres(windows, colorb, [X0+base, Y0],[X0, Y0-altu])
    


def triangulo(windows,colorb,x_ini,y_ini,base,altu):
    X0= x_ini
    Y0= y_ini
    draw_line_bres(windows, colorb, [X0, Y0],[X0+base,Y0])
    draw_line_bres(windows, colorb, [X0, Y0],[X0+(base/2),Y0-altu])
    draw_line_bres(windows, colorb, [X0+base, Y0],[X0+(base/2),Y0-altu])


def circulo(windows,colorb,xc,yc,x,y):
    punto(windows,colorb,[xc+x,yc+y])
    punto(windows,colorb,[xc-x,yc+y])
    punto(windows,colorb,[xc+x,yc-y])
    punto(windows,colorb,[xc-x,yc-y])
    punto(windows,colorb,[xc+y,yc+x])
    punto(windows,colorb,[xc-y,yc+x])
    punto(windows,colorb,[xc+y,yc-x])
    punto(windows,colorb,[xc-y,yc-x])


def circleBres(windows, color, xc,yc,r):
    x = 0
    y = r
    d = 3 - 2 * r
    circulo(windows, color, xc,yc,x,y)
    while (y >= x):
        x = x + 1
        if (d > 0):
            y = y - 1
            d = d + 4 * (x - y) + 10
        else:
            d = d + 4 * x + 6
        circulo(windows, color, xc,yc,x,y)

def trapecio(windows,colorb,x_ini,y_ini,base_menor,base_mayor,base,altu):
    X0= x_ini
    Y0= y_ini
    draw_line_bres(windows, colorb, [X0, Y0],[base_mayor,Y0])
    draw_line_bres(windows, colorb, [X0+(base_mayor/4), altu],[base_menor-(base_mayor/4),altu])
    draw_line_bres(windows, colorb, [X0, Y0],[X0+(base_mayor/4),altu])
    draw_line_bres(windows, colorb, [base_mayor,Y0],[base_menor-(base_mayor/4),altu])


def pentagono(windows,colorb,x_ini,y_ini,lado,borde):
    X0= x_ini
    Y0= y_ini
    draw_line_bres(windows, colorb, [X0, Y0],[lado,Y0])
    draw_line_bres(windows, colorb, [X0-(lado*0.1), lado],[X0,Y0])
    draw_line_bres(windows, colorb, [lado+(lado*0.1), lado],[lado,Y0])
    draw_line_bres(windows, colorb, [lado+(lado*0.1), lado],[230,borde-100])
    draw_line_bres(windows, colorb, [X0-(lado*0.1), lado],[230,borde-100])
   

pygame.init()
windows=pygame.display.set_mode((800,600))
windows.fill((255,255,255))
amarillo=np.array([255,255,0])
rojo=np.array([255,0,0])
verde=np.array([0,255,0])
azul=np.array([0,0,255])
blanco=np.array([255,255,255])
negro=np.array([0,0,0])


#figura 1
#Rectangulo_Relleno(windows,negro,azul,[250,50],[600,300])

#figura 2
#Figura_Dos(windows,negro,azul,[100,50],[400,350])

#figura 3
#Figura_Tres(windows,negro,azul,[100,50],[400,350])

#figura 4
#Figura_Cuatro(windows,negro,azul,[100,50],[600,550])

#figura 5
#Figura_Cinco(windows,negro,azul,[100,0],[700,600])

#figura 6
#triangulorec(windows,azul,200,300,100,100)

#figura 7
#triangulo(windows,azul,300,400,200,200)

#figura 8
trapecio(windows,azul,100,500,500,500,100,300)

#figura 9
#pentagono(windows,azul,100,500,350,350)

#figura 10
#circleBres(windows,azul,300,200,50)



pygame.display.update()

time.sleep(5)