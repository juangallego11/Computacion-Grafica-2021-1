#JUAN DAVID GALLEGO CC 1112627876


from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk,Image 
from tkinter.filedialog import askopenfile 
import numpy as np
from skimage import io
from FUNCIONES import * 

'''VENTANA TITLE'''
ventana=Tk()
ventana.title("VISOR DE IMAGENES")
ventana.geometry("600x500")

'''DECLARACION DE VARIABLES'''
Mibrillo=IntVar(value=0)
MiContraste=IntVar(value=0)
seleccion = IntVar(value=1) 

RED=IntVar()
GREEN=IntVar()
BLUE=IntVar()

CYAN=IntVar()
MAGENTA=IntVar()
YELLOW=IntVar()
KEY=IntVar()

imageio=np.zeros((20,30))
imagen_contraste=np.copy(imageio)
imagen_brillo=np.copy(imageio)
imagen_negativa=np.copy(imageio)
imagen_binarizada=np.copy(imageio)
imagen_grises=np.copy(imageio)

r=np.copy(imageio)
g=np.copy(imageio)
b=np.copy(imageio)
c=np.copy(imageio)
m=np.copy(imageio)
y=np.copy(imageio)
k=np.copy(imageio)

'''LINEA DE CODIGO PARA RUTA DE LA IMAGEN
OBS: La ruta cambia dependiendo de donde esten las imagenes que quiera probar'''

def obtenerRuta():
    Ruta=RutaImagen.get()
    Tipo=comboboxTipoImagen.get()
    ruta="C:/Users/fbdav/Desktop/UTP/COMPUTACION GRAFICA/Talleres/"+Ruta+'.'+Tipo
    return ruta

'''LINEA DE CODIGO QUE CARGA IMAGEN EN VENTANA'''
def cargar():  
    imagen =Image.open(obtenerRuta())
    imagen =imagen.resize((300, 400), Image.ANTIALIAS)
    imgCarga = ImageTk.PhotoImage(imagen)
    etiqueta.configure(image=imgCarga)
    ventana.mainloop()

'''FUNCION PRINCIPAL ACTUALIZAR QUE CONTIENE LAS FUNCIONES DEL ARCHIVO Funciones.py'''
def actualizar():
    imageio = io.imread(obtenerRuta())
    TipoImagen=comboboxTipo.get()
    imagen=np.copy(imageio)
    if(TipoImagen=="Original"):
        imagen_brillo=Brillo(imageio,Mibrillo.get())
        imagen_contraste=Contraste(imageio,MiContraste.get(),seleccion.get())
        imagen=imagen_brillo+imagen_contraste
    if(TipoImagen=="Invertir"):
        imagen_brillo=Brillo(imageio,Mibrillo.get())
        imagen_contraste=Contraste(imageio,MiContraste.get(),seleccion.get())
        imagen=imagen_brillo+imagen_contraste
        imagen_negativa=InvertirImagen(imagen)
        imagen=imagen_negativa
    if(TipoImagen=="Escala de grises"):
        imagen_brillo=Brillo(imageio,Mibrillo.get())
        imagen_contraste=Contraste(imageio,MiContraste.get(),seleccion.get())
        imagen=imagen_brillo+imagen_contraste
        imagen_grises=AverageGris(imagen)
        imagen=imagen_grises
    if(TipoImagen=="Binarizada"):
        imagen_brillo=Brillo(imageio,Mibrillo.get())
        imagen_contraste=Contraste(imageio,MiContraste.get(),seleccion.get())
        imagen=imagen_brillo+imagen_contraste
        imagen_binarizada=Binarizar(imagen,127.5)
        imagen=imagen_binarizada
    if(RED.get()==1):
        imagen_brillo=Brillo(imageio,Mibrillo.get())
        imagen_contraste=Contraste(imageio,MiContraste.get(),seleccion.get())
        imagen=imagen_brillo+imagen_contraste
        r=Rojo(imagen)
        imagen=r
    if(GREEN.get()==1):
        imagen_brillo=Brillo(imageio,Mibrillo.get())
        imagen_contraste=Contraste(imageio,MiContraste.get(),seleccion.get())
        imagen=imagen_brillo+imagen_contraste
        g=Verde(imagen)
        imagen=g
    if(BLUE.get()==1):
        imagen_brillo=Brillo(imageio,Mibrillo.get())
        imagen_contraste=Contraste(imageio,MiContraste.get(),seleccion.get())
        imagen=imagen_brillo+imagen_contraste
        b=Azul(imagen)
        imagen=b
    if(CYAN.get()==1):
        imagen_brillo=Brillo(imageio,Mibrillo.get())
        imagen_contraste=Contraste(imageio,MiContraste.get(),seleccion.get())
        imagen=imagen_brillo+imagen_contraste        
        c=Cian(imagen)
        imagen=c
    if(MAGENTA.get()==1):
        imagen_brillo=Brillo(imageio,Mibrillo.get())
        imagen_contraste=Contraste(imageio,MiContraste.get(),seleccion.get())
        imagen=imagen_brillo+imagen_contraste
        m=Magenta(imagen)
        imagen=m
    if(YELLOW.get()==1):
        imagen_brillo=Brillo(imageio,Mibrillo.get())
        imagen_contraste=Contraste(imageio,MiContraste.get(),seleccion.get())
        imagen=imagen_brillo+imagen_contraste
        y=Amarillo(imagen)
        imagen=y
    if(KEY.get()==1):
        imagen_brillo=Brillo(imageio,Mibrillo.get())
        imagen_contraste=Contraste(imageio,MiContraste.get(),seleccion.get())
        imagen=imagen_brillo+imagen_contraste
        k=Negro(imagen)
        imagen=k
    if(RED.get()==1 and BLUE.get()==1 and GREEN.get()==1):
        imagen=r+g+b
    if(CYAN.get()==1 and MAGENTA.get()==1 and YELLOW.get()==1 and KEY.get()==1):
        imagen=c+m+y+k 
    actualizarLabel(imagen) #ACTUALIZAMOS EL LABEL CON LA NUEVA IMAGEN MODIFICADA

'''METODO QUE ACTUALIZA A LA IMAGEN MODIFICADA'''

def actualizarLabel(imagen):
    imagen =Image.fromarray(np.uint8(imagen))
    imagen =imagen.resize((300, 400), Image.ANTIALIAS)
    imgCarga = ImageTk.PhotoImage(imagen)
    etiqueta.configure(image=imgCarga)
    ventana.mainloop()


def callbackFunc(event):
    actualizar()
    
'''BTN CARGAR IMAGEN'''

RutaImagen= Entry(ventana,width=20)
RutaImagen.place(x=12,y=15)
CargarImagen=Button(ventana,text="Cargar imagen", command=cargar).place(x=200,y=14) #TOMA LA RUTA QUE LE PASAMOS DE LA IMAGEN

'''BTN ACTUALIZAR'''

ActualizarImagen=Button(ventana,text="Actualizar imagen",command=actualizar) #TOMA LOS CAMBIOS Y LOS APLICA A LA IMAGEN
ActualizarImagen.place(x=400,y=200)

'''SPINNER BRILLO Y CONTRASTE'''

SpinnerBrillo=Spinbox(ventana,from_=0,to=100,width=10,textvariable=Mibrillo,command=actualizar).place(x=400,y=60) #INCREMENTA EL VALOR DEL BRILLO
SpinnerContraste=Spinbox(ventana,from_=0,to=100,width=10,textvariable=MiContraste,command=actualizar).place(x=400,y=80) #INCREMENTA EL VALOR DEL CONTRASTE

'''TITULOS BTNS'''

Labelbrillo=Label(ventana,width=10,text="Mi brillo").place(x=320,y=60)
LabelContraste=Label(ventana,width=10,text="contraste").place(x=320,y=80)
LabelTipoImagen=Label(ventana,width=12,text="Tipo imagen").place(x=320,y=120)
LabelCanalesRGB=Label(ventana,width=12,text="Canales RGB").place(x=320,y=150)
LabelCanalesCMYK=Label(ventana,width=15,text="Canales CMYK").place(x=320,y=170)

'''BTN ZONAS CLARAS'''

RadioClaro = Radiobutton(ventana, text='zonas claras', value=1, variable=seleccion, width=12)
RadioClaro.place(x=320,y=100)

'''BTN ZONAS OSCURAS'''

RadioOscuro = Radiobutton(ventana, text='zonas oscuras', value=2, variable=seleccion, width=12).place(x=410,y=100)

'''FORMATO IMAGEN'''
comboboxTipoImagen=Combobox(ventana,value=('jpg','gif','png'),width=5,state="readonly")
comboboxTipo=Combobox(ventana,value=('Original','Invertir','Escala de grises','Binarizada'),width=15,state="readonly")
comboboxTipo.current(0)
comboboxTipo.place(x=400,y=125)
comboboxTipo.bind("<<ComboboxSelected>>", callbackFunc)
comboboxTipoImagen.place(x=140,y=15)

'''CHECK RGB'''

checkRed=Checkbutton(ventana,text="R", variable=RED, width=15).place(x=400,y=150)
checkGreen=Checkbutton(ventana,text="G", variable=GREEN, width=15).place(x=440,y=150)
checkBlue=Checkbutton(ventana,text="B", variable=BLUE, width=15).place(x=480,y=150)

'''CHECK CYAN'''

checkCyan=Checkbutton(ventana,text="C", variable=CYAN, width=15).place(x=400,y=170)
checkMagenta=Checkbutton(ventana,text="M", variable=MAGENTA, width=15).place(x=440,y=170)
checkYellow=Checkbutton(ventana,text="Y", variable=YELLOW, width=15).place(x=480,y=170)
checkKey=Checkbutton(ventana,text="K", variable=KEY, width=15).place(x=520,y=170)

etiqueta=Label(image="")
etiqueta.place(x=4, y=40)



ventana.mainloop()

