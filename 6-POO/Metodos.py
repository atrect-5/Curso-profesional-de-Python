
class Persona:
    def saludar(self): # funcion definida dentro de la clase
        print('Hello!')

persona1 = Persona()
persona1.saludar() # Se ejecuta el metodo 'saludar' de la clase en el objeto 'persona1'
# Hello!


class Persona:
    def __init__(self, nombre) -> None: # Se inicializa el nombre de la variable
        self.nombre = nombre
    def presentar(self) -> None: # Aqui se imprime un saludo
        print('Hola, soy', self.nombre, '!')

p1 = Persona('Juan') # Se crean las instancias 
p2 = Persona('David')

# Estas son las dos maneras de llamar al metodo 'presentar'. A esto se refiere el el parametro 'self' que recibe el metodo
p1.presentar()
# Hola, soy Juan !
Persona.presentar(p2) # Se ejecuta el método de la clase pasando la instancia como argumento
# Hola, soy David !


class Punto:
    # Es una convencion que el primer parametro sea 'self', aunque funciona con cualquier nombre. Este hace referencia al objeto que llama al metodo
    def __init__(this, x, y):
            this.x = x
            this.y = y

p1 = Punto(1, 2)
print(p1.x,',', p1.y)
# 1 , 2
