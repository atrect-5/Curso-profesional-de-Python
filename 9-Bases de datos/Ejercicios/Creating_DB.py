# Alejandro Gonzalez

#region Ejercio Numero 1
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
#endregion
#region Ejercicio numero 2
'''Cree una función que reciba el nombre, la tabla, y los campos 
de una base de datos y devuelva los registros de la misma como una lista.
la función debe recibir, de manera opcional, el criterio de filtro para obtener los registros.'''

def read_Database(nameDB, nameTable, campos:list, campoFiltro, Filtro):
    print('\nConectando a la base de datos...') 
    # Creamos las conexiones
    dbPath = path.dirname(__file__)+f'\{nameDB}.sqlite3'
    conexion = sqlite3.connect(dbPath)
    cursor = conexion.cursor()

    # Definimos las partes de la query
    sqlGetCampos = ', '.join(campos)
    sql = f'SELECT {sqlGetCampos} FROM {nameTable}'
    if campoFiltro:
        sqlWhere = f' WHERE {campoFiltro}="{Filtro}"'
        sql += sqlWhere

    cursor.execute(sql)
    registros = cursor.fetchall()

    # Cerramos la conexion a la base de datos 
    cursor.close()
    conexion.close()
    return registros
#endregion
# Ejercicio Numero 3
'''Cree una función que reciba el nombre de un archivo csv con campos separados 
por punto y coma y el nombre y tabla de una base de datos. Con ellos, debe insertar 
todos los registros del archivo en la base de datos y tabla indicada. Lo campos 
de la base de datos estarán en la primera fila del archivo.'''

import csv # Importamos la libreria csv
def read_csv(nameDB, nameTable, archivoCSV):
    #region Conectando a la base de datos...
    print('\nConectando a la base de datos...') 
    # Creamos las conexiones
    dbPath = path.dirname(__file__)+f'\{nameDB}.sqlite3'
    conexion = sqlite3.connect(dbPath)
    cursor = conexion.cursor()
    #endregion
    print('Accediendo al archivo csv...')
    # Creamos la ruta al archivo csv
    csvPath = path.dirname(__file__)+f'\{archivoCSV}'

    # Abrimos el archivo indicado
    with open(csvPath, encoding="utf-8") as csvFile:
        print(f'Los datos obtenidos del archivo {archivoCSV} fueron:\n', csvFile.read())
        csvFile.seek(0) # Reiniciamos el puntero del archivo despues de leer

        print('\nEscribiendo datos en la base de datos...\n')
        # Obtenemos los datos del archivo en un 'DictReader'
        csvDictReader = csv.DictReader(csvFile, delimiter=';')

        # Iteramos en las filas leidas del archivo con 'DictReader'
        for fila in csvDictReader:
            # Definimos la sentencia sql y ejecutamos
            sql = f'INSERT INTO {nameTable} VALUES({fila["id"]}, "{fila["nombre_completo"]}", "{fila["apellido_paterno"]}", "{fila["apellido_materno"]}", "{fila["anyo_nacimiento"]}")'
            cursor.execute(sql)

    # Confirmamos los cambios a la base de datos
    conexion.commit()

    #region Cerramos la conexion a la base de datos 
    cursor.close()
    conexion.close()
    #endregion

if __name__=='__main__':
    #region Pedimos los nombres de la base de datos, la tabla y la accion que desea realizar
    nameDB = input('Cual es el nombre de su base de datos?: -> ')
    nameTable = input('Cual el nombre de la tabla: -> ')
    
    print('Que desea hacer con la base de datos?')
    opcion = input('(C)-Crear Tabla\n(R)-Leer Registros de una tabla\n(IC)-Insertar datos desde archivo csv\n-> ')
    #endregion
    
    if (opcion=='C'):
        campos = []
        camposCount = int(input('Cuantos campos tendra la base de datos? (El primero sera \'PRIMARY KEY\'): ->'))
        for i in range(camposCount):
            campos.append(input(f'Ingrese el campo {i+1}: -> '))
        create_Database(nameDB, nameTable, campos)
    elif(opcion=='R'):
        # Tomaos los datos restantes del usuario (campos que quiere obtener y el filtro que quiere aplicar)
        campos = []
        camposCount = input('Cantidad de campos quiere obtener de la base de datos(* para todos): -> ')
        if camposCount != '*':
            for i in range(int(camposCount)):
                campos.append(input(f'Ingrese el campo {i+1}: -> '))
        else:
            campos.append(camposCount)
        Filtro = ''
        campoFiltro = input('Que campo quiere filtrar (Enter si no quiere filtrar): -> ')
        if campoFiltro:
            Filtro = input(f'Solo buscar en los registros que {campoFiltro} = ? : -> ')
        # Llamamos a la funcion de leer registros y obtenemos la lista de registros leidos
        registros = read_Database(nameDB, nameTable, campos, campoFiltro, Filtro)
        [print(registro) for registro in registros]
    elif(opcion=='IC'):
        archivoCSV = input('Cual es el nombre del archivo csv?: -> ')
        read_csv(nameDB, nameTable, archivoCSV)