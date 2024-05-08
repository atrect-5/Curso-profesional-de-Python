import sqlite3
from os import path
dbPath = path.dirname(__file__)+'\pacientes.sqlite3'

conexion = sqlite3.connect(dbPath)
cursor = conexion.cursor()


# Eliminamos la tabla 'pacientes' Si es que existe
cursor.execute('DROP TABLE if exists pacientes')

# Imprimimos los valores obtenidos para confirmar
cursor.execute('SELECT name from sqlite_master where type= "table"')
registros = cursor.fetchall()

[print(registro) for registro in registros]
# 

cursor.close()
conexion.close()