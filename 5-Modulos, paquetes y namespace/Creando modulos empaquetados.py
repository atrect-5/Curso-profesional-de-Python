
# Se importa el modulo 'sys'
import sys 
if input() == 'y': # Si se escribe 'y', se imprime la documentacion de 'sys'
   print(sys.__doc__)
# This module provides access to some objects used or maintained by the interpreter and to functions that interact strongly with the interpreter.

# Se busca imprimir la lista de los lugares de busqueda cuando importas un modulo
for ruta in sys.path:
    print(ruta)
# c:\Users\alex1\School Files\Curso profesional de python\5-Modulos, paquetes y namespace
# C:\Users\alex1\AppData\Local\Programs\Python\Python311\python311.zip
# C:\Users\alex1\AppData\Local\Programs\Python\Python311\DLLs
# C:\Users\alex1\AppData\Local\Programs\Python\Python311\Lib
# C:\Users\alex1\AppData\Local\Programs\Python\Python311
# C:\Users\alex1\AppData\Local\Programs\Python\Python311\Lib\site-packages 
'''Podemos ver que el primero es la carpeta en la que nos encontramos actualmente'''
print('________________________________________')

# Se agrega a la lista de rutas la ruta en donde se encuentra nuestro proyecto con el modulo que queremos importar
sys.path.insert(1, r'C:\Users\alex1\School Files\Curso profesional de python\Operaciones')

# Se busca imprimir la lista de los lugares de busqueda cuando importas un modulo
for ruta in sys.path:
    print(ruta)
# c:\Users\alex1\School Files\Curso profesional de python\5-Modulos, paquetes y namespace
# C:\Users\alex1\School Files\Curso profesional de python\4-Funciones definidas por el usuario
# C:\Users\alex1\AppData\Local\Programs\Python\Python311\python311.zip
# C:\Users\alex1\AppData\Local\Programs\Python\Python311\DLLs
# C:\Users\alex1\AppData\Local\Programs\Python\Python311\Lib
# C:\Users\alex1\AppData\Local\Programs\Python\Python311
# C:\Users\alex1\AppData\Local\Programs\Python\Python311\Lib\site-packages
'''Vemos que se agrego correctamente la ruta'''

# Se importa el modulo de 'MetodosOperaciones' que contiene los modulos que hicimos en : Modulo 4 \ Argumentos_variables 
# (Se creo una carpeta nueva que solo contiene las funciones)
import MetodosOperaciones
print(dir(MetodosOperaciones))
# ['OPERACIONES', 'Operacion', 'Producto', 'Suma', 'SumaArgs', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']
'''Como podemos ver, tenemos acceso a las funciones que hay en dicho modulo'''