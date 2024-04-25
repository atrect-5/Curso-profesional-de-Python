
# ¿por qué tenemos que añadir explícitamente el parámetro self a los métodos cada vez que definimos uno? 
# ¿Por qué Python no los declara de forma automática y nos ahorramos tener que hacerlo nosotros? 

from math import sqrt

# Clase de un punto, donde guardamos sus coordenadas de un plano.
class Punto:
    def __init__(self, x, y) -> None:
        self.x = x # Coordenada 'x' del punto
        self.y = y # coordenada 'y' del punto
    def distancia(self, otroPunto): # Metodo para obtener la distancia entre 2 puntos de un plano
        delta_x = self.x - otroPunto.x
        delta_y = self.y - otroPunto.y # Primero se obtienen las diferencias de las coordenadas 'x' y 'y'

        return sqrt(delta_x**2 + delta_y**2) # se hace la operacion para obtener la distancia de los puntos y retorna el valor
    
p1 = Punto(1,2)
p2 = Punto(3,4) # Asignamos las coordenadas a los puntos

# Imprimimos si de llamar al metodo de la clase de estas 2 maneras es la mismo 
print( p1.distancia(p2) == Punto.distancia(p1, p2) ) 
# True



# Se crea de la clase 'Dot', que no contiene nada
class Dot:
    pass

# Se crea una funcion 'setear_x', que asgna un valor
def setear_x(self, valor):
    self.x = valor

# Se agrega el atributo 'setear_x' a la clase 'Dot', y se le indica que se le asignara la funcion que creamos previamente
Dot.setear_x = setear_x

# Para comprobar, creamos una instancia de nuestra clase y usamos el metodo 'setear_x' para ver su funcionamiento
p1 = Dot(25)
p1.setear_x(25)
print(p1.x)
# 25

'''El argumento definitivo de por qué el parámetro self no puede ser opcional, 
se encuentra en los decoradores, debido a las acciones que pueden realizarse en los mismos.'''