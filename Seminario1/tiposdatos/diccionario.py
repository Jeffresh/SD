#Diccionario: Asociacion de valor-clave. Van entre llaves.

dicc = { "Uno":1, "Dos": 2}
print(dicc)
print(dicc["Uno"])

print( "impresion solo de sus valores", dicc.values())

#Busqueda por clave
print("Tiene el valor 1?: " , "Uno" in dicc)
print("Tiene el valor 3?: ", "Tres" in dicc)

#Eliminar un valor, hace falta por fuerza un argumento ( una clave valida)
dicc.pop("Uno")
print(dicc)
