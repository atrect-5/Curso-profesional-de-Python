
# importamos el modulo de 'datetime' a nuestro proyecto
import datetime as dt  
'''Al agregarle 'as', ahora el modulo importado tengra el nombre 'dt' dentro del namespace local'''

print(dir(dt)) # Se imprimen todos los atributos de nuesto modulo importado
# ['MAXYEAR', 'MINYEAR', 'UTC', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']

print(dt.date.today.__doc__) # Al poner '.' accedemos a metodos de un modulo, con __doc__ accedemos a la documentacion para ver que hace el metodo
# Current date or datetime:  same as self.__class__.fromtimestamp(time.time()).
print(dt.date.today()) # Vemos que es lo que nos imprime realmente (la fecha de hoy)
# 2024-04-23


'''Se debe tener cuidado con el nombre asignado a la variables, ya que 
en Python podemos crear una variable con un nombre y luego reutilizarlo 
para asignar cualquier otro tipo de dato.'''
var = 5
print(type(var)) # Imprimimos el tipo de datos de nuestra variable 'var'
# <class 'int'>
var = 'Hello'
print(type(var)) # Cambiamos el tipo de dato del valor asignado e imprimimos otra vez el tipo
# <class 'str'>