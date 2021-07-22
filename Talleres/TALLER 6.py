import math
import numpy as np
import matplotlib.pyplot as plt
import pygame
import time

pygame.init()
windows= pygame.display.set_mode((900,700))


def Figura_Robot():
    #cuello
    pygame.draw.line(windows,(255,255,255),(400,180),(400,200),1)
    pygame.draw.line(windows,(255,255,255),(500,180),(500,200),1)

    #cara
    pygame.draw.line(windows,(255,255,255),(350,180),(550,180),1)
    pygame.draw.line(windows,(255,255,255),(350,100),(550,100),1)
    pygame.draw.line(windows,(255,255,255),(350,100),(350,180),1)
    pygame.draw.line(windows,(255,255,255),(550,100),(550,180),1)
    pygame.draw.line(windows,(255,255,255),(420,170),(480,170),1)
    pygame.draw.line(windows,(255,255,255),(420,155),(480,155),1)
    pygame.draw.line(windows,(255,255,255),(420,155),(420,170),1)
    pygame.draw.line(windows,(255,255,255),(480,155),(480,170),1)
    pygame.draw.line(windows,(255,255,255),(435,155),(435,170),1)
    pygame.draw.line(windows,(255,255,255),(450,155),(450,170),1)
    pygame.draw.circle(windows,(255,255,255),(400,125), 15,1)
    pygame.draw.circle(windows,(255,255,255),(500,125), 15,1)
    pygame.draw.arc(windows,(255,255,255),[385, 120, 20, 15],  0, math.pi / 2, 1)
    pygame.draw.arc(windows,(255,255,255),[485, 120, 20, 15],  0, math.pi / 2, 1)

    #antena
    pygame.draw.line(windows,(255,255,255),(465,155),(465,170),1)
    pygame.draw.line(windows,(255,255,255),(445,40),(445,100),1)
    pygame.draw.line(windows,(255,255,255),(455,40),(455,100),1)
    pygame.draw.circle(windows,(255,255,255),(450,28), 15,1)

    #brazo izq
    pygame.draw.line(windows,(255,255,255),(270,220),(300,220),1)
    pygame.draw.line(windows,(255,255,255),(270,230),(300,230),1)
    pygame.draw.circle(windows,(255,255,255),(245,225), 25,1)
    pygame.draw.circle(windows,(255,255,255),(245,225), 10,1)
    pygame.draw.line(windows,(255,255,255),(255,245),(255,260),1)
    pygame.draw.line(windows,(255,255,255),(235,245),(235,260),1)
    pygame.draw.line(windows,(255,255,255),(230,260),(260,260),1)
    pygame.draw.line(windows,(255,255,255),(230,370),(260,370),1)
    pygame.draw.line(windows,(255,255,255),(230,260),(230,370),1)
    pygame.draw.line(windows,(255,255,255),(260,260),(260,370),1)
    pygame.draw.line(windows,(255,255,255),(240,370),(240,385),1)
    pygame.draw.line(windows,(255,255,255),(250,370),(250,385),1)
    pygame.draw.circle(windows,(255,255,255),(245,394), 12,1)
    pygame.draw.line(windows,(255,255,255),(257,390),(257,415),1)
    pygame.draw.line(windows,(255,255,255),(267,390),(267,415),1)
    pygame.draw.line(windows,(255,255,255),(257,390),(267,390),1)
    pygame.draw.line(windows,(255,255,255),(257,415),(267,415),1)
    pygame.draw.line(windows,(255,255,255),(233,390),(233,415),1)
    pygame.draw.line(windows,(255,255,255),(223,390),(223,415),1)
    pygame.draw.line(windows,(255,255,255),(223,390),(233,390),1)
    pygame.draw.line(windows,(255,255,255),(223,415),(233,415),1)

    #brazo derecho
    pygame.draw.line(windows,(255,255,255),(600,220),(630,220),1)
    pygame.draw.line(windows,(255,255,255),(600,230),(630,230),1)
    pygame.draw.circle(windows,(255,255,255),(655,225), 25,1)
    pygame.draw.circle(windows,(255,255,255),(655,225), 10,1)
    pygame.draw.line(windows,(255,255,255),(645,245),(645,260),1)
    pygame.draw.line(windows,(255,255,255),(665,245),(665,260),1)
    pygame.draw.line(windows,(255,255,255),(640,260),(670,260),1)
    pygame.draw.line(windows,(255,255,255),(640,370),(670,370),1)
    pygame.draw.line(windows,(255,255,255),(640,260),(640,370),1)
    pygame.draw.line(windows,(255,255,255),(670,260),(670,370),1)
    pygame.draw.line(windows,(255,255,255),(650,370),(650,385),1)
    pygame.draw.line(windows,(255,255,255),(660,370),(660,385),1)
    pygame.draw.circle(windows,(255,255,255),(655,394), 12,1)
    pygame.draw.line(windows,(255,255,255),(667,390),(667,415),1)
    pygame.draw.line(windows,(255,255,255),(677,390),(677,415),1)
    pygame.draw.line(windows,(255,255,255),(667,390),(677,390),1)
    pygame.draw.line(windows,(255,255,255),(667,415),(677,415),1)
    pygame.draw.line(windows,(255,255,255),(643,390),(643,415),1)
    pygame.draw.line(windows,(255,255,255),(633,390),(633,415),1)
    pygame.draw.line(windows,(255,255,255),(633,390),(643,390),1)
    pygame.draw.line(windows,(255,255,255),(633,415),(643,415),1)

    #pie izquierdo
    pygame.draw.line(windows,(255,255,255),(350,400),(350,520),1)
    pygame.draw.line(windows,(255,255,255),(380,400),(380,520),1)
    pygame.draw.line(windows,(255,255,255),(350,520),(380,520),1)
    pygame.draw.line(windows,(255,255,255),(380,520),(380,555),1)
    pygame.draw.line(windows,(255,255,255),(250,555),(380,555),1)
    pygame.draw.line(windows,(255,255,255),(380,520),(250,555),1)
    pygame.draw.line(windows,(255,255,255),(350,520),(350,527),1)

    #pie derecho
    pygame.draw.line(windows,(255,255,255),(550,400),(550,520),1)
    pygame.draw.line(windows,(255,255,255),(520,400),(520,520),1)
    pygame.draw.line(windows,(255,255,255),(520,520),(550,520),1)
    pygame.draw.line(windows,(255,255,255),(520,520),(520,555),1)
    pygame.draw.line(windows,(255,255,255),(520,555),(650,555),1)
    pygame.draw.line(windows,(255,255,255),(520,520),(650,555),1)
    pygame.draw.line(windows,(255,255,255),(550,520),(550,527),1)

    #cuerpo
    pygame.draw.line(windows,(255,255,255),(300,400),(600,400),1)
    pygame.draw.line(windows,(255,255,255),(300,200),(600,200),1)
    pygame.draw.line(windows,(255,255,255),(300,200),(300,400),1)
    pygame.draw.line(windows,(255,255,255),(600,200),(600,400),1)

    pygame.draw.line(windows,(255,255,255),(330,280),(570,280),1)
    pygame.draw.line(windows,(255,255,255),(330,230),(570,230),1)
    pygame.draw.line(windows,(255,255,255),(330,230),(330,280),1)
    pygame.draw.line(windows,(255,255,255),(570,230),(570,280),1)

    pygame.draw.line(windows,(255,255,255),(345,270),(391,270),1)
    pygame.draw.line(windows,(255,255,255),(345,270),(368,235),1)
    pygame.draw.line(windows,(255,255,255),(368,235),(391,270),1)

    pygame.draw.line(windows,(255,255,255),(406,270),(452,270),1)
    pygame.draw.line(windows,(255,255,255),(406,270),(429,235),1)
    pygame.draw.line(windows,(255,255,255),(429,235),(452,270),1)

    pygame.draw.line(windows,(255,255,255),(468,270),(514,270),1)
    pygame.draw.line(windows,(255,255,255),(468,270),(491,235),1)
    pygame.draw.line(windows,(255,255,255),(491,235),(514,270),1)

    pygame.draw.line(windows,(255,255,255),(529,270),(565,270),1)
    pygame.draw.line(windows,(255,255,255),(529,270),(547,235),1)
    pygame.draw.line(windows,(255,255,255),(547,235),(565,270),1)

    pygame.draw.circle(windows,(255,255,255),(380,370), 12,1)
    pygame.draw.circle(windows,(255,255,255),(430,370), 12,1)
    pygame.draw.circle(windows,(255,255,255),(470,370), 12,1)
    pygame.draw.circle(windows,(255,255,255),(510,370), 12,1)

    pygame.display.update()
    time.sleep(5)



def Figura_Casa():
    #casa
    pygame.draw.line(windows,(255,255,255),(100,600),(800,600),1)
    pygame.draw.line(windows,(255,255,255),(120,450),(120,600),1)
    pygame.draw.line(windows,(255,255,255),(250,450),(250,600),1)
    pygame.draw.line(windows,(255,255,255),(120,450),(185,350),1)
    pygame.draw.line(windows,(255,255,255),(250,450),(185,350),1)
    pygame.draw.line(windows,(255,255,255),(120,450),(480,450),1)
    pygame.draw.line(windows,(255,255,255),(480,450),(480,600),1)
    pygame.draw.line(windows,(255,255,255),(185,350),(400,350),1)
    pygame.draw.line(windows,(255,255,255),(400,350),(480,450),1)

    #torre
    pygame.draw.line(windows,(255,255,255),(550,600),(550,10),1)
    pygame.draw.line(windows,(255,255,255),(380,350),(440,150),1)
    pygame.draw.line(windows,(255,255,255),(440,150),(550,140),1)

    pygame.draw.line(windows,(255,255,255),(720,600),(660,150),1)
    pygame.draw.line(windows,(255,255,255),(660,150),(550,140),1)

    pygame.draw.line(windows,(255,255,255),(440,150),(400,130),1)
    pygame.draw.line(windows,(255,255,255),(660,150),(700,130),1)
    pygame.draw.line(windows,(255,255,255),(400,130),(550,115),1)
    pygame.draw.line(windows,(255,255,255),(700,130),(550,115),1)
    pygame.draw.line(windows,(255,255,255),(400,130),(550,10),1)
    pygame.draw.line(windows,(255,255,255),(700,130),(550,10),1)

    #ventanas
    pygame.draw.line(windows,(255,255,255),(480,500),(490,500),1)
    pygame.draw.line(windows,(255,255,255),(490,500),(500,400),1)
    pygame.draw.line(windows,(255,255,255),(440,400),(500,400),1)
    pygame.draw.line(windows,(255,255,255),(490,370),(500,300),1)
    pygame.draw.line(windows,(255,255,255),(430,370),(440,300),1)
    pygame.draw.line(windows,(255,255,255),(440,300),(500,300),1)
    pygame.draw.line(windows,(255,255,255),(430,370),(490,370),1)
    pygame.draw.line(windows,(255,255,255),(510,250),(520,180),1)
    pygame.draw.line(windows,(255,255,255),(450,250),(460,180),1)
    pygame.draw.line(windows,(255,255,255),(450,250),(510,250),1)
    pygame.draw.line(windows,(255,255,255),(520,180),(460,180),1)

    pygame.draw.line(windows,(255,255,255),(660,500),(600,500),1)
    pygame.draw.line(windows,(255,255,255),(600,500),(590,400),1)
    pygame.draw.line(windows,(255,255,255),(650,400),(590,400),1)
    pygame.draw.line(windows,(255,255,255),(660,500),(650,400),1)

    pygame.draw.line(windows,(255,255,255),(660,370),(650,300),1)
    pygame.draw.line(windows,(255,255,255),(600,370),(590,300),1)
    pygame.draw.line(windows,(255,255,255),(650,300),(590,300),1)
    pygame.draw.line(windows,(255,255,255),(660,370),(600,370),1)

    pygame.draw.line(windows,(255,255,255),(650,250),(640,180),1)
    pygame.draw.line(windows,(255,255,255),(590,250),(580,180),1)
    pygame.draw.line(windows,(255,255,255),(650,250),(590,250),1)
    pygame.draw.line(windows,(255,255,255),(640,180),(580,180),1)

    pygame.display.update()
    time.sleep(10)


def Figura_3():
    pygame.draw.line(windows,(255,255,255),(100,50),(700,50),1)
    pygame.draw.line(windows,(255,255,255),(100,650),(700,650),1)
    pygame.draw.line(windows,(255,255,255),(100,50),(100,650),1)
    pygame.draw.line(windows,(255,255,255),(700,50),(700,650),1)
    pygame.draw.line(windows,(255,255,255),(400,50),(400,350),1)
    pygame.draw.line(windows,(255,255,255),(400,350),(100,350),1)
    pygame.draw.line(windows,(255,255,255),(400,350),(700,350),1)
    pygame.draw.line(windows,(255,255,255),(400,350),(400,650),1)

    #triangulo 1
    pygame.draw.line(windows,(255,255,255),(250,50),(100,200),1)
    pygame.draw.line(windows,(255,255,255),(550,50),(400,200),1)
    pygame.draw.line(windows,(255,255,255),(250,350),(100,500),1)
    pygame.draw.line(windows,(255,255,255),(550,350),(400,500),1)
    pygame.draw.line(windows,(255,255,255),(175,125),(325,125),1)
    pygame.draw.line(windows,(255,255,255),(175,275),(325,275),1)
    pygame.draw.line(windows,(255,255,255),(175,125),(175,275),1)
    pygame.draw.line(windows,(255,255,255),(325,125),(325,275),1)
    pygame.draw.line(windows,(255,255,255),(250,125),(175,200),1)
    pygame.draw.line(windows,(255,255,255),(250,125),(325,200),1)
    pygame.draw.line(windows,(255,255,255),(175,200),(250,275),1)
    pygame.draw.line(windows,(255,255,255),(325,200),(250,275),1)
    pygame.draw.line(windows,(255,255,255),(212.5,162.5),(287.5,237.5),1)
    pygame.draw.line(windows,(255,255,255),(287.5,162.5),(212.5,237.5),1)

    #triangulo 2
    pygame.draw.line(windows,(255,255,255),(250,50),(400,200),1)
    pygame.draw.line(windows,(255,255,255),(550,50),(700,200),1)
    pygame.draw.line(windows,(255,255,255),(250,350),(400,500),1)
    pygame.draw.line(windows,(255,255,255),(550,350),(700,500),1)
    pygame.draw.line(windows,(255,255,255),(475,125),(625,125),1)
    pygame.draw.line(windows,(255,255,255),(475,275),(625,275),1)
    pygame.draw.line(windows,(255,255,255),(475,125),(475,275),1)
    pygame.draw.line(windows,(255,255,255),(625,125),(625,275),1)
    pygame.draw.line(windows,(255,255,255),(550,125),(475,200),1)
    pygame.draw.line(windows,(255,255,255),(550,125),(625,200),1)
    pygame.draw.line(windows,(255,255,255),(475,200),(550,275),1)
    pygame.draw.line(windows,(255,255,255),(625,200),(550,275),1)
    pygame.draw.line(windows,(255,255,255),(512.5,162.5),(587.5,237.5),1)
    pygame.draw.line(windows,(255,255,255),(587.5,162.5),(512.5,237.5),1)

    #triangulo 3
    pygame.draw.line(windows,(255,255,255),(250,350),(100,200),1)
    pygame.draw.line(windows,(255,255,255),(550,350),(400,200),1)
    pygame.draw.line(windows,(255,255,255),(250,650),(100,500),1)
    pygame.draw.line(windows,(255,255,255),(550,650),(400,500),1)
    pygame.draw.line(windows,(255,255,255),(175,425),(325,425),1)
    pygame.draw.line(windows,(255,255,255),(175,575),(325,575),1)
    pygame.draw.line(windows,(255,255,255),(175,425),(175,575),1)
    pygame.draw.line(windows,(255,255,255),(325,425),(325,575),1)
    pygame.draw.line(windows,(255,255,255),(250,425),(175,500),1)
    pygame.draw.line(windows,(255,255,255),(250,425),(325,500),1)
    pygame.draw.line(windows,(255,255,255),(250,575),(175,500),1)
    pygame.draw.line(windows,(255,255,255),(250,575),(325,500),1)
    pygame.draw.line(windows,(255,255,255),(212.5,462.5),(287.5,537.5),1)
    pygame.draw.line(windows,(255,255,255),(287.5,462.5),(212.5,537.5),1)

    #triangulo 4
    pygame.draw.line(windows,(255,255,255),(250,350),(400,200),1)
    pygame.draw.line(windows,(255,255,255),(550,350),(700,200),1)
    pygame.draw.line(windows,(255,255,255),(250,650),(400,500),1)
    pygame.draw.line(windows,(255,255,255),(550,650),(700,500),1)

    pygame.draw.line(windows,(255,255,255),(475,425),(625,425),1)
    pygame.draw.line(windows,(255,255,255),(475,575),(625,575),1)
    pygame.draw.line(windows,(255,255,255),(475,425),(475,575),1)
    pygame.draw.line(windows,(255,255,255),(625,425),(625,575),1)
    pygame.draw.line(windows,(255,255,255),(550,425),(475,500),1)
    pygame.draw.line(windows,(255,255,255),(550,425),(625,500),1)
    pygame.draw.line(windows,(255,255,255),(550,575),(475,500),1)
    pygame.draw.line(windows,(255,255,255),(550,575),(625,500),1)
    pygame.draw.line(windows,(255,255,255),(512.5,462.5),(587.5,537.5),1)
    pygame.draw.line(windows,(255,255,255),(587.5,462.5),(512.5,537.5),1)

    pygame.display.update()
    time.sleep(10)


def figura_cuatro():
    pygame.draw.line(windows,(255,255,255),(100,50),(700,50),1)
    pygame.draw.line(windows,(255,255,255),(100,650),(700,650),1)
    pygame.draw.line(windows,(255,255,255),(100,50),(100,650),1)
    pygame.draw.line(windows,(255,255,255),(700,50),(700,650),1)
    pygame.draw.line(windows,(255,255,255),(400,50),(400,350),1)
    pygame.draw.line(windows,(255,255,255),(400,350),(100,350),1)
    pygame.draw.line(windows,(255,255,255),(400,350),(700,350),1)
    pygame.draw.line(windows,(255,255,255),(400,350),(400,650),1)

    pygame.draw.line(windows,(255,255,255),(250,50),(250,650),1)
    pygame.draw.line(windows,(255,255,255),(550,50),(550,650),1)

    pygame.draw.line(windows,(255,255,255),(100,200),(700,200),1)
    pygame.draw.line(windows,(255,255,255),(100,500),(700,500),1)

    #cuadro 1
    pygame.draw.line(windows,(255,255,255),(225,50),(100,175),1)
    pygame.draw.line(windows,(255,255,255),(200,50),(100,150),1)
    pygame.draw.line(windows,(255,255,255),(175,50),(100,125),1)
    pygame.draw.line(windows,(255,255,255),(150,50),(100,100),1)
    pygame.draw.line(windows,(255,255,255),(125,50),(100,75),1)
    pygame.draw.line(windows,(255,255,255),(250,50),(100,200),5)
    pygame.draw.line(windows,(255,255,255),(250,75),(125,200),1)
    pygame.draw.line(windows,(255,255,255),(250,100),(150,200),1)
    pygame.draw.line(windows,(255,255,255),(250,125),(175,200),1)
    pygame.draw.line(windows,(255,255,255),(250,150),(200,200),1)
    pygame.draw.line(windows,(255,255,255),(250,175),(225,200),1)

    #cuadro 2
    pygame.draw.line(windows,(255,255,255),(375,50),(400,75),1)
    pygame.draw.line(windows,(255,255,255),(350,50),(400,100),1)
    pygame.draw.line(windows,(255,255,255),(325,50),(400,125),1)
    pygame.draw.line(windows,(255,255,255),(300,50),(400,150),1)
    pygame.draw.line(windows,(255,255,255),(275,50),(400,175),1)
    pygame.draw.line(windows,(255,255,255),(250,50),(400,200),5)
    pygame.draw.line(windows,(255,255,255),(250,75),(375,200),1)
    pygame.draw.line(windows,(255,255,255),(250,100),(350,200),1)
    pygame.draw.line(windows,(255,255,255),(250,125),(325,200),1)
    pygame.draw.line(windows,(255,255,255),(250,150),(300,200),1)
    pygame.draw.line(windows,(255,255,255),(250,175),(275,200),1)

    #cuadro 3
    pygame.draw.line(windows,(255,255,255),(525,50),(400,175),1)
    pygame.draw.line(windows,(255,255,255),(500,50),(400,150),1)
    pygame.draw.line(windows,(255,255,255),(475,50),(400,125),1)
    pygame.draw.line(windows,(255,255,255),(450,50),(400,100),1)
    pygame.draw.line(windows,(255,255,255),(425,50),(400,75),1)
    pygame.draw.line(windows,(255,255,255),(550,50),(400,200),5)
    pygame.draw.line(windows,(255,255,255),(550,75),(425,200),1)
    pygame.draw.line(windows,(255,255,255),(550,100),(450,200),1)
    pygame.draw.line(windows,(255,255,255),(550,125),(475,200),1)
    pygame.draw.line(windows,(255,255,255),(550,150),(500,200),1)
    pygame.draw.line(windows,(255,255,255),(550,175),(525,200),1)

    #cuadro 4
    pygame.draw.line(windows,(255,255,255),(675,50),(700,75),1)
    pygame.draw.line(windows,(255,255,255),(650,50),(700,100),1)
    pygame.draw.line(windows,(255,255,255),(625,50),(700,125),1)
    pygame.draw.line(windows,(255,255,255),(600,50),(700,150),1)
    pygame.draw.line(windows,(255,255,255),(575,50),(700,175),1)
    pygame.draw.line(windows,(255,255,255),(550,50),(700,200),5)
    pygame.draw.line(windows,(255,255,255),(550,75),(675,200),1)
    pygame.draw.line(windows,(255,255,255),(550,100),(650,200),1)
    pygame.draw.line(windows,(255,255,255),(550,125),(625,200),1)
    pygame.draw.line(windows,(255,255,255),(550,150),(600,200),1)
    pygame.draw.line(windows,(255,255,255),(550,175),(575,200),1)

    #cuadro 5
    pygame.draw.line(windows,(255,255,255),(225,200),(250,225),1)
    pygame.draw.line(windows,(255,255,255),(200,200),(250,250),1)
    pygame.draw.line(windows,(255,255,255),(175,200),(250,275),1)
    pygame.draw.line(windows,(255,255,255),(150,200),(250,300),1)
    pygame.draw.line(windows,(255,255,255),(125,200),(250,325),1)
    pygame.draw.line(windows,(255,255,255),(100,200),(250,350),5)
    pygame.draw.line(windows,(255,255,255),(100,225),(225,350),1)
    pygame.draw.line(windows,(255,255,255),(100,250),(200,350),1)
    pygame.draw.line(windows,(255,255,255),(100,275),(175,350),1)
    pygame.draw.line(windows,(255,255,255),(100,300),(150,350),1)
    pygame.draw.line(windows,(255,255,255),(100,325),(125,350),1)

    #cuadro 6
    pygame.draw.line(windows,(255,255,255),(275,200),(250,225),1)
    pygame.draw.line(windows,(255,255,255),(300,200),(250,250),1)
    pygame.draw.line(windows,(255,255,255),(325,200),(250,275),1)
    pygame.draw.line(windows,(255,255,255),(350,200),(250,300),1)
    pygame.draw.line(windows,(255,255,255),(375,200),(250,325),1)
    pygame.draw.line(windows,(255,255,255),(400,200),(250,350),5)
    pygame.draw.line(windows,(255,255,255),(400,225),(275,350),1)
    pygame.draw.line(windows,(255,255,255),(400,250),(300,350),1)
    pygame.draw.line(windows,(255,255,255),(400,275),(325,350),1)
    pygame.draw.line(windows,(255,255,255),(400,300),(350,350),1)
    pygame.draw.line(windows,(255,255,255),(400,325),(375,350),1)

    #cuadro 7
    pygame.draw.line(windows,(255,255,255),(525,200),(550,225),1)
    pygame.draw.line(windows,(255,255,255),(500,200),(550,250),1)
    pygame.draw.line(windows,(255,255,255),(475,200),(550,275),1)
    pygame.draw.line(windows,(255,255,255),(450,200),(550,300),1)
    pygame.draw.line(windows,(255,255,255),(425,200),(550,325),1)
    pygame.draw.line(windows,(255,255,255),(400,200),(550,350),5)
    pygame.draw.line(windows,(255,255,255),(400,225),(525,350),1)
    pygame.draw.line(windows,(255,255,255),(400,250),(500,350),1)
    pygame.draw.line(windows,(255,255,255),(400,275),(475,350),1)
    pygame.draw.line(windows,(255,255,255),(400,300),(450,350),1)
    pygame.draw.line(windows,(255,255,255),(400,325),(425,350),1)

    #cuadro 8
    pygame.draw.line(windows,(255,255,255),(575,200),(550,225),1)
    pygame.draw.line(windows,(255,255,255),(600,200),(550,250),1)
    pygame.draw.line(windows,(255,255,255),(625,200),(550,275),1)
    pygame.draw.line(windows,(255,255,255),(650,200),(550,300),1)
    pygame.draw.line(windows,(255,255,255),(675,200),(550,325),1)
    pygame.draw.line(windows,(255,255,255),(700,200),(550,350),5)
    pygame.draw.line(windows,(255,255,255),(700,225),(575,350),1)
    pygame.draw.line(windows,(255,255,255),(700,250),(600,350),1)
    pygame.draw.line(windows,(255,255,255),(700,275),(625,350),1)
    pygame.draw.line(windows,(255,255,255),(700,300),(650,350),1)
    pygame.draw.line(windows,(255,255,255),(700,325),(675,350),1)

    #cuadro 9
    pygame.draw.line(windows,(255,255,255),(125,350),(100,375),1)
    pygame.draw.line(windows,(255,255,255),(150,350),(100,400),1)
    pygame.draw.line(windows,(255,255,255),(175,350),(100,425),1)
    pygame.draw.line(windows,(255,255,255),(200,350),(100,450),1)
    pygame.draw.line(windows,(255,255,255),(225,350),(100,475),1)
    pygame.draw.line(windows,(255,255,255),(250,350),(100,500),5)
    pygame.draw.line(windows,(255,255,255),(250,375),(125,500),1)
    pygame.draw.line(windows,(255,255,255),(250,400),(150,500),1)
    pygame.draw.line(windows,(255,255,255),(250,425),(175,500),1)
    pygame.draw.line(windows,(255,255,255),(250,450),(200,500),1)
    pygame.draw.line(windows,(255,255,255),(250,475),(225,500),1)

    #cuadro 10
    pygame.draw.line(windows,(255,255,255),(375,350),(400,375),1)
    pygame.draw.line(windows,(255,255,255),(350,350),(400,400),1)
    pygame.draw.line(windows,(255,255,255),(325,350),(400,425),1)
    pygame.draw.line(windows,(255,255,255),(300,350),(400,450),1)
    pygame.draw.line(windows,(255,255,255),(275,350),(400,475),1)
    pygame.draw.line(windows,(255,255,255),(250,350),(400,500),5)
    pygame.draw.line(windows,(255,255,255),(250,375),(375,500),1)
    pygame.draw.line(windows,(255,255,255),(250,400),(350,500),1)
    pygame.draw.line(windows,(255,255,255),(250,425),(325,500),1)
    pygame.draw.line(windows,(255,255,255),(250,450),(300,500),1)
    pygame.draw.line(windows,(255,255,255),(250,475),(275,500),1)

    #cuadro 11
    pygame.draw.line(windows,(255,255,255),(525,350),(400,475),1)
    pygame.draw.line(windows,(255,255,255),(500,350),(400,450),1)
    pygame.draw.line(windows,(255,255,255),(475,350),(400,425),1)
    pygame.draw.line(windows,(255,255,255),(450,350),(400,400),1)
    pygame.draw.line(windows,(255,255,255),(425,350),(400,375),1)
    pygame.draw.line(windows,(255,255,255),(550,350),(400,500),5)
    pygame.draw.line(windows,(255,255,255),(550,375),(425,500),1)
    pygame.draw.line(windows,(255,255,255),(550,400),(450,500),1)
    pygame.draw.line(windows,(255,255,255),(550,425),(475,500),1)
    pygame.draw.line(windows,(255,255,255),(550,450),(500,500),1)
    pygame.draw.line(windows,(255,255,255),(550,475),(525,500),1)

    #cuadro 12
    pygame.draw.line(windows,(255,255,255),(675,350),(700,375),1)
    pygame.draw.line(windows,(255,255,255),(650,350),(700,400),1)
    pygame.draw.line(windows,(255,255,255),(625,350),(700,425),1)
    pygame.draw.line(windows,(255,255,255),(600,350),(700,450),1)
    pygame.draw.line(windows,(255,255,255),(575,350),(700,475),1)
    pygame.draw.line(windows,(255,255,255),(550,350),(700,500),5)
    pygame.draw.line(windows,(255,255,255),(550,375),(675,500),1)
    pygame.draw.line(windows,(255,255,255),(550,400),(650,500),1)
    pygame.draw.line(windows,(255,255,255),(550,425),(625,500),1)
    pygame.draw.line(windows,(255,255,255),(550,450),(600,500),1)
    pygame.draw.line(windows,(255,255,255),(550,475),(575,500),1)

    #cuadro 13
    pygame.draw.line(windows,(255,255,255),(225,500),(250,525),1)
    pygame.draw.line(windows,(255,255,255),(200,500),(250,550),1)
    pygame.draw.line(windows,(255,255,255),(175,500),(250,575),1)
    pygame.draw.line(windows,(255,255,255),(150,500),(250,600),1)
    pygame.draw.line(windows,(255,255,255),(125,500),(250,625),1)
    pygame.draw.line(windows,(255,255,255),(100,500),(250,650),5)
    pygame.draw.line(windows,(255,255,255),(100,525),(225,650),1)
    pygame.draw.line(windows,(255,255,255),(100,550),(200,650),1)
    pygame.draw.line(windows,(255,255,255),(100,575),(175,650),1)
    pygame.draw.line(windows,(255,255,255),(100,600),(150,650),1)
    pygame.draw.line(windows,(255,255,255),(100,625),(125,650),1)

    #cuadro 14
    pygame.draw.line(windows,(255,255,255),(275,500),(250,525),1)
    pygame.draw.line(windows,(255,255,255),(300,500),(250,550),1)
    pygame.draw.line(windows,(255,255,255),(325,500),(250,575),1)
    pygame.draw.line(windows,(255,255,255),(350,500),(250,600),1)
    pygame.draw.line(windows,(255,255,255),(375,500),(250,625),1)
    pygame.draw.line(windows,(255,255,255),(400,500),(250,650),5)
    pygame.draw.line(windows,(255,255,255),(400,525),(275,650),1)
    pygame.draw.line(windows,(255,255,255),(400,550),(300,650),1)
    pygame.draw.line(windows,(255,255,255),(400,575),(325,650),1)
    pygame.draw.line(windows,(255,255,255),(400,600),(350,650),1)
    pygame.draw.line(windows,(255,255,255),(400,625),(375,650),1)

    #cuadro 15
    pygame.draw.line(windows,(255,255,255),(525,500),(550,525),1)
    pygame.draw.line(windows,(255,255,255),(500,500),(550,550),1)
    pygame.draw.line(windows,(255,255,255),(475,500),(550,575),1)
    pygame.draw.line(windows,(255,255,255),(450,500),(550,600),1)
    pygame.draw.line(windows,(255,255,255),(425,500),(550,625),1)
    pygame.draw.line(windows,(255,255,255),(400,500),(550,650),5)
    pygame.draw.line(windows,(255,255,255),(400,525),(525,650),1)
    pygame.draw.line(windows,(255,255,255),(400,550),(500,650),1)
    pygame.draw.line(windows,(255,255,255),(400,575),(475,650),1)
    pygame.draw.line(windows,(255,255,255),(400,600),(450,650),1)
    pygame.draw.line(windows,(255,255,255),(400,625),(425,650),1)

    #cuadro 16
    pygame.draw.line(windows,(255,255,255),(575,500),(550,525),1)
    pygame.draw.line(windows,(255,255,255),(600,500),(550,550),1)
    pygame.draw.line(windows,(255,255,255),(625,500),(550,575),1)
    pygame.draw.line(windows,(255,255,255),(650,500),(550,600),1)
    pygame.draw.line(windows,(255,255,255),(675,500),(550,625),1)
    pygame.draw.line(windows,(255,255,255),(700,500),(550,650),5)
    pygame.draw.line(windows,(255,255,255),(700,525),(575,650),1)
    pygame.draw.line(windows,(255,255,255),(700,550),(600,650),1)
    pygame.draw.line(windows,(255,255,255),(700,575),(625,650),1)
    pygame.draw.line(windows,(255,255,255),(700,600),(650,650),1)
    pygame.draw.line(windows,(255,255,255),(700,625),(675,650),1)





#Figura_Robot()
#Figura_Casa()
#Figura_3()
#figura_cuatro()


pygame.display.update()
time.sleep(5)
