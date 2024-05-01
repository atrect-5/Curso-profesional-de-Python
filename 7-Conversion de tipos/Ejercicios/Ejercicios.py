# Alejandro Gonzalez

'''
Instrucciones para el ejercicio :
1.- Importe namedtuple y utilizando la misma, cree una clase Pizza con los atributos tamanyo, precio e ingredientes. Luego, cree una lista vacía pizzas.
2.- Dada la lista “pedidos”, agruéguela al código, recorra la misma, cree instancias de la clase Pizza y agregue las mismas a la lista “pizzas”.
3.- Utilizando collections.Counter, cree un objeto ranking_ingredientes que contenga todos los ingredientes de las instancias en la lista “pizzas” 
 (incluyendo repetidos). Luego imprima el ingrediente más utilizado con la cantidad de pedidos que incluyeron el mismo.
** La impresión debe devolver [('Queso', 6)]
4.- Utilizando collections.defaultdict, cree un objeto con el tipo int por defecto. Luego, actualice el objeto con los valores de la variable 
 ranking_ingredientes del paso anterior. Para finalizar, imprima el valor de las claves “Pepperoni” y “Pepinillos”; deben devolver 3 y 0 respectivamente.
5.- Obtenga e imprima en pantalla el precio mínimo y máximo de cada tamaño de pizza existente en la lista “pizzas”. Considere utilizar defaultdict.
'''

# importamos el modulo 'collections'
import collections
# Creamos la clase 'Pizza' usando 'namedtuple'
Pizza = collections.namedtuple('Pizza', 'tamano,precio,ingredientes')

# Creamos una lista vacia 'pizzas'
pizzas = []

# Agregamos la lista 'pedidos' predefinida para los ejercicios
pedidos = [
    ["XL", 100, ["Queso", "Jamón"]],
    ["XL", 120, ["Queso", "Pepperoni"]],
    ["M", 80, ["Queso", "Piña"]],
    ["S", 60, ["Queso"]],
    ["M", 70, ["Pepperoni"]],
    ["L", 90, ["Queso", "Pepperoni"]],
    ["L", 80, ["Queso", "Tomates"]],
]

# Agregamos los pedidos a la lista 'pizzas' como objetos de 'Pizza'
for pzz in pedidos:
    pizza=Pizza(tamano=pzz[0], precio=pzz[1], ingredientes=pzz[2])
    pizzas.append(pizza) # Se gurada la lista de las pizzas que hay

print(pizzas)