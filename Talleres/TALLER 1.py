#TALLER 1
#Juan D Gallego R

import numpy as np
from statistics import mode

#1 Cree un vector A={2,3,5,1,4,7,9,8,6,10}

a=np.array([2,3,5,1,4,7,9,8,6,10])
print(a)

#2 Cree un vector B que contenga los elementos desde el 11hasta el 20 (utilice subscripts
b= np.arange(10)
print(b)

#3 Componer un vector C formado por los vectores A y B en la misma fila respectivamente.
c=np.concatenate([a,b])
print ("Vector c ",c)

#4 Encuentre el valor mínimo en el vector C haciendo uso de lafunción propia de Numpy.
print(np.amin(c))

#5 Encuentre el valor máximo en el vector C haciendo uso de la función propia de Numpy.
print(np.amax(c))

#6 Encuentre la longitud en el vector C haciendo uso de la función propia de Numpy.
print(np.size(c))

#7 Encuentre la suma de los elementos el vector C haciendo uso de la función propia de Numpy.
print("Suma del vector c ",np.sum(c))

#8 Encuentre el promedio de los elementos en el vector C haciendo uso de las operaciones elementales suma y división.
print("Promedio del vector c ",np.sum(c)/np.size(c))

#9 Encuentre el promedio en el vector C haciendo uso de la función propia de Numpy.
print("Promedio del vector c ",np.mean(c))

#10  Encuentre la media en el vector C haciendo uso de la función propia de Numpy.
print("Media del vector c ",np.median(c))

#11 Encuentre la suma en el vector C haciendo uso de la función propia de Numpy.
print("Suma vector c ",np.sum(c))

#12 Cree un vector D a partir del vector C con los elementos mayores que 5.
d=[]
for i in range (0,np.size(c)):
    if (c[i]>=5):
        d.append(c[i])
print("Mayores que 5 ",d)

#13 Cree un vector E a partir del vector C con los elementos mayores que 5 y menores que 15.
e=[]
for i in range (0,np.size(c)):
    if ((c[i] >= 5) and (c[i]<= 15)):
        e.append(c[i])
print("Mayores que 5 y Menores que 15 del vec c",e)

#14 Cambie los elementos 5 y 15 elemento del vector C por ‘7'
for i in range (0,np.size(c)):
    if ((c[i]==5) or (c[i]==15) ):
        c[i]=7
print("Vector c sin 15 ni 5 ",c)

#15 Determine la moda del vector C.
print("Moda del vector c ", mode(c))

#16 Ordene el Vector C de menor a mayor
c.sort()
print("Ordenamiento del vector c ", c)

#17 Multiplique el vector C por 10
print("Multiplicar por 2 ",c*2)

#18 Cambie los elementos del 6 al 8 de la matriz C por 60, 70 y80 respectivamente
c[6]=60
c[7]=70
c[8]=80
print("cambio de los elementos",c)

#19 Cambie los elementos del 14 al 16 de la matriz C por 140, 150 y 160 respectivamente.
c[14]=140
c[15]=150
c[16]=160
print(" segundo cambio de elementos en c ",c)


