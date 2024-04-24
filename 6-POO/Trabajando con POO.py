

# DEFINICION DE CLASES //////
# Se define una clase con la palabra reservada 'class' 
class Objeto:
    def __init__(self) -> None: # Este es el 'constructor', cuando se crea un objeto se ejecuta esta parte
        print("Inicializando objeto...")

object = Objeto() # Podemos ver que al crear una instancia de nuestra clase, se llama al metodo __init__
# Inicializando objeto...
print(type(object))
# <class '__main__.Objeto'>



# VARIABLES DE INSTANCIA //////
class Persona:
    def __init__(self, variable_nombre, variable_edad) -> None: 
        self.nombre = variable_nombre # Se delcara que tendran un tipo de dato llamado 'nombre', que valdra lo que se reciba en la funcion (igual con 'edad')
        self.edad = variable_edad # Normalmente los parametros recibidos por la funcion se llaman igual que los atributos de las instancias, pero en este caso queremos diferenciarlos

persona1 = Persona('Eduardo', 40) # Se crean dos instancias de la clase 'Persona'
persona2 =Persona(variable_nombre='Samuel', variable_edad=18)

'''Observamos como cada objeto se queda con sus respectivos valores'''
print(persona1.nombre)
# Eduardo
print(persona2.edad)
# 18


# VARIABLES DE CLASE //////
class Automovil:
    ruedas = 4 # Esta variable tendra el mismo valor para cada instancia de la clase
    def __init__(self, marca, color) -> None:
        self.marca = marca
        self.color = color

auto1 = Automovil('Ford', 'Blanco')
auto2 = Automovil('Kia', 'Azul')

# Podemos observar que el numero de ruedas es el mismo para los dos auutos
print("Auto 1 : ", auto1.marca, '| No. Ruedas : ', auto1.ruedas)
# Auto 1 :  Ford | No. Ruedas :  4
print("Auto 2 : ", auto2.marca, '| No. Ruedas : ', auto2.ruedas)
# Auto 2 :  Kia | No. Ruedas :  4

# Precausiones a tomar en cuenta :
class Perro:
    trucos = [] # Aqui se hace una lista de los trucos que se aprenden
    def __init__(self, nombre) -> None:
        self.nombre = nombre
# Creamos 2 objetos con nuestra clase 'Perro'
perro1 = Perro('Firulais')
perro2 = Perro('SoloVino')

# Le agregamos un truco a cada perro
perro1.trucos.append('Rodar')
perro2.trucos.append('Dar la pata')

# Aunque le agreguemos un truco a cada uno, ambos tendran los mismos ya que se trata de una variable de clase y no de instancia
print('Perro 1 : ', perro1.nombre, '| Trucos : ', perro1.trucos)
# Perro 1 :  Firulais | Trucos :  ['Rodar', 'Dar la pata']
print('Perro 2 : ', perro2.nombre, '| Trucos : ', perro2.trucos)
# Perro 2 :  SoloVino | Trucos :  ['Rodar', 'Dar la pata']