# Alejandro Gonzalez

# Ejercicio numero 3
'''Cree una función que, recibiendo una lista de números, retorne una lista con 2 
elementos, la primera debe ser una lista de pares y el segundo una lista de impares.'''
print('Ejercicio Numero 3')

def Dividiendo_Pares_Impares(lista): # Definimos la funcion para separar la lista en 2 listas
    '''Devuelve 1 lista, en donde el primer valor son los numeros pares y el segundo los numeros impares
       de una lista principal
    Parameters: 
        list lista: Una lista de numeros
    Return:
        list: Lista donde el primer valor, son los numeros pares de 'lista' y el segundo valor
              son los numeros impares de 'lista' '''
    pares = []
    impares = []

    # Se recorren los numeros de la lista
    for numero in lista:
        if numero % 2:
            impares.append(numero) # cuando son impares, se agregan a la lista impares
        else:
            pares.append(numero) # cuando son pares, se agregan a la lista pares
    
    return [pares, impares] # Se regresa una lista, como primer valor numeros pares y segundo valor numeros impares

lista = [1,2,3,4,5,6,7,8,9,10] # Se declara la lista de numeros principal
print('Lista original', lista)
# Se llama a la funcion para que separe los numeros
lista_dividida = Dividiendo_Pares_Impares(lista)
print('Pares : ', lista_dividida[0], '\nImpares : ', lista_dividida[1])