# Alejandro Gonzalez : Ejercicios propuestos

# Ejercicio Numero 3 
''' Cree una clase Vector que reciba 2 instancias de la clase Punto y devuelva el vector resultante. Deberá poseer 3 atributos:
a: será el punto 1.
b: será el punto 2
c: @property ab: será una tupla del vector resultante que indicará la diferencia (distancia) entre los puntos recibidos.'''
from _2_Cuadrante_property import Punto # importamos nuestra clase 'Punto' para usarla en este ejercicio
# Definimos nuestra clase 'Vector'
class Vector:
    def __init__(self, puntoA, puntoB) -> None: # Se inicializa el vector, donde se guardan las coordenadas de 2 puntos
        self.puntoA = puntoA
        self.puntoB = puntoB

    @property # en este metodo se calcula el vector resultante de los 2 puntos (Vector AB = B-A)
    def ab(self):
        return(self.puntoB.x - self.puntoA.x, self.puntoB.y - self.puntoA.y)

# Declaramos 2 instancias de 'Punto', cada una con sus coordenadas
print('Punto A:')
punto_a = Punto(int(input('Ingresa la coordenada del eje x : ')),int(input('Ingresa la coordenada del eje y : ')))
print('Punto B:')
punto_b = Punto(int(input('Ingresa la coordenada del eje x : ')),int(input('Ingresa la coordenada del eje y : ')))

# Declaramos una instancia de 'Vector', donde se guarda la ubicacion de los 2 puntos
vector = Vector(punto_a,punto_b)

# Vemos que se han guardado exitosamente
print('Punto A: ')
vector.puntoA.ubicacion
print('Punto B: ')
vector.puntoB.ubicacion

print('Vector resultante de los puntos recibidos AB: ', vector.ab)