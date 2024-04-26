# Alejandro Gonzalez : Ejercicios propuestos

# Ejercicio numero 2
'''Modifique el método anterior para convertirlo en una propiedad (@property).'''
# Copiamos la clase anterior para convertir el metodo en @property
class Punto:
    def __init__(self, x, y) -> None: 
        self.x = x
        self.y = y

    @property # Hacemos de la funcion un @property para poder acceder a esta como un atributo y no como un metodo
    def ubicacion(self): 
        if (self.x >= 0): 
            if (self.y >= 0):
                print('Cuadrante superior derecho (+,+)')
                print('  | 0\n--+--\n  |  ')
            else:
                print('Cuadrante inferior derecho (+,-)')
                print('  |  \n--+--\n  | 0')
        
        else:
            if (self.y >= 0):
                print('Cuadrante superior izquierdo (-,+)')
                print('0 |  \n--+--\n  |  ')
            else:
                print('Cuadrante inferior izquierdo (-,-)')
                print('  |  \n--+--\n0 |  ')

# Recibimos los valores de la coordenadas por medio de 'input' y los asignamos a los atributos 'x' y 'y'
p = Punto(float(input('Ingresa la coordenada del eje x : ')),float(input('Ingresa la coordenada del eje y : ')))
p.ubicacion # Podemos apreciar que al acceder al metodo 'ubicacio()', lo hacemos como si se tratase de un atributo