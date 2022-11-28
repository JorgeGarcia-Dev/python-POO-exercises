"""
Desarrollar un programa que cargue los datos de un triángulo. Implementar una clase con los métodos para inicializar los atributos,
imprimir el valor del lado con un tamaño mayor y  el tipo de triángulo que es (equilátero, isósceles o escaleno).
"""

# Con esta función, validamos que los datos que ingresa el usuario, son de tipo int().
def validar_numeros(message):

    while True:
        try:
            data = int(input("Ingresa " + message))
            return data
        except ValueError:
            print("El dato debe ser número entero.")

# Definimos la clase Triángulo.
class Triangulo:

    # Iniciamos y establecemos los atributos nombre y edad con el método __init__ (self no es más que el objeto Triangulo).
    def __init__(self, base, lado_a, lado_b):

        # El parámetro self se refiere al objeto instanciado de esa clase sobre el cual se está invocando dicho método.
        self.base = base
        self.lado_a = lado_a
        self.lado_b = lado_b

    # Definimos el método el_mayor_es, aquí condicionamos todas las posibles variables de las medidas de el triángulo.
    def el_mayor_es(self):

        if self.base == self.lado_a and self.base == self.lado_b and self.lado_a == self.lado_b:
            print("Todos los lados son iguales.")

        elif (self.base == self.lado_a) and (self.base > self.lado_b and self.lado_a > self.lado_b):
            print("Los lados mayores son la base y el lado_a.")

        elif (self.base == self.lado_b) and (self.base > self.lado_a and self.lado_b > self.lado_a):
            print("Los lados mayores son la base y el lado_b.")

        elif (self.lado_a == self.lado_b) and (self.lado_a > self.base and self.lado_b > self.base):
            print("Los lados mayores son el lado_a y el lado_b.")

        elif self.lado_b > self.base and self.lado_b > self.lado_a:
            print("El lado con mayor tamaño es el lado_b.")

        elif self.lado_a > self.base and self.lado_a > self.lado_b:
            print("El lado con mayor tamaño es el lado_a.")

        elif self.base > self.lado_a and self.base > self.lado_b:
            print("El lado con mayor tamaño es la base.")

    # Definimos el método comparar_medidas, aquí determinamos que tipo de triángulo es: Equilatero, Isóseles o Escaleno.
    def comparar_medidas(self):

        if self.base == self.lado_a and self.lado_a == self.lado_b:
            print("El triángulo es equilátero.")

        if ((self.base != self.lado_a and self.base != self.lado_b) or (self.lado_a != self.base and self.lado_a != self.lado_b) or (self.lado_b != self.base and self.lado_b != self.lado_a)) and (self.lado_a == self.lado_b or self.base == self.lado_a or self.base == self.lado_b):
            print("El triángulo es isósceles.")

        if self.base != self.lado_a and self.base != self.lado_b and self.lado_a != self.lado_b:
            print("El triángulo es escaleno.")

# Por medio de variables, recibimos las medidas de cada lado del triángulo.
int_base = validar_numeros("la medida de la base del triángulo: ")
int_lado_a = validar_numeros("la medida del lado_a del triángulo: ")
int_lado_b = validar_numeros("la medida del lado_b del triángulo: ")

# Enviamos los valores de las medidas para los parámetros base, lado_a y lado_b.
medidas = Triangulo(int_base, int_lado_a, int_lado_b)

# Invocamos los métodos de la clase Triangulo.
medidas.el_mayor_es()
medidas.comparar_medidas()