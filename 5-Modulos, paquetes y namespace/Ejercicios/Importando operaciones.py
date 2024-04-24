# Alejando Gonzalez

# Paso numero 3 del ejercicio de 'Modulos, paquetes y namespace'
'''Cree un nuevo programa en otro directorio y, utilizando el módulo sys 
y su atributo path, agregue el directorio del paso anterior al camino de 
búsqueda de import. Luego, importe el módulo operaciones.py con el alias 
op.'''

import sys
# Agregamos la ruta de nuestro mosulo que contiene las funciones: 'Suma, Resta, Producto, Division'
sys.path.insert(1,r'C:\Users\alex1\School Files\Curso profesional de python\5-Modulos, paquetes y namespace\Ejercicios\Modulo_Para_Importar_Python')
# importamos nuestro modulo con las funciones que utilizaremos
import Modulo_Para_Importar_Python.Operaciones as Operaciones 

# Siguiente paso : 
'''Utilizando el módulo operaciones y siguiendo en el mismo ejercicio anterior, 
utilice la función input, para solicitar un número variable de valores separados 
por coma y luego imprima la sumatoria, resta, producto y división de los mismos 
utilizando el módulo importado.'''

lista_Str = input('Ingrese una lista de numeros separados por \",\" (sin espacios) : ') # Pedimos que se ingrese la lista de numeros
# Convertimos la cadena que se ingreso en una lista de numeros
lista_Num = [int(num) for num in lista_Str.split(',') if num.isnumeric()]

# Imprimimos los valores de los resultados usando las funciones que declaramos en el otro proyecto que importamos
print('La Suma de los numeros ingresados es : ', Operaciones.Suma(*lista_Num))
print('La Resta de los numeros ingresados es : ', Operaciones.Resta(*lista_Num))
print('El Producto de los numeros ingresados es : ', Operaciones.Producto(*lista_Num))
print('La Division de los numeros ingresados es : ', Operaciones.Division(*lista_Num))