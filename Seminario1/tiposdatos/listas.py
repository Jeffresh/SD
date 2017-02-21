# Son iguales que los arrays dinámicos de otros lenguajes, solo que te permiten almacenar elementos de distinto tipo.

lista = ["uno", "dos", "tres"]

lista

lista_mixta = ["uno", 2 , "tres"]

lista_mixta

#Son interables

for elemento in lista_mixta :
    print(elemento)

#Pueden ser accedidas y modificadas mediante un indice que empieza en 0

print(lista_mixta[2])
lista_mixta[2] = "tres"
print(lista_mixta[2])
