# Alejandro Gonzalez : Ejercicios propuestos


# Ejercicio Numero 1 
'''Cree una clase Punto que reciba las coordenadas (x, y) y un método que indique a qué cuadrante pertenece.'''
# Definimos la clase con los atributos correspondientes
class Punto:
    def __init__(self, x, y) -> None: # Recibimos y guardamos las coordenadas 'x' y 'y' del punto
        self.x = x
        self.y = y

    def ubicacion(self): # Definimos la funcion que ubicara los puntos en el plano
        if (self.x >= 0): # Si x es positivo, se ubicara del lado derecho del plano.
            if (self.y >= 0): # Si y es positivo, se ubicara del lado superior del plano
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
p.ubicacion()