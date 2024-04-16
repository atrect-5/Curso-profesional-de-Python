#lista
'''Las listas en python son mas versatiles, 
esto quiere decir que no necesitas definir
cuantos valores va a tener ni de que tipo
van a ser esos valores en la lista'''
lista = [0, "Posicion 1", [2, 3], 3]


#Tupla (la que se recomienda es la tupla2)
'''Las tuplas son muy similares a las listas, 
con la única diferencia de que son inmutables. 
Esto quiere decir que una vez que se definen, 
no pueden ser modificadas.'''
tupla1 = 1, 2, 3
tupla2 = (1, 2, 3)


#Conjuntos (set)
'''Son parecidos a las listas, con la diferencia 
de que los datos no estan ordenados.Es decir que 
cuando quieras imprimir el conjunto, no tendra el 
mismo orden en el que fue creado'''
conjunto = {"Lunes", "Martes", "Miercoles", "Jueves", "Viernes"}
#.discard(), no hace nada cuando no existe el parametro
#.remove(), excepcion KeyError
#.pop(), elimina el ultimo elemento (aleatorio)


#Diccionarios (dict)
'''Los diccionarios son conjuntos desordenados 
de parejas clave: valor, por lo que para cada 
valor que almacenes en el diccionario, siempre 
habrá una clave para poder acceder a él.
(las claves no se deben repetir)'''
diccionario = {'Celsius' : 'C', 'Fahrenheit' : 'F', 'Kelvin' : 'K'}
diccionario2 = dict([('C', 'Celsius'), ('F', 'Fahrenheit'), ('K', 'Kelvin')])
#diccionario[], devuelve excepcion KeyError si no encuentra
#diccionario.get(), devuelve None si no encuentra
