
# Importamos las clases del modulo de 'Polimorfismo.py' que vamos a utilizar 
from Polimorfismo import Mago, Guerrero
 
# Se crea una clase que hereda de 2 clases padres
class Brujo(Mago, Guerrero):
    pass
 
if __name__ == '__main__':
    # Se crea una instancia de clase 'Brujo'
    brujo = Brujo()
    '''Al no tener el metodo 'atacar', utilizara el metodo del padre.
    En este caso, primero usara el metodo 'atacar' que se encuentre en el 
    primer padre ('Mago'), en caso de que el primer padre no contenga un metodo 
    'atacar', lo buscara en su segundo padre'''
    brujo.atacar() # Usa el metodo atacar del primer padre, (del segundo si este no tuviera o el "abuelo" si ningun padre lo tuviese)
    # Hechizo!

    # Aqui se imprime el orden en que busca un metodo de la clase para ser ejecutado cuando se usa
    print(Brujo.__mro__)
    # (<class '__main__.Brujo'>, <class 'Polimorfismo.Mago'>, <class 'Polimorfismo.Guerrero'>, <class 'Polimorfismo.Humano'>, <class 'object'>)