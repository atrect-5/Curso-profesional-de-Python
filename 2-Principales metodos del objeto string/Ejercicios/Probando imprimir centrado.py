# Alejandro Gonzalez


# Se imprime la palabla 'centrado' en el centro de un determinado numero de caracteres
cadena = 'centrado'
separadores = int(input('Cantidad de caracteres donde se centrara la palabra : '))
print((cadena.rjust(separadores+len(cadena), '>')).ljust((2*separadores)+len(cadena), '<'))