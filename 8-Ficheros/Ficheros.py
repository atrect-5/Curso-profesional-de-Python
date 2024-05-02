

# Obtenemos la direccion en la que se encuentra nuestro programa .py y buscamos en esta direccion al archivo 'lorem.txt'
'''Esto porque VScode busca en el directorio que estas trabajando y no donde se ejecuta el programa, lo que ocacionaba que no se encontrara
el archivo 'lorem.txt' '''
from os import path
lorem = path.dirname(__file__)+'\lorem.txt'


# OPEN()
# Se abre el ducumento guardado en dicha carpeta
file = open(lorem)
print(type(file))
# <class '_io.TextIOWrapper'>
file.close() # Se cierra el archivo (Si no, mientras el codigo se ejecute y no se cierre el archivo no se podra acceder al documento)


# READ()
file = open(lorem)
# read() nos regresara la informacion contenida en nuestro archivo
print(file.read(50)) #primeros 50 caracteres
print(file.read(50)) #Siguientes 50 caracteres
print(file.read()) #Todo el contenido restante
file.close()


# TELL() & SEEK()
file = open(lorem)
 
print("posición 1:", file.tell())
# posición 1: 0
print(file.read(50))    #primeros 50 caracteres
 
#vemos la posición actual y nos desplazamos al inicio
print("posición 2:",file.tell())
# posición 2: 50
file.seek(0)
print("posición 3:",file.tell())
# posición 3: 0
 
print(file.read(50))    #primeros 50 caracteres
print("posición 4:",file.tell())
# posición 4: 50
file.close()


# SEEKEABLE() READEBLE() WRITEABLE()
file = open(lorem)

print("Es seekable?:", file.seekable()) # Checamos si podemos definir nuestra posicion en el archivo
# Es seekable?: True
file.seek(50)
print("Posición:", file.tell())
# Posición: 50
print("Es readable?:", file.readable()) # Checamos si podemos leer el archivo
# Es readable?: True
print(file.read(50))
#  elit, sed do eiusmod tempor incididunt ut labore

print("Es writable?:", file.writable()) # Checamos si podemos escribir el archivo
# Es writable?: False
try:
    pass
    #print(file.write("Escribo contenido..."))
    # io.UnsupportedOperation: not writable
finally:
    file.close()


# Para hacer que si se pueda escribir:
file = open(lorem, "a+") # indicamos que queremos escribir el archivo al final (a+)
print("Es writable?:", file.writable())
# Es writable?: True
cadena = 'Queso' 
file.write(cadena) # Escribimos nuestro archivo
 
#nos desplazamos al comienzo de la cadena agregada con:
#posició actual + largo de lectura hasta el final - el largo de la cadena creada
file.seek(file.tell() + len(file.read()) - len(cadena))

#leemos e imprimimos desde dicha posición
print(file.read())
# Queso

file.close()