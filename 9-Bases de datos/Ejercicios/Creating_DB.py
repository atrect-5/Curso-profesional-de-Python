# Alejandro Gonzalez

# Ejercio Numero 1
'''Cree una función que reciba el nombre y los campos de una 
base de datos sqlite y cree la misma en caso de que no existan. 
** El primer campo será la PK y los demás serán campos de texto.'''

import sqlite3
from os import path

def create_Database(nameDB, nameTable, campos):
    '''Crea una base de datos, junto con una tabla y campos descritos para dicha tabla'''
    print('\nConectando o creando base de datos...')

    # Creamos la ruta a la base de datos con e lnombre que nos indica el usuario
    dbPath = path.dirname(__file__)+f'\{nameDB}.sqlite3'
    # Hacemos la conexion a la base de datos
    conexion = sqlite3.connect(dbPath)
    '''Esto crea la base de datos en caso de que no exista'''
    # Creamos el cursor
    cursor = conexion.cursor()

    print('Creando la tabla con los campos descritos (si es que la tabla no existe)...\n')
    # Juntammos la lista de campos con el siguiente formato 'campo1 TEXT,'
    campos_query = " TEXT, ".join(campos[1:]) + ' TEXT'
    '''Esto nos permitira crear la base de datos con los campos necesarios'''

    # Creamos la query completa de la base de datos, creando la tabla indicada si es que no existe
    queryTable = f'CREATE TABLE IF NOT EXISTS {nameTable}({campos[0]} integer PRIMARY KEY, {campos_query})'
    '''El 1er campo es 'integer PRIMARY KEY' y los demas son texto'''
    # Ejecutamos la query que diseñamos con los datos dados por el usuario
    cursor.execute(queryTable)

    # Cerramos la conexion a la base de datos 
    cursor.close()
    conexion.close()

if __name__=='__main__':
    # Pedimos los datos al usuario para la base de datos
    nameDB = input('Elija el nombre de su base de datos: -> ')
    nameTable = input('Elija el nombre de la tabla que quiere crear: -> ')
    campos = []
    camposCount = int(input('Cuantos campos tendra la base de datos? (El primero sera \'PRIMARY KEY\'): ->'))
    for i in range(camposCount):
        campos.append(input(f'Ingrese el campo {i+1}: -> '))

    create_Database(nameDB, nameTable, campos)
