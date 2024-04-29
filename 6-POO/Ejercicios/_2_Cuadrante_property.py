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
        wigth = ''
        if (self.x > 0):
            if (self.y > 0):
                print('Cuadrante superior derecho (+,+)')
                for h in reversed(range(self.y +1 )):
                    if (h==self.y-1):
                        wigth=' |'+' '*(self.x*2-1)+'0'
                        print(wigth)
                    else:
                        print(' |')
                wigth = '—|'+'—'*(self.x*2)
                print(wigth)

            elif (self.y < 0):
                print('Cuadrante inferior derecho (+,-)')
                wigth = '—|'+'—'*(self.x*2)
                print(wigth)
                for h in range(self.y*-1 +1 ):
                    if (h==self.y*-1-1):
                        wigth=' |'+' '*(self.x*2-1)+'0'
                        print(wigth)
                    else:
                        print(' |')
            else :
                print('Eje \'x\' positivo (+,0)')
                wigth = '—|'+'—'*(self.x-1)+'0'
                print(wigth)

        elif (self.x < 0): 
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
        else: 
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
if __name__ == '__main__':
    # Recibimos los valores de la coordenadas por medio de 'input' y los asignamos a los atributos 'x' y 'y'
    p = Punto(int(input('Ingresa la coordenada del eje x : ')),int(input('Ingresa la coordenada del eje y : ')))
    p.ubicacion # Podemos apreciar que al acceder al metodo 'ubicacio()', lo hacemos como si se tratase de un atributo