
# Join 
''' str.join(iterable) '''
print('.'.join(('www', 'azulschool', 'net'))) # Devuelve una cadena concatenando los elementos de un iterable (como list, string y tuple), separándolos con la cadena str
# www.azulschool.net

# Partition 
''' str.partition(sep) '''
print('www.azulschool.net'.partition('azulschool')) # Devuelve una tupla de 3 elementos, donde se divide la cadena en la primer aparición del parámetro sep. (antes, sep, despues)
# ('www.', 'azulschool', '.net')
print('www.azulschool.net'.partition('http://')) # Si no se enceuntra, devuelve ('str', '', '')
# ('www.azulschool.net', '', '')

# Rpartition 
''' str.rpartition(sep) '''
print('www.azulschool.net'.rpartition('azulschool')) # Devuelve una tupla de 3 elementos, donde se divide la cadena en la ultima aparición del parámetro sep. (antes, sep, despues)
# ('www.', 'azulschool', '.net')
print('www.azulschool.net'.rpartition('http://')) # Si no se enceuntra, devuelve ('', '', 'str')
# ('', '', 'www.azulschool.net')

# Split
''' str.split(sep=None, maxsplit=-1) '''
print('1\t2\n\n3 4'.split()) # Devuelve una lista de las palabras existentes en la cadena, usando el parámetro sep como delimitador. maxsplit = maximas divisiones
# ['1', '2', '3', '4']
print('1\n2\n\n3\n4'.split('\n')) # Devuelve una lista de las palabras existentes en la cadena, usando el parámetro sep como delimitador. maxsplit = maximas divisiones
# ['1', '2', '', '3', '4']
print('1,2,3'.split(sep=',', maxsplit=1)) # Devuelve una lista de las palabras existentes en la cadena, usando el parámetro sep como delimitador. maxsplit = maximas divisiones
# ['1', '2,3']

# Rsplit 
''' str.rsplit(sep=None, maxsplit=-1) '''
print('1,2,3'.rsplit(sep=',', maxsplit=1)) # Devuelve una lista de las palabras existentes en la cadena, usando el parámetro sep como delimitador, empezando por la derecha. maxsplit = maximas divisiones
# ['1,2', '3']

# Splitlines 
''' str.splitlines([keepends]) '''
# Lista de las líneas en la cadena, rompiendo las mismas en los finales de línea. Se indica el final de linea si keepends==True
print('https\nwww\razulschool\r\nnet'.splitlines()) 
# ['https', 'www', 'azulschool', 'net']
print('https\nwww\razulschool\r\nnet'.splitlines(keepends=True))
# ['https\n', 'www\r', 'azulschool\r\n', 'net']