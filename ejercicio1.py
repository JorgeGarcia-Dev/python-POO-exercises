"""
Realizar un programa que conste de una clase llamada Alumno que tenga como atributos el nombre y la nota del alumno.
Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.
"""

# Definimos la clase Alumno.
class Alumno:
    
    # Iniciamos y establecemos los atributos nombre y nota_alumno con el método __init__ (self no es más que el objeto Alumno).
    def __init__(self, nombre, nota_alumno):
        
        # El parámetro self se refiere al objeto instanciado de esa clase sobre el cual se está invocando dicho método.
        self.nombre = nombre
        self.nota_alumno = nota_alumno
    
    # Definimos el método imprimir, en el cual mostramos en la terminal el nombre y la nota del alumno.
    def imprimir(self):
        print('\n')
        print("Nombre: ", self.nombre)
        print("Nota: ", self.nota_alumno)
    
    # Definimos el método resultado, aquí condicionamos por medio de if y else que si el resultado es menor o igual a 5, ha reprobado.
    def resultado(self):
        
        if self.nota_alumno <= 5:
            print("El alumno ha reprobado. \n")
        else:
            print("El alumno ha aprobado. \n")

# Por medio de una variable, envíamos los valores de los parámetros de nombre y nota_alumno.
alumno_uno = Alumno("Jorge", 9)
alumno_dos = Alumno("Alejandro", 5)

# Invocamos los métodos de la clase para cada alumno.
alumno_uno.imprimir()
alumno_uno.resultado()
alumno_dos.imprimir()
alumno_dos.resultado()