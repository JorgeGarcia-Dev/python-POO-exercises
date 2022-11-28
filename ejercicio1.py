"""
Realizar un programa que conste de una clase llamada Alumno que tenga como atributos el nombre y la nota del alumno.
Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.
"""

class Alumno:
    
    def __init__(self, nombre, nota_alumno):
        
        self.nombre = nombre
        self.nota_alumno = nota_alumno
    
    def imprimir(self):
        print('\n')
        print("Nombre: ", self.nombre)
        print("Nota: ", self.nota_alumno)
    
    def resultado(self):
        
        if self.nota_alumno <= 5:
            print("El alumno ha reprobado. \n")
        else:
            print("El alumno ha aprobado. \n")

alumno_uno = Alumno("Jorge", 9)
alumno_dos = Alumno("Alejandro", 5)

alumno_uno.imprimir()
alumno_uno.resultado()
alumno_dos.imprimir()
alumno_dos.resultado()