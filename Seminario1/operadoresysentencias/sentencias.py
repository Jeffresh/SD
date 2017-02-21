#Sentencias  incorpora una sentencia especial para indicar que no se debe realizar ninguna acción.
#Se trata de pass y especialmente útil cuando deseamos indicar que no se haga nada en una sentencia que requiere otra.

#pass cuando queremos indicar que no se haga nada, por ejemplo, crear una estructura que luego iremos rellenando.

for i  in range(10) :
    pass # sin este pass no nos dejaria hacer el print ya que nos daria error de identacion.

print("Despues del for")

#with  se utiliza con objetos que soportan el protocolo de manejador de contexto y garantiza que una o varias sentencias serán ejecutadas automáticamente.
#Esto nos ahorra muchas líneas de código, a la vez que nos garantiza que ciertas operaciones serán realizadas sin que lo indiquemos explícitamente

with open(r'texto.txt') as myfile :
    for line in myfile :
        print(line)
