import sqlite3
from os import path
dbPath = path.dirname(__file__)+'\pacientes.sqlite3'

conexion = sqlite3.connect(dbPath)
cursor = conexion.cursor()


#Creamos los valores
valores = (6, "Matias", "Ferreyra", 28, "No")
 
#Insertamos los valores
# Los '?' seran remplazados por los valores de la tupla 'valores'
cursor.execute('INSERT INTO pacientes(id, nombre, apellido, edad, diabetico) VALUES(?, ?, ?, ?, ?)', valores)
 
#confirmamos los cambios
conexion.commit()



cursor.close()
conexion.close()