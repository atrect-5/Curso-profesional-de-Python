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
        if (self.x > 0):
            if (self.y > 0):
                print('Cuadrante superior derecho (+,+)')
                print('  | 0\n--+--\n  |  ')
            elif (self.y < 0):
                print('Cuadrante inferior derecho (+,-)')
                print('  |  \n--+--\n  | 0')
            else :
                print('Eje \'x\' positivo (+,0)')
                print('  |  \n--+-0\n  |')
        elif (self.x < 0): 
            if (self.y > 0):
                print('Cuadrante superior izquierdo (-,+)')
                print('0 |  \n--+--\n  |  ')
            elif (self.y < 0):
                print('Cuadrante inferior izquierdo (-,-)')
                print('  |  \n--+--\n0 |  ')
            else:
                print('Eje \'x\' negativo (-,0)')
                print('  |  \n0-+--\n  |')
        else: 
            if (self.y > 0):
                print('Eje \'y\' superior (0,+)')
                print('  0  \n--+--\n  |  ')
            elif (self.y < 0):
                print('Eje \'y\' inferior (0,-)')
                print('  |  \n--+--\n  0  ')
            else:
                print('Origen (0,0)')
                print('  |  \n--0--\n  |')
if __name__ == '__main__':
    # Recibimos los valores de la coordenadas por medio de 'input' y los asignamos a los atributos 'x' y 'y'
    p = Punto(float(input('Ingresa la coordenada del eje x : ')),float(input('Ingresa la coordenada del eje y : ')))
    p.ubicacion # Podemos apreciar que al acceder al metodo 'ubicacio()', lo hacemos como si se tratase de un atributo