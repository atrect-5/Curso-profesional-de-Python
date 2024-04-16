
# Replace
''' str.replace(old, new[, count]) '''
# Devuelve una cadena reemplazando todas las apariciones de la subcadena ‘old‘ reemplazadas por la nueva ‘new‘,  'count' veces.
print("Azul Web Web Web".replace("Web", "School", 2))
# Azul School School Web


# Format
''' str.format(*args, **kwargs) '''
# Remplaza los campos delimitados por llaves {}, por el elemento de la clave que contienen las llaves.
print('El resultado de {0}*{1} es {2}.'.format(2,5,2*5)) # {0}, {1} y {2} son sustituidos por sus pocisiones en los parametros de .format()
# El resultado de 2*5 es 10.
print('{0}'.format(3/7)) # También se puede definir el formato del remplazo
# 0.42857142857142855
print('{0:.1f}'.format(3/7)) # ‘.1‘ significa que se redondee a la décima más próxima, El especificador ‘f‘ indica que el número debe mostrarse con formato de punto flotante
# 0.4


# Format_map
''' str.format_map(mapping) '''
# Es parecido a format, pero las claves de remplazo deben tener las claves que estan en el parametro.
claves = {'prefijo': 'https://www.', 'sufijo':'.net'} # Se hace un diccionario con las claves
print('{prefijo}azulschool{sufijo}'.format_map(claves)) # Se usan las claves y se aplican los valores del diccionario
# https://www.azulschool.net


# Encode
''' str.encode(encoding="utf-8", errors="strict") '''
# En utf-8 los caracteres pertenecientes a la tabla ASCII son guardados en un solo byte, aquellos que no pertenecen a esta tabla son guardados en 2 bytes
print('El niño está en la escuela'.encode('utf-8')) 
# El ni\xc3\xb1o est\xc3\xa1 en la escuela


# Decode
''' bytes.decode(encoding="utf-8", errors="strict") '''
''' bytearray.decode(encoding="utf-8", errors="strict") '''
# Devuelve una cadena decodificada de los bytes dados, donde la codificación predeterminada es ‘utf-8’. 
print(b'El ni\xc3\xb1o est\xc3\xa1 en la escuela'.decode("utf-8"))
# El niño está en la escuela