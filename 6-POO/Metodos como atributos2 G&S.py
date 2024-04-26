
# Getters & Setters
# Definimos la clase
class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura # Se asignan los valores de los atributos
 
    '''El decorado property nos permite usar metodos como si se trataran de atributos'''
    @property 
    def base(self): # Se llama a esta funcion cuando se require obtener el valor del atributo 'base' de un objeto (Getter)
        return self._base
 
    @base.setter 
    def base(self, base): # Se llama a esta funcion cuando se require asignar el valor del atributo 'base' de un objeto (Setter), (Por eso recibe 'base' como parametro')
        if base < 0: # Valida que el valor que se guradara no se un numero negativo
            raise ValueError("La base no puede ser un número negativo") 
        self._base = base
 
    @property  
    def altura(self): # Se llama a esta funcion cuando se require obtener el valor del atributo 'area' de un objeto (Getter)
        return self._altura # Cuando se busca el valor de altura de un objeto, esta funcion regresa su valor
 
    @altura.setter 
    def altura(self, altura):# Se llama a esta funcion cuando se require asignar el valor del atributo 'area' de un objeto (Setter), (Por eso recibe 'altura' como parametro')
        if altura < 0: # Valida que el valor que se guradara no se un numero negativo
            raise ValueError("La altura no puede ser un número negativo")
        self._altura = altura
 
    @property
    def area(self): # Se llama a esta funcion cuando se require obtener el valor del atributo 'altura' de un objeto (Getter)
        return self.base * self.altura / 2  # Cuando se busca el valor de altura de un objeto, este metodo calcula y regresa su valor
     
     
t = Triangulo(4, 5)
print('Base : ',t.base,'| Altura :',t.altura,"\nÁrea:", t.area)
# Base :  4 | Altura : 5 
# Área: 10.0
'''Podemos ver, que aunque los Getter y Setter son metodos, podemos acceder a ellos como si se tratasen de atributos'''
 
# Como ahora se ejecuta un "metodo" para 'area', cuando cambiamos el valor de un atributo, si se modifica el resultado
t.base = 10
print("Nueva área:", t.area)
# Nueva área: 25.0