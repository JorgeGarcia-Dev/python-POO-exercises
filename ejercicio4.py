"""
Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el método __init__.
Calcular después la suma, resta, multiplicación y división.
Utilizar un método para cada una e imprimir los resultados obtenidos.
Llamar a la clase Calculadora.
"""

def validar_numeros(message):

    while True:
        try:
            data = int(input("Ingresa " + message))
            return data
        except ValueError:
            print("El dato debe ser número entero.")

class Calculadora:
    
    def __init__(self, num_1, num_2):
        
        self.num_1 = num_1
        self.num_2 = num_2
    
    def suma(self):
        
        suma = self.num_1 + self.num_2
        print("El resultado de la suma es: ", suma)
        
    def resta(self):
        
        resta = self.num_1 - self.num_2
        print("El resultado de la resta es: ", resta)
        
    def division(self):
        
        division = self.num_1 / self.num_2
        print("El resultado de la división es: ", division)
        
    def multiplicacion(self):
        
        multiplicacion = self.num_1 * self.num_2
        print("El resultado de la multiplicación es: ", multiplicacion)

int_num_1 = validar_numeros("el primer número: ")
int_num_2 = validar_numeros("el segundo número: ")

suma = Calculadora(int_num_1, int_num_2)
resta = Calculadora(int_num_1, int_num_2)
division = Calculadora(int_num_1, int_num_2)
multiplicacion = Calculadora(int_num_1, int_num_2)

suma.suma()
resta.resta()
division.division()
multiplicacion.multiplicacion()