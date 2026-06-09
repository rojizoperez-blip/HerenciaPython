
class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def comer(self):
        print(f"{self.nombre} está comiendo.")

    def describir(self):
        print(f"Soy {self.nombre} y tengo {self.edad} años.")



class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)  
        self.raza = raza

    def ladrar(self):
        print(f"{self.nombre} dice: ¡Guau!")

    def describir(self):  
        super().describir()
        print(f"Soy un perro de raza {self.raza}.")


mi_perro = Perro("Rex", 3, "Labrador")

mi_perro.describir()   
mi_perro.comer()       
mi_perro.ladrar()      