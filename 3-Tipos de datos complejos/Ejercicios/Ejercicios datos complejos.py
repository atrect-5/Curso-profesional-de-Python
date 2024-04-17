# Alejandro Gonzalez

# Ejercicio Numero 1
'''Cree una lista de números pares del 0 al 10 utilizando una lista por comprensión.'''
print('Ejercicio numero 1')
numerosPares = [n for n in range(0, 11) if n%2 == 0] # En el rango de 0 a 11 (el 11 no se incluye), los numeros pares se agregan a la lista
print('Lista de numeros pares: ', numerosPares)
print('_______________________________________________________')


# Ejercicio Numero 2
'''Recorra la lista en forma directa e inversa e imprima sus valores.'''
print('Ejercicio numero 2')
print('Lista Original  : ', numerosPares)
print('Lista Invertida : ', numerosPares[::-1]) # Se indica que la lista completa se recorrera con iteracion de -1 (inversa)
print('_______________________________________________________')


# Ejercicio Numero 3
'''Data la lista [“radar”, “palabra”, “reconocer”, “frase”, “aves”, “perdiz”], recorra sus 
elementos con un ciclo for e imprima un mensaje si la misma es un palíndromo.'''
print('Ejercicio Numero 3')
listaPalabras = ['radar', 'palabra', 'reconocer', 'frase', 'aves', 'perdiz', 'ana', 'arenera']
for palabra in listaPalabras: # Se recorre la lista
    if palabra == palabra[::-1]:  # Si la palabra es igual a la palabra alrevez, es un palindromo 
        print(palabra, ': Es un palindromo')
    else:
        print(palabra, ': Esta no')
print('_______________________________________________________')


# Ejercicio Numero 4
'''Cree un diccionario que posea el nombre de las monedas “Euro” y “Dolar” 
como claves con sus respectivos símbolos (€ y $) como valor.''' 
print('Ejercicio Numero 4')
monedas = dict([('Euro', '€'), ('Dolar', '$'), ('Libra', '£')]) # Creando un diccionario de monedas
print('Diccionario inicial de monedas : ', monedas)


# Ejercicio Numero 5
'''Recorra e imprima las parejas clave:valor del diccionario creado en el punto anterior.'''
print('\nEjercicio Numero 5')
for k, v in monedas.items(): # Imprimimos los diferentes claves:valores del diccionario
    print(k,v)

# Ejercicio Numero 6
'''Agregue la pareja Yen (¥) con el método setdefault.'''
print('\nEjercicio Numero 6')
monedas.setdefault('Yen', '¥') # Se agrega una nueva moneda
print('Diccionario final de monedas : ', monedas)

for k, v in monedas.items(): # Imprimimos los diferentes claves:valores del diccionario
    print(k,v)
print('_______________________________________________________')


# Ejercicio numero 7
'''Cree un diccionario con las claves “buen”, “día”, “noche”, “gracias” y “hola” con 
sus respectivas traducciones al inglés como clave. Luego, con la frase “Hola buen día”, 
muestre su traducción obteniendo la misma de este diccionario.'''
print('\nEjercicio Numero 7')
traducciones = {'buen':'good', 'dia':'day', 'noche':'nigth', 'gracias':'thanks', 'Hola':'hey'} # Creamos el diccionario de palabras traducidas

frase = 'Hola buen dia' # Creamos la frase a traducir
fraseTraducida = ''
for palabra in frase.split(): # Dividimos la frase en las palabras por separado
    fraseTraducida += traducciones.get(palabra) + ' ' # Obtenemos las palabras traducidas y se juntan en la variable

print('Español : ')
print(frase)
print('Ingles : ')
print(fraseTraducida)