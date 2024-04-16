# Alejandro Gonzalez 

# Ejercicio Numero 1
'''Dada la cadena “El veloz murciélago hindú comía feliz cardillo y kiwi”, imprimir 
su variante justificada a la derecha rellenando con '>', a la izquierda rellenando 
con '<' y centrada en 60 caracteres con asteriscos utilizando métodos de cadenas.'''
print('Ejercicio Numero 1')
print('Una frase sobre un murcielago'.rjust(60, '>')) # Justificado a la derecha
print('Una frase sobre un murcielago'.ljust(60, '<')) # Justificado a la izquierda
print('Una frase sobre un murcielago'.center(60, '+')) # Centrado en 60 '+' 
print('_______________________________________________________')


# Ejercicio Numero 2
'''Dada la cadena “Nuevo curso de Python 3”, utilizar los métodos de cadena e imprimir:'''
print('Ejercicio Numero 2')
''' a) Su variante en mayúsculas '''
print('Nuevo curso de Python 3, en mayuscula'.upper()) # Convierte todas las leras en mayuscula
''' b) Su variante en minúsculas '''
print('Nuevo curso de Python 3, EN MINUSCULA'.lower()) # Convierte todas las letras en minuscula
print('Nuevo curso de Python 3, EN MINUSCULA'.casefold()) # Tambien convierte todo a minuscula
''' c) Su variante intercambiando mayúsculas y minúsculas '''
print('Nuevo curso de Python 3, Cambiando Mayus Y Minus'.swapcase()) # Cambia mayusculas y minusculas de lugar
''' d) Convertir el primer caracter de cada palabra a mayúscula '''
print('Nuevo curso de Python 3, iNICIANDO eN mAYUSCULA'.title()) # Empieza cada palabra con mayuscula
''' extra) Unicamente la primera letra en mayuscula '''
print('Nuevo curso de Python 3, SOLO LA PRIMERA EN MAYUSCULA'.capitalize()) # Unicamentte la primer letra se queda en mayuscula
print('_______________________________________________________')


# Ejercicio Numero 3
'''Utilizando métodos de cadenas, identificar cuál de las siguientes cadenas 
posee solo caracteres alfabéticos: “Python 3”, “Python3”, “Python3.8”'''
print('Ejercicio Numero 3')
print('\"Python 3\", son solo caracteres alfabeticos? -', 'Python 3'.isalpha()) # Evaluando las cadenas
print('\"Python3\", son solo caracteres alfabeticos? -', 'Python3'.isalpha())
print('\"Python3.8\", son solo caracteres alfabeticos? -', 'Python3.8'.isalpha())
print('\"Python\", son solo caracteres alfabeticos? -', 'Python'.isalpha()) # Evaluando sin numero
print('_______________________________________________________')


# Ejercicio Numero 4
'''Utilizando métodos de cadenas, identificar cuál de los siguientes caracteres 
son ascii: ñ, d, s, a, $, &.'''
print('Ejercicio Numero 4')
print('\"ñ\" es ascci? - ', 'ñ'.isascii()) # Evaluando caracteres
print('\"d\" es ascci? - ', 'd'.isascii())
print('\"s\" es ascci? - ', 's'.isascii())
print('\"á\" es ascci? - ', 'á'.isascii())
print('\"$\" es ascci? - ', '$'.isascii())
print('\"&\" es ascci? - ', '&'.isascii())
print('\"~\" es ascci? - ', '~'.isascii())
print('_______________________________________________________')


# Ejercicio numero 5
'''Utilizando métodos de cadenas, crear una variable con una lista de números 
pares del 2 al 10 como cadenas e imprimir sus valores separados por un guión medio.'''
print('Ejercicio Numero 5')
pares = ['2', '4', '6', '8', '10', '12'] # Tienen que ser tipo string para que funcione
print('Numeros pares =', '|'.join(pares)) # Imprimiendo pares con '|' en medio
impares = ['1', '3', '5', '7', '9', '11']
print('Numeros impares =', '|'.join(impares))
print('_______________________________________________________')


# Ejercicio Numero 6
'''Del ejercicio anterior, guardar en una variable el valor impreso y 
volver a separar sus valores utilizando métodos de cadenas.'''
print('Ejercicio Numero 6')
impresion_pares = '|'.join(pares) # Almacenando la impresion anterior con join()
print('Ejercicio anterior con pares: ', impresion_pares)
impresion_impares = '|'.join(impares)
print('Ejercicio anterior con impares: ', impresion_impares)
print('Obteniendo lista original de pares: ', impresion_pares.split('|')) # Obteniendo la lista original partiendo de la impresion almacenada
print('Obteniendo lista original de impares: ', impresion_impares.split('|'))
print('_______________________________________________________')


# Ejercicio numero 7
'''Dada una expresión matemática “2 * 15 = 30”, cambiar el asterisco por 
una “x” y el signo “=” por la cadena “es igual a” utilizando métodos de 
cadenas. **Puede que precises utilizar dos veces el mismo método.'''
print('Ejercicio numero 7')
print('Estado Original de la cadena a imprimir : ', "2 * 15 = 30")
print('Cadena editada : ', "2 * 15 = 30".replace('*', 'X').replace('=', 'es igual a')) # Editando la cadena con replace()
print('_______________________________________________________')



# Ejercicio Numero 8 
'''Dada la expresión “{1} * {2} = {0}”.format(15, #, #), reemplaza los 
numerales para que la cadena sea una expresión válida.'''
print('Ejercicio Numero 8')
print('Aqui viene una multiplicacion : ', '{1} * {2} = {0}'.format(15, 5, 3)) # Lo que esta en las llaves se remplaza con los argumentos de format()
print('{0} que se {1}, se lo lleva la {2}'.format('camaron', 'duerme', 'corriente'))
print('_______________________________________________________')


# Ejercicio Numero 9
'''Codifica la cadena “El veloz murciélago hindú comía feliz cardillo y kiwi” 
a una secuencia de bytes con utf-16, guarda el valor en una variable y luego 
vuelve a decodificarla para imprimir la cadena.'''
print('Ejercicio numero 9')
print('Codificando una cadena : ')
cadenaCodificada = 'El veloz murciélago hindú comía feliz cardillo y kiwi'.encode('utf-16') # Se codifica la cadena
print('Cadena codificada con utf-16 : ', cadenaCodificada)
cadenaDecodificada = cadenaCodificada.decode('utf-16') # se decodifica la cadena
print('Cadena decodificada : ', cadenaDecodificada)