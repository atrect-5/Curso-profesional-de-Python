
# Importamos el modulo collections
import collections

# print(collections.__doc__)
'''This module implements specialized container datatypes providing
    alternatives to Python's general purpose built-in containers, dict,
    list, set, and tuple. '''


# Conuter() Cuenta cuantas veces se repite un elemento
palabra = "AzulSchool"
count = collections.Counter(palabra) # Guardamos el conteo de palabras en 'count'
 
print(type(count))
# <class 'collections.Counter'>
print(count) # Regresa un diccionario indicando cuantas veces se repite cada letra
# Counter({'l': 2, 'o': 2, 'A': 1, 'z': 1, 'u': 1, 'S': 1, 'c': 1, 'h': 1})


lenguajes_usuarios = ['Python', 'C++', 'Java', 'Python', 'C#', 'Ruby', 'Python', 'C++', 'JS', 'Java', 'Go'] 
count = collections.Counter(lenguajes_usuarios)
 
print(count.most_common(1)) # Devuelve una lista de un elemento: una tupla que posee la cadena y la cantidad de veces que se repite
# [('Python', 3)]
print(count.most_common()) # Devuelve una lista de tuplas ordenada de la mayor a menor cantidad de repeticiones
# [('Python', 3), ('C++', 2), ('Java', 2), ('C#', 1), ('Ruby', 1), ('JS', 1), ('Go', 1)]

# defaultdict() al intentar obtener el valor de una clave que no hayamos definido, se cree la clave con el tipo de dato que hayamos definido y nos devuelva dicho valor
d = collections.defaultdict(str)

print(type(d))
# <class 'collections.defaultdict'

print("claves:", d.keys()) # No tiene claves
# claves: dict_keys([])
print("valor:", d["alguna_clave"]) # Al buscar la clave, se crea en el diccionario
# valor: 
print("claves:", d.keys()) # Ahora si posee una clave
# claves: dict_keys(['alguna_clave'])


# OrderedDict ()

# Creamos 2 diccionarios con los mismos valores, pero de manera invertida 
a = {}
a["uno"] = 1
a["dos"] = 2
b = {}
b["dos"] = 2
b["uno"] = 1
print(f'a: {a}, b: {b}')
# a: {'uno': 1, 'dos': 2}, b: {'dos': 2, 'uno': 1}
print(a == b) # Comparamos si son iguales (Ya que el orden de los diccionarios no importa)
# True

# Hacemos lo mismo, pero con la clase OrderedDict
a = collections.OrderedDict()
a["uno"] = 1
a["dos"] = 2
b = collections.OrderedDict()
b["dos"] = 2
b["uno"] = 1
 
print(a == b) # Aqui si importa el orden
# False