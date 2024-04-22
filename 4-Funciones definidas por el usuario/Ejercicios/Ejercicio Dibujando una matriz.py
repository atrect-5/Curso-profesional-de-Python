# Alejandro Gonzalez 

# Ejercicio Numero 1
'''Escriba una función que, recibiendo el valor de una matriz de 2 dimensiones, 
imprima la misma con el caracter “X”.'''
print('Ejercicio Numero 1')

# Definimos la funcion que hara la matriz
def Dibuja_Matriz(ejex, ejey):
    '''Devuelve una matriz dibujada con 'X' 

    Parameters:
        int ejex: indica el largo de la matriz
        int ejey: indica el alto de la matriz
    
    Returns:
        Una matriz de largo 'ejex' y de alto 'ejey' 
    '''
    for x in range(ejey):  # Se imprimira un nuevo renglon la cantidad de veces indicada en 'ejey', lo que nos dara el alto determinado
        print('X ' * ejex) # Se imprime una 'X' la cantidad de veces indicada en 'ejex'

# Se llama a la funcion que dibuja la matriz
Dibuja_Matriz(int(input('Largo de la Matriz : ')), int(input('Alto de la matriz : ')))
