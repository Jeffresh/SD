#Modulos, básicamente son lo mismo que #import en java o #include en c++

import math
#ahora podemos utilizar las funciones que hay en el fichero math

r = math.factorial(5)
print(r)

#Tambien podemos importar solamente partes de él y no todo el fichero, igual que en  java.
from math import factorial
#igual que con java hay que tener cuidado con las importaciones.

#Tambien podemos importarlo con nombres disintos

import math as fac

r = fac.factorial(5)
print(r)
