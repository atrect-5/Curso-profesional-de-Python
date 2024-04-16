# Alejandro Gonzalez

# Ejercicio 4
'''Cree una lista de 5 elementos con valores del 1 al 5. Luego, agregue un 
elemento obteniendo el valor del tercer elemento de la lista (posición 2). 
Para finalizar, encuentre la posición del valor 3 y elimine la misma.'''
lista = [1, 2, 3, 4, 5]
print(lista, '\nLista original')

lista.append(lista[2])      #Obtiene el elemento en la posicion 2 y lo agrega a la lista
print(lista, '\nAgregando un elemento obteniendo el valor del tercer elemento de la lista')

lista.pop(3)    #Elimina el valor de la posicion 3
print(lista, '\nLista sin el valor de la posicion 3')
