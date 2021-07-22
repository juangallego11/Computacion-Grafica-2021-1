import math
import numpy as np
import matplotlib.pyplot as plt

def factorial(n):
	if n==0 or n==1:
		resultado=1.
	elif n>1:
		resultado=n*factorial(n-1)
	else:
		return "NaN"
	return resultado

def misin(x):
	suma=0
	termino=0
	n=0
	apotemin=0.00001
	while (True):
		termino = (pow(-1,n))/(factorial(2*n+1))*pow(x,(2*n+1))
		suma=suma+termino
		n=n+1
		if (math.fabs(termino)<apotemin):
			break
	return(suma)

def micos(x):
	suma=0
	termino=0
	n=0
	apotemin=0.00001
	while (True):
		termino=(pow(-1,n))/(factorial(2*n))*pow(x,(2*n))
		suma=suma+termino
		n=n+1
		if (math.fabs(termino)<apotemin):
			break
	return(suma)

def mitan(x):
	suma = misin(x)/micon(x)
	return(suma)


#prueba = factorial(5)
#print(prueba)

print(misin(0.5))

print(micos(0))