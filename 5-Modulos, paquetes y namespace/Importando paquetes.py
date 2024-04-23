
# Se importa el modulo 'sys'
import sys

# Se agrega a la lista de rutas la ruta en donde se encuentra nuestro paquete con el modulo que queremos importar
sys.path.insert(1, r'C:\Users\alex1\School Files\Curso profesional de python')  # No incluimos nuestro paquete en la ruta

# Aqui importamos la funcion de 'Operacion' de nuestro modulo 'MetodosOperaciones' que se encuentra en el paquete 'OperacionesPaq'
from OperacionesPaq.MetodosOperaciones import Operacion

# Imprimimos los metodos a los que tenemos acceso en el namespace
print(dir())
# ['Operacion', '__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'sys']
'''Podemos ver que tenemos acceso a la funcion "Operacion" que es la que importamos de nuestro paquete'''

# Imprimimos la suma de unos numeros usando la funcion que importamos del paquete de modulos
print(Operacion(2, 3, 4, operacion="suma"))
# 9

# Imprimimos el producto de unos numeros usando la funcion que importamos del paquete de modulos
print(Operacion(2, 3, 4, operacion="producto"))
# 24


# Tambien se pueden hacer importaciones del tipo :

'''Importando paquete'''
import OperacionesPaq
'''importando un modulo de un paquete'''
import OperacionesPaq.MetodosOperaciones as MO
'''De eta misma manera, se puede acceder a sub paquetes dentro de otros paquetes'''

# Accediendo a una funcion del modulo
print(MO.SumaArgs(1,2,3,4))
# 10

# Accediendo a una funcion de un modulo ubicado en un paquete
print(OperacionesPaq.MetodosOperaciones.Producto(1,2,3,4))
# 24