"""
Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el método __init__.
Calcular después la suma, resta, multiplicación y división.
Utilizar un método para cada una e imprimir los resultados obtenidos.
Llamar a la clase Calculadora.
"""

# Con esta función, validamos que los datos que ingresa el usuario, son de tipo int().
def validar_numeros(message):

    while True:
        try:
            data = int(input("Ingresa " + message))
            return data
        except ValueError:
            print("El dato debe ser número entero.")

# Definimos la clase Calculadora.
class Calculadora:

    # Iniciamos y establecemos los atributos nombre y edad con el método __init__ (self no es más que el objeto Calculadora).
    def __init__(self, num_1, num_2):

        # El parámetro self se refiere al objeto instanciado de esa clase sobre el cual se está invocando dicho método.
        self.num_1 = num_1
        self.num_2 = num_2

    # Definimos el método suma, en el cual sumamos num_1 + num_2
    def suma(self):

        suma = self.num_1 + self.num_2
        print("El resultado de la suma es: ", suma)

    # Definimos el método resta, en el cual restamos num_1 - num_2
    def resta(self):

        resta = self.num_1 - self.num_2
        print("El resultado de la resta es: ", resta)

    # Definimos el método division, en el cual dividimos num_1 / num_2
    def division(self):

        division = self.num_1 / self.num_2
        print("El resultado de la división es: ", division)

    # Definimos el método multiplicacion, en el cual multiplicamos num_1 * num_2
    def multiplicacion(self):

        multiplicacion = self.num_1 * self.num_2
        print("El resultado de la multiplicación es: ", multiplicacion)

# Por medio de variables, recibimos del usuario los valores de num_1 y num_2.
int_num_1 = validar_numeros("el primer número: ")
int_num_2 = validar_numeros("el segundo número: ")

# Enviamos los valores para los parámetros num_1 y num_2 para posteriormente heredarlos a los métodos: suma, resta, division y multiplicacion.
suma = Calculadora(int_num_1, int_num_2)
resta = Calculadora(int_num_1, int_num_2)
division = Calculadora(int_num_1, int_num_2)
multiplicacion = Calculadora(int_num_1, int_num_2)

# Invocamos los métodos de la clase Calculadora.
suma.suma()
resta.resta()
division.division()
multiplicacion.multiplicacion()