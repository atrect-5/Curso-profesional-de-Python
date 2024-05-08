import sqlite3, csv # El modulo 'csv' nos permite leer la informacion de 'pacientes.txt' como si se tratase de una tabla
from os import path
dbPath = path.dirname(__file__)+'\pacientes.sqlite3'
pacientestxtPath = path.dirname(__file__)+'\pacientes.txt'

# Creamos la conexion y el cursor 
conexion = sqlite3.connect(dbPath)
cursor = conexion.cursor()

# Datos en nuestro archivo pacientes.txt
'''
id;apellido;nombre;edad;diabetico
1;Juan;Perez;42;Sí
2;Jose;García;15;No
3;Manuel;Rodriguez;50;Sí
4;Alicia;Ramirez;12;No
5;Lucas;Lucyk;25;No
'''

#abrimos el archivo en modo lectura con codificacion utf-8
with open(pacientestxtPath, encoding="utf-8") as f:
 
    #utilizamos el método DictReader del módulo csv.
    #El mismo nos devuelve un objeto DictReader () que podemos iterarlo como a una lista
    cf = csv.DictReader(f, delimiter=';')
 
    #Recorremos todos los elementos devueltos por DictReader
    for fila in cf:
 
        #Creamos una sentencia sql accediendo al valor de cada columna en cada una de las filas
        sql = f'INSERT INTO pacientes values({fila["id"]}, "{fila["apellido"]}", "{fila["nombre"]}", {fila["edad"]}, "{fila["diabetico"]}")'
         
        #Imprimimos la sentencia sql creada
        print(sql)
        # INSERT INTO pacientes values(1, "Juan", "Perez", 42, "Sí")
        # INSERT INTO pacientes values(2, "Jose", "García", 15, "No")
        # INSERT INTO pacientes values(3, "Manuel", "Rodriguez", 50, "Sí")
        # INSERT INTO pacientes values(4, "Alicia", "Ramirez", 12, "No")
        # INSERT INTO pacientes values(5, "Lucas", "Lucyk", 25, "No")
 
        #ejecutamos la sentencia sql
        cursor.execute(sql)
 
#confirmamos los cambios
conexion.commit()
 


cursor.close()
conexion.close()