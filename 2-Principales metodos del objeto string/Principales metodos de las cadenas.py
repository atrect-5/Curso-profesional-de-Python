
# Center
''' str.center(width[, fillchar]) '''
print('something'.center(50, '*'))  # Imprime 'something' centrado en una cadena de 50 de largo entre '*'
#   *********************somthing*********************

# Rjust 
''' str.rjust(width[, fillchar]) '''
print('something'.rjust(50, '>'))   # Imprime 'something' a la derecha de una cadena de 50 con '>' a su izquierda
#   >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>something

# Ljust
''' str.ljust(width[, fillchar]) '''
print('something'.ljust(50, '<'))   # Imprime 'something' a la izquierda de una cadena de 50 con '<' a su derecha
#   something<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# Zfill
''' str.zfill(width) '''
print('12'.zfill(5))    # Imprime 12 completando a 5 con ceros a su izquierda
#   00012
print('-12'.zfill(5))    # Imprime 12 completando a 5 con ceros a su izquierda, despues del '-'
#   -0012

# Strip
''' str.strip([chars]) '''
print('www.azulscool.net'.strip('wnet.'))   # Imprime 'www.azulscool.net' removiendo las coincidencias de los carateres 'w, n, e, t y .' al inicio y final de la cadena
#   azulscool

# Rstrip
''' str.rstrip([chars]) '''
print('www.azulscool.net'.rstrip('wnet.'))   # Imprime 'www.azulscool.net' removiendo las coincidencias de los carateres 'w, n, e, t y .' al final de la cadena
#   www.azulscool