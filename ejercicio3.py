"""
Desarrollar un programa que cargue los datos de un triángulo. Implementar una clase con los métodos para inicializar los atributos,
imprimir el valor del lado con un tamaño mayor y  el tipo de triángulo que es (equilátero, isósceles o escaleno).
"""

def validar_numeros(message):

    while True:
        try:
            data = int(input("Ingresa " + message))
            return data
        except ValueError:
            print("El dato debe ser número entero.")

class Triangulo:

    def __init__(self, base, lado_a, lado_b):

        self.base = base
        self.lado_a = lado_a
        self.lado_b = lado_b

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

    def comparar_medidas(self):

        if self.base == self.lado_a and self.lado_a == self.lado_b:
            print("El triángulo es equilátero.")

        if ((self.base != self.lado_a and self.base != self.lado_b) or (self.lado_a != self.base and self.lado_a != self.lado_b) or (self.lado_b != self.base and self.lado_b != self.lado_a)) and (self.lado_a == self.lado_b or self.base == self.lado_a or self.base == self.lado_b):
            print("El triángulo es isósceles.")

        if self.base != self.lado_a and self.base != self.lado_b and self.lado_a != self.lado_b:
            print("El triángulo es escaleno.")


int_base = validar_numeros("la medida de la base del triángulo: ")
int_lado_a = validar_numeros("la medida del lado_a del triángulo: ")
int_lado_b = validar_numeros("la medida del lado_b del triángulo: ")

medidas = Triangulo(int_base, int_lado_a, int_lado_b)

medidas.el_mayor_es()
medidas.comparar_medidas()