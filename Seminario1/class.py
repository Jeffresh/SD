class Person:

    def __init__(self,name):
        self.name = name

    def saluda(self):
        print("saludos de %s" %self.name)


Pepe = Person("Pepe")

Pepe.saluda()
