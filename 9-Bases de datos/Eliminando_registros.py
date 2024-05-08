import sqlite3
from os import path
dbPath = path.dirname(__file__)+'\pacientes.sqlite3'

conexion = sqlite3.connect(dbPath)
cursor = conexion.cursor()

# Eliminamos registros de id mayor o igual a 5
cursor.execute('DELETE FROM pacientes WHERE id >= 5')

# Imprimimos los registros que fueron afectados por la sentencia ejecutada
print("Registros afectados:", cursor.rowcount)
# Registros afectados: 2

# Confirmamos los cambios
conexion.commit()

# Para confirmar, leemos los registros actuales
cursor.execute('SELECT * FROM pacientes')
registros = cursor.fetchall()

[print(registro) for registro in registros]
# (1, 'Juan', 'Perez', 42, 'Sí')
# (2, 'Jose', 'García', 15, 'No')
# (3, 'Manuel', 'Rodriguez', 50, 'Sí')
# (4, 'Alicia', 'Ramirez', 12, 'No')


cursor.close()
conexion.close()