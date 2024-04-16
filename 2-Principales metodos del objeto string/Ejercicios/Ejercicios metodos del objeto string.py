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
