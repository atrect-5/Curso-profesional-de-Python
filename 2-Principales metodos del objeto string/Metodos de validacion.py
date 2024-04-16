
# Endswith
''' str.endswith(suffix[, start[, end]]) '''
print('www.azulschool.net'.endswith(('.net', '.com'))) #    Busca que termine con .com o .net 
# True

# Isalpha
''' str.isalpha() '''
print('Python'.isalpha()) # checa si 'Python' Son puras letras
# True
print('Python 3'.isalpha()) # checa si 'Python 3' Son puras letras
# False

# Isascii
''' str.isascii() '''
print('n'.isascii()) # Evalua si 'n' es ascii
# True
print('ñ'.isascii()) # Evalua si 'ñ' es ascii (rango ascii = U+0000-U+007F)
# Flase

# Isdecimal
''' str.isdecimal() '''
print('30'.isdecimal()) # Evalua si '30' es decimal (numero)
# True
print('-30'.isdecimal()) # Evalua si '-30' es decimal (numero)
# False

# Isdigit
''' str.isdigit() '''
print('𐩁'.isdigit()) # Evalua si '𐩁' es un digito (Toma en cuenta los números del sistema Kharosthi)
# True

# Isnumeric
''' str.isnumeric() '''
print('\u00BD'.isnumeric()) # Evalua si se traa de un numero o no (también reconoce fracciones vulgares de Unicode)
# True
print('½'.isnumeric()) # Evalua si se traa de un numero o no 
# True

# Isidentifier
''' str.isidentifier() '''
print('22_var_name'.isidentifier()) # Evalua si se trata de un identificador valido (define si puedes utilizar dicho valor como nombre para de variable)
# False
print('var_name'.isidentifier()) # Evalua si se trata de un identificador valido
# True

# Islower
''' str.islower() '''
print('MiNusCuLas'.islower()) # Evalua si los caracteres de la cadena son todos minusculas
# False
print('minusculas'.islower()) # Evalua si los caracteres de la cadena son todos minusculas
# True

# Isprintable
''' str.isprintable() '''
print('\n'.isprintable()) # Evalua si se trata de caracteres que se pueden imprimir visiblemente
# False
print('\ '.isprintable()) # Evalua si se trata de caracteres que se pueden imprimir visiblemente
# True

# Isspace
''' str.isspace() '''
print(' \n\t'.isspace()) # Devuelve True en la cadena solo hay caracteres espaciadores y hay -al menos- un carácter, False de lo contrario. 
# True
print('Python \n\t3'.isspace()) # Devuelve True en la cadena solo hay caracteres espaciadores y hay -al menos- un carácter, False de lo contrario. 
# False

# Istitle
''' str.istitle() '''
print('Nuevo Curso De Python 3'.istitle()) # Evalua si la cadena tiene un formato de titulo
# True
print('PyThon 3'.istitle()) # Evalua si la cadena tiene un formato de titulo
# False

#Isupper
''' str.isupper() '''
print('MaYuScUlas'.isupper()) # Evalua si los caracteres de la cadena son todos mayusculas
# False
print('MAYUSCULAS'.isupper()) # Evalua si los caracteres de la cadena son todos mayusculas
# True

# Isalnum
''' str.isalnum() '''
print('Python 3'.isalnum()) # Evalua si se trata de carateres alpha numericos (numeros y letras)
# False
print('Python3'.isalnum()) # Evalua si se trata de carateres alpha numericos (numeros y letras)
# True