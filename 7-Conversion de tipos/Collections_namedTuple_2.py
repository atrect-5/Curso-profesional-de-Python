
from collections import namedtuple
from math import sqrt
 
# Tambien se permite heredar de otras clases
_Punto = namedtuple("_Punto", "x,y,z") 

# class Punto(namedtuple("_Punto", "x,y,z")):  // No es necesario crear una variable, ya que este es su equivalente
class Punto(_Punto):
# No cuenta con un constructor, ya que los atributos se inicializan en la clase padre (_Punto)    

    def distancia(self, otro):
        """ Distancia entre dos puntos """
 
        dif_x = (self.x - otro.x) ** 2
        dif_y = (self.y - otro.y) ** 2
        dif_z = (self.z - otro.z) ** 2
 
        return sqrt(dif_x + dif_y + dif_z) # Retorna la distancia entre 2 puntos
 
if __name__ == '__main__':
    p = Punto(5, 4, 7)
 
    print("p:", p)
    # p: Punto(x=5, y=4, z=7)
    print("distancia:", p.distancia(Punto(8, 4, 9)))
    # distancia: 3.605551275463989


# asdict() Crea un diccionario con los nombres de los atributos (como keys) y sus valores
# Creamos la clase persona con 'namedtuple'
Persona = namedtuple("Persona", "nombre, apellido, genero")
 
if __name__ == '__main__':
    p = Persona("Alex", "Gonzalez", "H")
    dd = p._asdict() 
 
    print(type(dd))
    # <class 'dict'>
 
    for k,v in dd.items():
        print(k, ">>", v)
    # nombre >> Alex
    # apellido >> Gonzalez
    # genero >> H

# _replace() devuelve un nuevo objeto con los valores indicados
Usuario = namedtuple("Usuario", "nombre, mail, clave")

if __name__ == '__main__':
    user = Usuario("atrect5", "atrect5@gmail", "AzulSchool") # Se crea la instancia de 'Usuario'
    user2 = user._replace(mail="atrect5@gmail.com", clave="otraClave") # Modificamos ciertos atributos creando otro objeto
 
    print(user)
    # Usuario(nombre='atrect5', mail='atrect5@gmail', clave='AzulSchool')
    print(user2)
    # Usuario(nombre='atrect5', mail='atrect5@gmail.com', clave='otraClave')
    
    #user.nombre = 'Cambie de nombre'  // Si intentas cambiar el valor de un atributo derectamente...
    # AttributeError: can't set attribute