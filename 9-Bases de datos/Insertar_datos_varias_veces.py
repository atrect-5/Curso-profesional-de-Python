import sqlite3
from os import path
dbPath = path.dirname(__file__)+'\pacientes.sqlite3'

conexion = sqlite3.connect(dbPath)
cursor = conexion.cursor()


# Creamos una tabla medicos con los campos id y apellido
cursor.execute('CREATE TABLE if not exists medicos(id integer PRIMARY KEY, apellido text)')
 
# Creamos una lista de datos. Cada elemento es una tupla de valores
data = [(1, "Rodriguez"), (2, "Pérez"), (3, "Álvarez"), (4, "Acevedo")]
 
# Insertamos los valores pasando la lista de valores
'''executemany() ejecutara la sentencia segun la cantidad de elementos de la lista 'data' '''
cursor.executemany("INSERT INTO medicos VALUES(?, ?)", data)
 
# Confirmamos los cambios
conexion.commit()
 
# Imprimimos los datos de la tabla 'medicos' para confirmar
cursor.execute('SELECT * FROM medicos')
registros = cursor.fetchall()
 
[print(registro) for registro in registros]
# (1, 'Rodriguez')
# (2, 'Pérez')
# (3, 'Álvarez')
# (4, 'Acevedo')


cursor.close()
conexion.close()