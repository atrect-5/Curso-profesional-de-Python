

class Guerrero:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vida = 100
    
    # Se accede al metodo cuando una instancia es mandada con el metodo bool()
    def __bool__(self):
        return True if self.vida > 0 else False
 

if __name__ == '__main__':
    # bool() sobreescribiendo el metodo en la clase
    g1 = Guerrero("Thor")

    print(bool(g1))
    # True

    g1.vida = 0
    print(bool(g1))
    # False
    
    # uso comun de bool()
    v1 = bool(15)
    v2 = bool(0)
 
    print(v1, v2)
    # True False