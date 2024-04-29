# Alejandro Gonzalez : Ejercicios propuestos


# Ejercicio Numero 1 
'''Cree una clase Punto que reciba las coordenadas (x, y) y un método que indique a qué cuadrante pertenece.'''
# Definimos la clase con los atributos correspondientes
class Punto:
    def __init__(self, x, y) -> None: # Recibimos y guardamos las coordenadas 'x' y 'y' del punto
        self.x = x
        self.y = y

    def ubicacion(self): # Definimos la funcion que ubicara los puntos en el plano
        if (self.x > 0): # Si 'x' es positivo, se ubicara del lado derecho del plano.
            if (self.y > 0): # Si 'y' es positivo, se ubicara del lado superior del plano
                print('Cuadrante superior derecho (+,+)')
                for h in reversed(range(self.y +1 )): # Imprime una representacion visual del punto con dichas coordenadas 
                    if (h==self.y-1):
                        wigth=' |'+' '*(self.x*2-1)+'0'
                        print(wigth)
                    else:
                        print(' |')
                wigth = '—|'+'—'*(self.x*2)
                print(wigth)
            elif (self.y < 0): # Si 'y' es negativo, se ubicara del lado inferior del plano
                print('Cuadrante inferior derecho (+,-)')
                wigth = '—|'+'—'*(self.x*2)
                print(wigth)
                for h in range(self.y*-1 +1 ):
                    if (h==self.y*-1-1):
                        wigth=' |'+' '*(self.x*2-1)+'0'
                        print(wigth)
                    else:
                        print(' |')
            else : # Si 'y' no es mayor ni menor que 0 (Es 0), se ubicara el en Eje x
                print('Eje \'x\' positivo (+,0)')
                wigth = '—|'+'—'*(self.x-1)+'0'
                print(wigth)

        elif (self.x < 0): # Si 'x' es negativo, se ubicara del lado izquierdo del plano.
            if (self.y > 0):
                print('Cuadrante superior izquierdo (-,+)')
                for h in reversed(range(self.y +1 )):
                    if (h==self.y-1):
                        wigth='0'+' '*(self.x*-2-1)+'|'
                        print(wigth)
                    else:
                        print(" "*(self.x*(-2))+'|')
                wigth = '—'*(self.x*-2)+'|—'
                print(wigth)
            elif (self.y < 0):
                print('Cuadrante inferior izquierdo (-,-)')
                wigth = '—'*(self.x*-2)+'|—'
                print(wigth)
                for h in range(self.y*-1+1 ):
                    if (h==self.y*-1-1):
                        wigth='0'+' '*(self.x*-2-1)+'|'
                        print(wigth)
                    else:
                        print(" "*(self.x*(-2))+'|')
            else:
                print('Eje \'x\' negativo (-,0)')
                wigth = '0'+'—'*(self.x*-1-1)+'|—'
                print(wigth)

        else: # Si 'x' no es mayor ni menor que 0 (Es 0), se ubicara en el Eje y
            if (self.y > 0):
                print('Eje \'y\' superior (0,+)')
                print(' 0')
                for h in range(self.y-1):
                    print(' |')
                print('—|—')
            elif (self.y < 0):
                print('Eje \'y\' inferior (0,-)')
                print('—|—')
                for h in range(self.y*-1-1):
                    print(' |')
                print(' 0')
            else:
                print('Origen (0,0)')
                print('  |  \n--0--\n  |')

# Recibimos los valores de la coordenadas por medio de 'input' y los asignamos a los atributos 'x' y 'y'
p = Punto(int(input('Ingresa la coordenada del eje x : ')),int(input('Ingresa la coordenada del eje y : ')))
p.ubicacion()