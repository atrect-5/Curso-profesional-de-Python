
# Upper
'''	str.upper() '''
print("LeTtErs".upper()) #  Imprime 'LeTtErs' con pura mayuscula
# LETTERS

# Lower
'''	str.lower() '''
print("LeTtErs".lower()) #  Imprime 'LeTtErs' con pura minuscula
# letters

# Casefold
''' str.casefold() '''
print('der Fluß'.casefold()) #  Imprime la version minuscula de otras letras en otros idiomas
# der fluss

# Swapcase
''' str.swapcase() '''
print('AZUL school'.swapcase()) #   Cambia de lugar mayusculas y minusculas
# azul SCHOOL

# Title
''' str.title() '''
print('UnA lInea laRGA'.title()) #  Inicia cada palabra con mayuscula y lo demas en miniscula
# Una Linea Larga

# Capitalize
''' str.capitalize() '''
print('UnA lInea laRGA'.capitalize()) #  Inicia toda la oracion con mayuscula y lo demas en miniscula
# Una linea larga

# Find
''' str.find(sub[, start[, end]]) '''
print('Avada Kedavra'.find('v')) #  Imprime la posicion donde encuentra la 'v'
# 1
print('Avada Kedavra'.find('v', 3, 11)) #    Busca en el rango que se le indica (-1 si no se enceuntra)
# 10 

# Rfind
''' str.rfind(sub[, start[, end]]) '''
print('Avada Kedavra'.rfind('v')) #  Imprime la posicion donde encuentra la 'v' (Buscando desde la derecha)
# 10

# index
''' str.index(sub[, start[, end]]) '''
print('Avada Kedavra'.index('v')) #  Imprime la posicion donde encuentra la 'v'
# 1
print('Avada Kedavra'.index('v', 3, 11)) #    Busca en el rango que se le indica (ValueError si no se enceuntra)
# 10 

# Rindex
''' str.rindex(sub[, start[, end]]) '''
print('Avada Kedavra'.rindex('v')) #  Imprime la posicion donde encuentra la 'v' (Buscando desde la derecha)
# 10


