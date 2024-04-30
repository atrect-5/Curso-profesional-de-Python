
class Triangulo:
    def __init__(self, base, altura): 
        self.base = base
        self.altura = altura
 
    @property
    def base(self):
        return self._base
 
    @base.setter
    def base(self, base): # Getter and Setter del atributo 'base'
        if base < 0:
            raise ValueError("La base no puede ser un número negativo") # Si la base es negativa, eleva una excepcion de tipo 'ValueError'
        self._base = base
 
    @property
    def altura(self):
        return self._altura
 
    @altura.setter
    def altura(self, altura): # Getter and Setter del atributo 'altura'
        if altura < 0:
            raise ValueError("La altura no puede ser un número negativo") # Si la altura es negativa, eleva una excepcion de tipo 'ValueError'
        self._altura = altura
 
    @property
    def area(self): # Devuelve el valor del area
        return self.base * self.altura / 2
     
if __name__ == '__main__':
    # Declaramos la instancia
    t = Triangulo(4, 5)
    print("Área:", t.area) # Se imprime el area del triangulo
    # Área: 10.0

    # uso comun de str(). (Devuelve la representacion informal de un objeto)
    '''Cuando se llama al metodo 'print()', tambien se hace uso de la funcion 'str()' para convertir el tipo de dato 
    que queremos imprimir en una cadena de texto. Es decir que estas dos maneras de imprimir en pantalla son equivalentes '''
    print("Triángulo:", t) # Imprime la instancia de Triangulo 't'
    # Triángulo: <__main__.Triangulo object at 0x0000026CA6C6B790>
    print("Uso str():", str(t))
    # Uso str(): <__main__.Triangulo object at 0x0000026CA6C6B790>


    # uso comun de repr(). (Devuelve la representacion formal de un objeto) 
    '''Si no definimos el método, en vez de dar un error, Python genera una representación automática, 
    indicando el nombre de la clase y la dirección en memoria del objeto en cuestión.'''
    print(repr(t))
    # <__main__.Triangulo object at 0x0000017ACF31B790>