
# Secuencias 

num_pares = [0, 2, 4, 6, 8, 10]
for num_par in num_pares:
    print(num_par) # Con esto se imprime la lista 1 por 1 de los elementos de 'num_pares'
'''
0
2
4
6
8
10
'''

for num_par in num_pares[::-1]: # Aqui se indica que se recorrera la lista alrevez
    print(num_par)
'''
10
8
6
4
2
0
'''
# Esto es porque se especifican : [inicio:final:Salto]

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(lista[1:5]) # Se imprimen los sugares de la lista del 1 al 5, sin contar el lugar 5 pero si el 1
# [2, 3, 4, 5]
print(lista[::2]) # Se imprimen todos los valores de la lista, aumentando de 2 en 2
# [1, 3, 5, 7, 9]
print(lista[::-2]) # Se imprimen todos los valores de la lista, empezando por el final y disminuyendo de 2 en 2
# [10, 8, 6, 4, 2]

# Lista por extension
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# lista por comprension 
num_impares = [n for n in numeros if n%2]
print(num_impares)


# Metodos de listas 

'''Extend'''
numeros = list(range(1, 6)) # Solo se le da un nuevo valor a la lista 'numeros'
print(numeros)
# [1, 2, 3, 4, 5]
numeros.extend(list(range(6, 10)))  # Se a;aden los elementos de la iteracion a la lista 'numeros'
print(numeros)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

'''Insert'''
frutas = ["peras", "manzanas"]
print(frutas)
# ['peras', 'manzanas']
frutas.insert(1, "naranjas") # Se agrega el elemento 'naranjas' a la lista en la posicion 1
print(frutas)
# ['peras', 'naranjas', 'manzanas']

'''Clear'''
frutas.clear() # Elimina los elementos de 'frutas'
print(frutas)
# []

'''Sort'''
numeros = [5,7,2,6]
print(numeros) 
# [5,7,2,6]
numeros.sort() # Se ordenan los numeros de menor a mayor, si no se indica lo contrario
print(numeros)
# [2, 5, 6, 7]

frase = "El veloz murciélago hindú comía feliz cardillo y kiwi".split() # Se crea una lista de palabras con esta frase
print(frase)
# ['El', 'veloz', 'murciélago', 'hindú', 'comía', 'feliz', 'cardillo', 'y', 'kiwi']
frase.sort(key=len, reverse=True) # Se le indica que va a ordenar con referencia a que tan larga es la palabra y de manera invertida (mayor a menor)
print(frase)
# ['murciélago', 'cardillo', 'veloz', 'hindú', 'comía', 'feliz', 'kiwi', 'El', 'y']

'''Reverse'''
frase.reverse() # Esto invierte los elementos de la lista 'frase'
print(frase)
# ['y', 'El', 'kiwi', 'feliz', 'comía', 'hindú', 'veloz', 'cardillo', 'murciélago']

'''Copy'''
copyFrase = frase.copy()
print(copyFrase)
# ['y', 'El', 'kiwi', 'feliz', 'comía', 'hindú', 'veloz', 'cardillo', 'murciélago']