# Alejando Gonzalez

# Paso numero 3 del ejercicio de 'Modulos, paquetes y namespace'
'''Cree un nuevo programa en otro directorio y, utilizando el módulo sys 
y su atributo path, agregue el directorio del paso anterior al camino de 
búsqueda de import. Luego, importe el módulo operaciones.py con el alias 
op.'''

import sys
# Agregamos la ruta de nuestro mosulo que contiene las funciones: 'Suma, Resta, Producto, Division'
sys.path.insert(1,r'C:\Users\alex1\School Files\Curso profesional de python\5-Modulos, paquetes y namespace\Ejercicios\Modulo_Para_Importar_Python')