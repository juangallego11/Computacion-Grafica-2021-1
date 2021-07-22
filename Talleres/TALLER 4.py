#GALLEGO RANGEL JUAN DAVID 
#1112627876

import math
import numpy as np
import matplotlib.pyplot as plt
import sys 

#-----------------------
#CargarImagen

from skimage import io 
from skimage import exposure
from PIL import Image
import PIL.ImageOps
#-----------------------

imagen = io.imread("bart.jpg")/255.0
ima_1 = io.imread("rsz.jpg")
ima_2 = io.imread("rsz.jpg")
imag_blanco = io.imread("Blanco.jpg")
imag_blanco2 = io.imread("Blanco.jpg")

#------------------------
#1 Elaborar un procedimiento que diseñe la siguiente matriz
#cyan
for i in range(0, 100):#fila
	for j in range(0, 100):	#columnas	
		imag_blanco[i, j, 0] = 1
#rojo
for i in range(0, 100):
	for j in range(200, 300):
		imag_blanco[i, j, 1] = 0
		imag_blanco[i, j, 2] = 0
#magenta
for i in range(100, 200):
	for j in range(0, 100):		
		imag_blanco[i, j, 1] = 1
#amarillo
for i in range(200, 300):
	for j in range(0, 100):		
		imag_blanco[i, j, 2] = 1
#negro
for i in range(200, 300):
	for j in range(100, 200):		
		imag_blanco[i, j, 0] = 1
		imag_blanco[i, j, 1] = 1
		imag_blanco[i, j, 2] = 1
#azul
for i in range(200, 300):
	for j in range(200, 300):
		imag_blanco[i, j, 0] = 0
		imag_blanco[i, j, 1] = 0
#verde
for i in range(100, 200):
	for j in range(200, 300):
		imag_blanco[i, j, 0] = 0
		imag_blanco[i, j, 2] = 0
#gris
for i in range(100, 200):
	for j in range(100, 200):
		imag_blanco[i, j, 0] = imag_blanco[i, j, 0] * 0.5
		imag_blanco[i, j, 1] = imag_blanco[i, j, 1] * 0.5
		imag_blanco[i, j, 2] = imag_blanco[i, j, 2] * 0.5
#2 Realizar un procedimiento que diseñe la siguiente imagen a través de una matriz
#amarillo
for i in range(0, 250):
	for j in range(0, 30):		
		imag_blanco2[i, j, 2] = 1
#cyan
for i in range(0, 250):#fila
	for j in range(30, 90):	#columnas	
		imag_blanco2[i, j, 0] = 1
#verde
for i in range(0, 250):
	for j in range(90, 150):
		imag_blanco2[i, j, 0] = 0
		imag_blanco2[i, j, 2] = 0
#magenta
for i in range(0, 250):
	for j in range(150, 210):		
		imag_blanco2[i, j, 1] = 1
#rojo
for i in range(0, 250):
	for j in range(210, 270):
		imag_blanco2[i, j, 1] = 0
		imag_blanco2[i, j, 2] = 0
#azul
for i in range(0, 250):
	for j in range(270, 330):
		imag_blanco2[i, j, 0] = 0
		imag_blanco2[i, j, 1] = 0
#Grises
nor = 1.2
for h in np.arange(0, 360, 30):
	nor = nor - 0.1
	for i in range(250, 300):
		for j in range(h-30, h):
			imag_blanco2[i, j, 0] = imag_blanco2[i, j, 0] * nor
			imag_blanco2[i, j, 1] = imag_blanco2[i, j, 1] * nor
			imag_blanco2[i, j, 2] = imag_blanco2[i, j, 2] * nor
#3 Elaborar una función que invierta los colores de una imagen
def Invert(iman):
	imagen1 = np.copy(imagen*0.255)
	imagen_i = 255 - imagen_i
	return imagen1
#4 Elaborar una función a la que se le envie de una imagen retorne su capa Roja
def capaRoja(iman):
	imagen_r = np.copy(imagen)
	imagen_r[:,:,1] = 0
	imagen_r[:,:,2] = 0
	return imagen_r
#5 Elaborar una función a la que se le envie de una imagen retorne su capa Verde
def capaVerde(iman):
	imagen_V = np.copy(imagen)
	imagen_V[:,:,0] = 0
	imagen_V[:,:,2] = 0
	return imagen_V
#6 Elaborar una función a la que se le envié de una imagen retorne su capa Azul
def capaAzul(iman):
	imagen_A = np.copy(imagen)
	imagen_A[:,:,0] = 0
	imagen_A[:,:,1] = 0
	return imagen_A
#7 Elaborar una función a la que se le envié de una imagen y retorne la imagen en Magenta
def capaMag(iman):
	imagen_ = np.copy(imagen)
	imagen_[:,:,0] = 1
	imagen_[:,:,2] = 1
	return imagen_
#8Elaborar una función a la que se le envié de una imagen y retorne la imagen en Cyan
def capaCyan(iman):
	imagen_ = np.copy(imagen)
	imagen_[:,:,1] = 1
	imagen_[:,:,2] = 1
	return imagen_
#9 Elaborar una función a la que se le envié de una imagen y retorne la imagen en Amarillo
def capaAmarillo(iman):
	imagen_ = np.copy(imagen)
	imagen_[:,:,0] = 1
	imagen_[:,:,1] = 1
	return imagen_
#10 Elaborar una función en  la que le envie por separado las capas RGB y con base en ellas reconstruya la imagen en colores
def recon(R, G, B):
	original = R + G + B
	return original
#11 Elaborar una función a la que se le envié 2 imágenes y que me retorne la fusión de las dos imágenes sin ecualizar
def fus_sin(ima1, ima2):
	hola = ima_1 + ima_2
	return hola
#12Elaborar una función a la que se le envié 2 imágenes y que me retorne la fusión de las dos imágenes ecualizadas
def fus_con(ima1, ima2):
	hola = ima_1 + ima_2
	hola1 = exposure.equalize_adapthist(hola, clip_limit=0.5)
	return hola1
#13. Elaborar una función a la que se le envie una imagen y un factor y retorne la imagen ecualizada según el factor
def ecual(ima, factor):
	return ima*factor
#14. Elaborar una función a la que se le envie una imagen y que retorne la imagen con la Técnica de promedio (Average)
def average(R,G,B):
	imagen_gris_av = ((R+G+B)/3)
	return (imagen_gris_av)
#15. Elaborar una función a la que se le envié una imagen y que retorne la imagen en escala de grises con la técnica de promedio (Average)
def grises_average(R,G,B):
	imagen_gris_av = ((R+G+B)/3)*0.3
	return (imagen_gris_av)
#16. Elaborar una función a la que se le envié una imagen y que retorne la imagen en escala de grises con latécnica de Luminosidad (Luminosity)
def grises_luminoso(R,G,B):
	imagen_gris_lm = (((0.2989*R)+(0.5870*G)+(0.1140*B))/3)
	return (imagen_gris_lm)
#17. Elaborar una función a la que se le envié una imagen y que retorne la imagen en escala de grisescon latécnica de La tonalidad (Midgray)
def grises_midgray(R,G,B):
 	maximo = np.maximum(R, G, B)
 	minimo = np.minimum(R, G, B)
 	imagen_gris_md = (maximo + minimo) / 2
 	return (imagen_gris_md)

imagen_gris = np.copy(imagen)
R = imagen_gris[:,:,0]
G = imagen_gris[:,:,1]
B = imagen_gris[:,:,2]

average = grises_average(R,G,B)
luminoso = grises_luminoso(R,G,B)
mydgray = grises_midgray(R,G,B)

plt.figure("Imagen")
#plt.subplot(221)
#plt.imshow(Invert(imagen))
#plt.imshow(capaRoja(ima_1))
#plt.imshow(recon(R,G,B))
#plt.subplot(222)
#plt.imshow(capaVerde(ima_1))
#plt.imshow(fus_con(ima_1, ima_2))
#plt.subplot(223)
#plt.imshow(capaAzul(ima_1))
#plt.imshow(ecual(imagen,0.9))
#plt.subplot(224)
#plt.imshow(recon(R,G,B))
#plt.imshow(capaCyan(ima_1))
#plt.imshow(fus_sin(ima_1, ima_2))
#plt.imshow(mydgray)

#plt.imshow(imag_blanco)
plt.imshow(imag_blanco2)
plt.show()