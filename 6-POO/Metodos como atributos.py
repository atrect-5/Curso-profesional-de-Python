
# Creamos una clase 
class Triangulo:
    def __init__(self, base, altura) -> None:
        self.altura = altura # Se definen los atributos del triangulo
        self.base = base
        self.area = (base*altura) / 2 # Se calcula el valor que tendra el area del triangulo

triangulo = Triangulo(4,3)
print('Area : ', triangulo.area) # Se imprime el valor del area calculada
# 6.0

# Se cambia uno de los atributos del objeto
triangulo.base = 10
print('Area : ', triangulo.area)
# 6.0
'''Aunque se cambio uno de los atributos del objeto, el area ya fue calculada cuando se inicializo
Por lo que el area tendra el mismo valor aunque se cambie el valor de un atributo'''

# Para arreglarlo, 'area debera ser un metodo y no un atributo'
class Triangulo:
    def __init__(self, base, altura) -> None:
        self.altura = altura # Se definen los atributos del triangulo
        self.base = base

    def area(self): # Se define 'area' como un metodo en lugar de un atributo
        return self.base * self.altura / 2

triangulo = Triangulo(4,3)
print('Area : ', triangulo.area()) # Se imprime el valor del area calculada
# 6.0

# Se cambia uno de los atributos del objeto
triangulo.base = 10
print('Area : ', triangulo.area())
# 15.0
'''En esta ocasion, si cambio el resultado, debido a que ahora se trata de un metodo y no de un atributo'''
