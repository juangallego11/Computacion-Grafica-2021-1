#Juan David Gallego 1112627876

import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import io

#Pregunta 1 Elaborar una función a la que se le envié de una imagen y un factor de
    #ajuste (permite aumentar o disminuir el brillo), la función debe
        #retornar la imagen con el brillo deseado de acuerdo al factor de ajust 2 Elaborar una función a la que se le envié de una imagen, el canal y un
            #factor de ajuste (permite aumentar o disminuir el brillo), la función debe retornar la imagen con el brillo deseado de acuerdo al canal y al factor de ajuste
def subimg(pos, title, img):
    grilla = int(str(22) + str(pos))

    plt.subplot( grilla )
    plt.title( title )
    plt.imshow( img )

def brillo(img, fac):
    return img * fac + (1 - fac)

imagen = io.imread('bart.jpg') / 255

con = np.copy( imagen )

subimg(1, 'Original', imagen)
subimg(2, 'Brillo 0.2', brillo( con, 0.2 ))
subimg(3, 'Brillo 0.5', brillo( con, 0.5 ))
subimg(4, 'Brillo 0.8', brillo( con, 0.8 ))

plt.show()

#Pregunta 2 Elaborar una función a la que se le envié de una imagen, el canal y un factor de ajuste (permite aumentar o disminuir el brillo), la función
#debe retornar la imagen con el brillo deseado de acuerdo al canal y al factor de ajuste
def subimg(pos, title, img):
    grilla = int(str(33) + str(pos))

    plt.subplot( grilla )
    plt.title( title )
    plt.imshow( img )

def brillo(img, fac):
    return img * fac + (1 - fac)

def canal(img, can, fac):
    img_2 = np.copy(img)
    for i in range(0,3):
        if i != can:
            img_2[:,:,i] = 0

    return brillo(img_2, fac)

imagen = io.imread('bart.jpg') / 255

imagen_2 = np.copy( imagen )

subimg(1, 'Canal Rojo - Brillo 0.2', canal( imagen_2, 0, 0.2 ))
subimg(2, 'Canal Rojo - Brillo 0.5', canal( imagen_2, 0, 0.5 ))
subimg(3, 'Canal Rojo - Brillo 0.8', canal( imagen_2, 0, 0.8 ))
subimg(4, 'Canal Verde - Brillo 0.2', canal( imagen_2, 1, 0.2 ))
subimg(5, 'Canal Verde - Brillo 0.5', canal( imagen_2, 1, 0.5 ))
subimg(6, 'Canal Verde - Brillo 0.2', canal( imagen_2, 1, 0.8 ))
subimg(7, 'Canal Azul - Brillo 0.2', canal( imagen_2, 2, 0.2 ))
subimg(8, 'Canal Azul - Brillo 0.5', canal( imagen_2, 2, 0.5 ))
subimg(9, 'Canal Azul - Brillo 0.8', canal( imagen_2, 2, 0.8 ))

plt.show()


#Pregunta 3 Elaborar una función a la que se le envié de una imagen y un factor de contraste, la función debe retornar la imagen con el contraste
#deseado de acuerdo al factor de contraste

def subimg(pos, title, img):
    grilla = int(str(22) + str(pos))

    plt.subplot( grilla )
    plt.title( title )
    plt.imshow( img )

def contra(img, fac):
    return img + fac

imagen = io.imread('rsz.jpg') / 255

con = np.copy( imagen )

subimg(1, 'Original', imagen)
subimg(2, 'Contraste 1', contra( con, 0.1 ))
subimg(3, 'Contraste 2', contra( con, 0.2 ))
subimg(4, 'Contraste 3', contra( con, 0.3 ))

plt.show()

#Pregunta 4 Elaborar una función que permita realizarle un zoom a una parte de la imagen

image = cv2.imread('rsz.jpg')
imageOut = image[60:220,280:480]

cv2.imshow('Imagen de entrada',image)
cv2.imshow('Imagen de salida',imageOut)
cv2.waitKey(0)

#Pregunta 5 Elaborar una función que permita binarizar una imagen

img = cv2.imread('rsz.jpg',0)
ret,var1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,var2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
 
titles = ['Imagen Original','Binarizada','Bina_Inv']
images = [img, var1, var2]
miArray = np.arange(3)
for i in miArray:
  plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
  plt.title(titles[i])
  plt.xticks([]),plt.yticks([])
 
plt.show()

#Pregunta 6 Elaborar una función que permita rotar una imagen
image = cv2.imread('bart.jpg')
ancho = image.shape[1] #columnas
alto = image.shape[0] # filas

# Rotación
M = cv2.getRotationMatrix2D((ancho//2,alto//2),45,1)
imageOut = cv2.warpAffine(image,M,(ancho,alto))

cv2.imshow('Imagen de entrada',image)
cv2.imshow('Imagen de salida',imageOut)
cv2.waitKey(0)

#Pregunta 7 Elaborar un procedimiento que permita sacar el histograma de cada una de las capas de una imagen

def Mihisto(imagen):
    image_histo = np.trunc(np.around(imagen *255,0))
    return (image_histo)
# Llamado histograma
image_histo = Mihisto(imagen)
plt.figure("Histograma")
plt.hist(image_histo.ravel(), 256, [0,256])
plt.show()