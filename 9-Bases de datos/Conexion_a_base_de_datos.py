from os import path
dbPath = path.dirname(__file__)+'\pacientes.sqlite3'

# Importamos el modulo 'sqlite3' para poder trabajar con bases de datos 
import sqlite3

# Creamos la conexion a la base de datos
conexion = sqlite3.connect(dbPath)
'''Esto crea un nuevo archivo sqlite3 (base de datos) en la ruta que creamos'''

# Vemos que el tipo de la variable de 'conexion' es de conexion (con la base de datos que creamos)
print(type(conexion)) 
# <class 'sqlite3.Connection'>

# Esto crea un cursor que usaremos para hacer CRUD a nuesta base de datos
cursor = conexion.cursor()
# Vemos que el objeto es de tipo 'cursor'
print(type(cursor)) 
# <class 'sqlite3.Cursor'>


# Se crea una conexion a una base de datos que se crea en la memoria RAM
memoryconexion = sqlite3.connect(':memory:')
'''Esto no nos crea ningun archivo, ya que la base de datos que se crea, trabaja unicamente en la memoria RAM
y desaparece cuando se termina de ejecutar el programa'''

print(type(memoryconexion))
# <class 'sqlite3.Connection'>

