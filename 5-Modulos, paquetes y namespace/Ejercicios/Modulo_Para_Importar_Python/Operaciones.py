# Alejandro Gonzalez 

# Paso Numero 1 del ejercicio de 'Modulos, paquetes y namespace'
'''Cree un módulo de Python que contenga las siguientes funciones:
1- suma(*args): Debe recibir un número variable de argumentos y retornar la suma de los mismos.
2- resta(*args): Debe recibir un número variable de argumentos y retornar la resta de los mismos.
3- producto(*args): Debe recibir un número variable de argumentos y retornar el producto de los mismos.
4- division(*args): Debe recibir un número variable de argumentos y retornar lla división de los mismos.'''

def Suma(*sumandos:list) -> float:
    '''Esta funcion devuelve una suma de una lista de numeros
    Parameters:
        list : sumandos : Lista de los numeros que se van sumar
    Returns:
        float : Suma de una lista de numeros'''
    total = 0
    for numero in sumandos:
          total += numero
    return total

def Resta(*rest:list) -> float:
    '''Esta funcion devuelve una resta de una lista de numeros
    Parameters:
        list : rest : Lista de los numeros que se van restar
    Returns:
        float : Resta de numeros'''
    total = rest[0]*2  # Se inicia con el valor del primer elemento, y ya que es el primer numero que se le va a restar, se compensa multiplicandolo * 2
    for numero in rest:
          total -= numero
    return total

def Producto(*factores:list) -> float:
    '''Esta funcion devuelve el producto de una lista de numeros
    Parameters:
        list : factores : Lista de los numeros que se van multiplicar
    Returns:
        float : Producto de una lista de numeros'''
    total = 1
    for numero in factores:
          total *= numero
    return total


def Divicion(*dividendos:list) -> float:
    '''Esta funcion devuelve la division de una lista de numeros
    Parameters:
        list : dividendos : Lista de los numeros que se van dividir
    Returns:
        float : Division de una lista de numeros'''
    total = dividendos[0]**2  # Se inicia con el valor del primer elemento, y ya que es el primer numero que se le va a dividir, se compensa elevando al cuadrado
    for numero in dividendos:
          if numero == 0:
               return "No es posible dividir, hay un cero en la lista de numeros"
          total /= numero
    return total
