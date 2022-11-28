"""
Realizar un programa que tenga una clase Persona con las siguientes características.
La clase tendrá como atributos el nombre y la edad de una persona.
Implementar los métodos necesarios para inicializar los atributos,
mostrar los datos e indicar si la persona es mayor de edad o no.
"""

# Definimos la clase Persona.
class Persona:
    
    # Iniciamos y establecemos los atributos nombre y edad con el método __init__ (self no es más que el objeto Persona).
    def __init__(self, nombre, edad):
        
        # El parámetro self se refiere al objeto instanciado de esa clase sobre el cual se está invocando dicho método.
        self.nombre = nombre
        self.edad = edad
    
    # Definimos el método mayor, aquí condicionamos por medio de if que si la edad es mayor o igual a 18, es mayor de edad,
    # En caso contrario, es menor de edad.
    def mayor(self):
        
        if self.edad >= 18:
            print(self.nombre, "Es mayor de edad.")
        else:
            print(self.nombre, "Es menor de edad.")

# Por medio de una variable, envíamos los valores de los parámetros de nombre y edad.
persona_1 = Persona('Jorge', 38)
persona_2 = Persona('Alejandro', 15)

# Invocamos los métodos de la clase para cada persona.
persona_1.mayor()
persona_2.mayor()