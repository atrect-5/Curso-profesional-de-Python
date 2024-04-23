
# Funcion para sumar 2 numeros
def Suma(x,y): # Podemos ver que aqui se reciven 2 numeros 
     return x+y

# Esta es una funcion que suma una canidad desconocida de numeros
'''Se crea para probar el uno de *args en funciones'''
def SumaArgs(*args): # En esta funcion, se recibe una lista de x numeros que se almacenara en 'args'
    num = 0
    for n in args:
          num += n
    return num

# Esta funcion regresa el producto de una cantidad variable de elementos parametro
def Producto(*args):
    num = 1
    for arg in args:
        num *= arg
    return num

# Se crea un diccionario con palabras clave que nos dejara decidir si queremos ir a una funcion o a otra
OPERACIONES = {'suma':SumaArgs, 'producto':Producto}

# Esta funcion recive una cantidad variable de parametros que se sumaran o multiplicaran, dependiendo de lo que se obtenga de parametro en 'kwargs' (recibiendo un diccionario)
def Operacion(*args, **kwargs):
    return OPERACIONES.get(kwargs.get("operacion"))(*args)

