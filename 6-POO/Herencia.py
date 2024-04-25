
# Definimos una clase base
class Persona:
    def hablar(self, mensaje):
        print(mensaje)

    def __init__(self, nombre) -> None:
        self.nombre = nombre

# Definimos la clase hija que esta vacia, pero hereda de la clase 'Persona'
class Profesor(Persona):
    pass

# Definimos un objeto de cada clase
persona = Persona('')
profesor = Profesor('Hector')
# Utilizamos el metodo de la clase padre para ambos objetos (El de la clase hija, tiene acceso a los metodos del padre), asi como los atributos (nombre en este caso)
persona.hablar('Hola mundo!')
# Hola mundo!
profesor.hablar('Hola aLumnos!')
# Hola aLumnos!
print(profesor.nombre)
# Hector



# Definimos una clase de la localizacion de un punto con coordenadas
class Punto:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

# Definimos una clase hijo que hereda de 'Punto' 
class Circulo(Punto):
    # Definimos un metodo '__init__' para nuestra clase hijo
    def __init__(self, x, y, radio) -> None: # Recibe los parametros que recibe '__init__' en la clase padre, mas los parametros de esta clase
        super().__init__(x, y) # Llama al constrcutos (__init__) de la clase padre, mandandole los parametros recibidos
        self.radio = radio # Se continua con la declaracion propia de la clase hijo

# Se declara una variable de tipo circulo (instancia de clase)
c = Circulo(x=2, y=7, radio=5) # Tiene los atributos de la clase padre y la clase propia (hijo)
print('x : ', c.x, ' | y : ', c.y, ' | redio : ', c.radio)
# x :  2  | y :  7  | redio :  5