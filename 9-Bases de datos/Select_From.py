import sqlite3
from os import path
dbPath = path.dirname(__file__)+'\pacientes.sqlite3'

conexion = sqlite3.connect(dbPath)
cursor = conexion.cursor()

# Realizamos nuestra query sql para obtener los datos de la base de datos
cursor.execute('SELECT * FROM pacientes')
# Con 'fetchall' obtenemos los resultados devueltos en una lista
registros = cursor.fetchall()

# Recorremos e imprimimos todos los registros
[print(registro) for registro in registros]
# (1, 'Juan', 'Perez', 42, 'Sí')
# (2, 'Jose', 'García', 15, 'No')
# (3, 'Manuel', 'Rodriguez', 50, 'Sí')
# (4, 'Alicia', 'Ramirez', 12, 'No')
# (5, 'Lucas', 'Lucyk', 25, 'No')
# (6, 'Matias', 'Ferreyra', 28, 'No')


# Modificando el query sql, podemos obtener resultados especificos
# Obtenemos unucamente el 'id', 'nombre' y 'apellido' de los pacientes diabeticos
cursor.execute('SELECT id, nombre, apellido FROM pacientes WHERE diabetico="Sí"')
registros = cursor.fetchall()

[print(registro) for registro in registros]
# (1, 'Juan', 'Perez')
# (3, 'Manuel', 'Rodriguez')

cursor.close()
conexion.close()