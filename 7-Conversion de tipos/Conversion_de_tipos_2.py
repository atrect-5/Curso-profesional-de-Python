
# Importamos la clase 'Triangulo' del ejemplo anterior
from Conversion_de_tipos import Triangulo

# str() / __str__
# Cuando se llame el metodo 'str()' para triangulo, se llamara esta funcion, asi imprimiremos lo que nosostros queramos y no 'tipo de objeto, direccion en memoria'
def __str__(self):
    '''La parte 'type(self).__name__' nos devuelve el nombre de la clase del objeto que llama al metodo, 
    esto nos permite hacerlo reutilizable en caso de que la clase herede'''
    return f'{type(self).__name__} de base {self.base} y altura {self.altura}.'


# Agregamos dicha funcion a nuestra clase 'Triangulo'
Triangulo.__str__ = __str__


if __name__ == '__main__':
    # Probamos el metodo 
    t = Triangulo(4, 5)
    print("Área:", t.area) # Se imprime el area del triangulo
    # Área: 10.0

    print("Triángulo:", t) # Ahora se utiliza la funcion '__str__' sobreescrita en la clase triangulo
    # Triángulo: Triangulo de base 4 y altura 5.
    print("Uso str():", str(t))
    # Uso str(): Triangulo de base 4 y altura 5.
    '''Como podemos observar, utilizar “t” en un print, es equivalente a utilizar “str(t)“.'''



# repr() / __repr__
# Cuando se llame a la funcion 'repr()' se llamara a esta funcion 
'''si eval() es capaz de construir una instancia a partir de dicho método, significa que tiene toda la información necesaria. '''

def __repr__(self):
    clase = type(self).__name__
    #retorna Triangulo(base, altura), que es el mismo formato que utilizamos al crear una instancia de dicha clase.
    return f'{clase}({self.base}, {self.altura})' 

# Agregamos dicha funcion a nuestra clase 'Triangulo'
Triangulo.__repr__ = __repr__


if __name__ == '__main__':
    print(repr(t))
    # Triangulo(4, 5)
    print(eval(repr(t))) #Vemos que 'eval(repr(t))', devuelve un objeto identico al que pasamos como argumento, y este es impreso con la funcion str()->__str__
    # Triangulo de base 4 y altura 5.