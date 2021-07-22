import numpy as np
import math

##1
m=np.array([[0,2,4,6],[0,3,5,7]])
np.savetxt("matriz.mat", m)
print(m)
del m
n=np.loadtxt("matriz.mat")
print(n[1][3])
print(n[0:2,0:2])

##2
a=np.array([[1,3,5,8],[2,6,5,3],[4,1,9,7],[1,8,0,2]])
b=np.array([[1,9,5,8],[12,5,5,9],[4,2,9,74],[0,6,0,3]])
c=np.array([[1,9],[10,2] ])

##3*A
print(a)
print(3*a)

##A-7
print(a)
print(a-7)

##A*B
print(" a*b " ,a*b)

##A^-1
print(np.linalg.inv(a))

##B^-1
print(np.linalg.inv(b))