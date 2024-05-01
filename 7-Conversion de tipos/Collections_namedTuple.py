
# Manera "Tradicional" de hacer una clase
class Punto:
    """ Define las coordenadas x, y, z de un punto en un espacio tridimensional. """
 
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

        # Agregamos la funcion para que imprima con buen formato
    def __repr__(self):
        clase = type(self).__name__
        return f'{clase}({self.x}, {self.y}, {self.z})'

    # Agregamos la funcion que se llama al usar el operador '==' y asi poder evaluar dos instancias
    def __eq__(self, otro):
        return True if self.x == otro.x and \
            self.y == otro.y and \
            self.z == otro.z \
            else False
 
if __name__ == '__main__':
    p = Punto(5, -4, 7)
 
    print("x:", p.x)
    # x: 5
    print("y:", p.y)
    # y: -4
    print("z:", p.z)
    # z: 7

    print(p)
    # Punto(5, -4, 7)
    print(p == Punto(5, -4, 7)) # Ahora si se pueden comparar 2 instancias de 'Punto'
    # True
    print(p == Punto(5, -4, 6))
    # False
    print('________________________')


# Manera de hacerlo con namedtuple

import collections
Punto2 = collections.namedtuple("Punto2", "x y z")
 
p = Punto2(5, 7, 10)
 
print("x:", p.x)
# x: 5
print("z:", p[-1])
# z: 10
print("Tamaño:", len(p))
# Tamaño: 3

print(p)
# Punto2(x=5, y=7, z=10)
print(p == Punto2(5, 7, 10))
# True


# Si algun argumento no tiene un mobre valido, se cambia por el numero de su posicion seguido de un '_' (Si se especifica 'rename=True')
Usuario = collections.namedtuple(
    "Usuario",
    "_password, nombre, 123",
    rename=True)
 
print(Usuario._fields)
#('_0', 'nombre', '_2')