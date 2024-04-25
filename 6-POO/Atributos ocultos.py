
# Creamos una clase
class Perosna:
    def __init__(self, nombre, secreto) -> None:
        self.nombre = nombre
        self._secreto = secreto # Al colocar el '_' antes del atributo, indiica que es un atributo privado

# Creamos la instancia de la clase
persona = Perosna('Juan','Prefiere Java')
# Vemos que aunque el atributo sea 'privado', se puede acceder con normalidad
print('Nombre: ', persona.nombre, '\nSecreto: ', persona._secreto)
# Nombre:  Juan 
# Secreto:  Prefiere Java


'''Los atributos privados suelen ser útiles para evitar colisiones cuando poseemos un método con el mismo nombre que el atributo.'''
# Clase con un atributo '_contenido' y un metodo 'contenido', diferenciados por el '_' del atributo (privado)
class Canasta:
 
    CAPACIDAD_MAXIMA = 10 # Capacidad maxima igual para todos los objetos
 
    def __init__(self, contenido):
        self._contenido = contenido # Se inicializa el contenido con el que se le indica (Se indica como privado para diferenciarlo del metodo)
 
    def contenido(self):
        return min(self.CAPACIDAD_MAXIMA, self._contenido) # Limita el contenido a la capacidad maxima (En caso de que se pase) o retorna el valor original
 
c = Canasta(5)
cc = Canasta(15)

# Se llama al metodo de la clase
print("c:", c.contenido())
# 5
print("cc:", cc.contenido())
# 10

'''Los atributos ocultos están pensados para que no sean accedidos desde fuera de la definición de la clase'''
# Se define iuna clase con un atribubto 'oculto'
class Usuario:
    def __init__(self, nombre, contenido_premium):
            self.nombre = nombre
            self.__contenido_premium = contenido_premium # Al iniciar el nombre con '__' (2*'_') oculta dicho atributo

user = Usuario("Lucas Lucyk", "Curso de Python")
print('Nombre: ',user.nombre)
# Lucas Lucyk

# Si intentaramos acceder al atributo oculto desde la instancia de la clase (siguiente linea comentada), nos ocasionaria un error
#print(user.__contenido_premium)
# AttributeError: 'Usuario' object has no attribute '__contenido_premium'.
'''Al crear el atributo __contenido_premium, el mismo es automáticamente renombrado a '_Usuario__contenido_premium' '''

# Usando el nombre redefinido del atributo, podemos acceder a el
print(user._Usuario__contenido_premium)
# Curso de Python