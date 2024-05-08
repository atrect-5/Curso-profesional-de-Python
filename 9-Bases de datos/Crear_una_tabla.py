import sqlite3
from os import path
dbPath = path.dirname(__file__)+'\pacientes.sqlite3'

# Creamos la conexion y el cursor 
conexion = sqlite3.connect(dbPath)
cursor = conexion.cursor()



# Creamos una tabla en nuestra base de datos con los datos que definimos con el metodo 'execute()'
cursor.execute('CREATE TABLE if not exists pacientes(id integer PRIMARY KEY, nombre text, apellido text, edad integer, diabetico text)')
'''La sentencia 'if not exists', verifica si existe la tabla antes de crearla (Si la intenta crear cuando ya existe, dara un error) '''



# Esto cierra las conexiones a la base de datos
cursor.close()
conexion.close()