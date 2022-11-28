"""
Realizar un programa que tenga una clase Persona con las siguientes características.
La clase tendrá como atributos el nombre y la edad de una persona.
Implementar los métodos necesarios para inicializar los atributos,
mostrar los datos e indicar si la persona es mayor de edad o no.
"""

class Persona:
    
    def __init__(self, nombre, edad):
        
        self.nombre = nombre
        self.edad = edad
    
    def mayor(self):
        
        if self.edad >= 18:
            print(self.nombre, "Es mayor de edad.")
        else:
            print(self.nombre, "Es menor de edad.")

persona_1 = Persona('Jorge', 38)
persona_2 = Persona('Alejandro', 15)

persona_1.mayor()
persona_2.mayor()