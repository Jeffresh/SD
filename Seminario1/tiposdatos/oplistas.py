#Operacioneslistas

#Se pueden concatenar con el operados "+"

lista1 = ["Uno", 2 ,3]
lista2 = [4, "Cinco", "Seis"]

print("Lista1: ", lista1)
print("Lista2: ",lista2)

lista3 = lista1+lista2
print("Lista3 resultante de la suma de las dos anteriores:  ", lista3)

#Podemos utilizar extend() para amplicar una lista existente ( otra forma de concatenar)

lista4 = [7,8,9]
print("Lista4: ", lista4)

lista3.extend(lista4)
print("Lista 3 resultante después de haber extendido de lista 4",lista3)

#Operador de busqueda "in" en una lista

print("Esta el entero 3 en la lista4? ", 3 in lista4)
print("Está la cadena 3 en la lista4?", "tres" in lista4)
print("Está el entero 10 en la lista4?", 10 in lista4)

# Operador += para añadir a una lista ya creada

print("Lista3: ", lista3)
lista3+=[10,11,"Doce"]
print("Lista3: ", lista3)

#Operador "*" funciona como repetidor en las listas, duplica la información ya almacenada X veces.

lista3 = lista3 * 2
print("Lista3:", lista3)


#Operador append(object) introduce un elemento al final de la lista

lista3.append(13)
print("lista3 después de append 11", lista3)

#Operador count(value) te dice el numero de ocurrencias que hay con el valor "value"

print("La lista tiene el numero 3: ", lista3.count(3), " veces.")
print("La lista tiene la cadena \"Doce\"", lista3.count("Doce"), " veces.")

#Operador instert(index,object) inserta el objeto en la posición index de la lista, decir que no reemplaza, es una lista, inserta el elemento en esa
#posicion y mueve todos los demás una hacia adelante.

print("Lista3: ",lista3)
lista3.insert(0,1)
print("Lista3 después de haber hecho insert(0,1): ", lista3)

#Operador remove(value) elimina LA PRIMERA ocurrencia de value en la lista3

print("Lista3: ",lista3)
lista3.remove(1)
print("Lista3 después de haber hecho remove(1): ",lista3)

#Operador pop(index), se obtiene el elemento en la posicion  index de la lista y se elimina.
#Si no se especifica un index, lo hace con el último elemento de la lista.

print("Lista3: ",lista3)
elemento1=lista3.pop(0)
print("Este es el primer elemento de la lista:", elemento1)
print("Lista3 resultante después de hacer pop(0):  ",lista3)


#Operador reverse(), invierte la lista CUIDADO se hace sobre la misma lista no sobre una copia.

print("Lista3: ",lista3)
lista3.reverse()
print("Lista3 después de haber hecho reverse() ",lista3)
lista3.reverse()

#Trabajando con rangos [Inicio,fin,salto]
lista3.insert(0,1)
print("Lista3: ",lista3[0:12:])
#Podemos acceder a los elementos en orden inverso utilizando el o "-" delante, se empieza en 1
#Como podemos observar el "fin" es un intervalo abierto, por lo tanto hacia atrás nos comemos un elemento, el problema de utilizar esto...
print("Lista3: ",lista3[11:0:-1])

#Listas por comprensión, operador range(value)

lista5 = range(10)
print("Lista5: ",lista5)
#Multiplicamos todos los numeros de la lista *2
lista5 = [2* x for x in range(10)]
print("Lista5: ", lista5)
#Podemos añadir criteros/condiciones SOBRE X por ejemplo solo multiplicar los X pares
lista5 = [2* x for x in range(10) if x % 2 == 0]
print("Lista5: ",lista5)

#Tuplas, las tuplas son listas constantes

#Podemos pasar de lista a tupla.
tupla = tuple(lista5)
print(tupla)
#print("Intentamos insetar en la tupla: )
#tupla.insert(0,1) ocurre un error.
#Tambien podemos pasar de tupla a lista.
tupla = tuple(range(10))
print(tupla)
lista6 = list(tupla)
print(lista6)
