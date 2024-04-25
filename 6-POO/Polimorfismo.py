
# Se crea la clase base 'Humano'
class Humano:
    def atacar(self):
        print("Puñetazo!")
 
# Se crean las clases hijas de 'Humano'
class Rey(Humano):
    pass
 
class Mago(Humano):
    def atacar(self): # Se modifica el metodo de la clase padre
        print("Hechizo!")
 
class Guerrero(Humano):
    def atacar(self): # Se modifica el metodo de la clase padre
        print("Espada!")
 
# Esta comparacio nos sirve para ejecutar el codigo en caso de que se haya ejecutado este archivo, 
# si este archivo se importo a otro proyecto no se ejecutara lo siguiente en otro proyecto
if __name__ == '__main__':
    # Se crean las intancias de las clases
    humano = Humano()
    rey = Rey()
    mago = Mago()
    guerrero = Guerrero()
 
    # Llamamos el metodo atacar en todos para ver como se comporta el metodo en cada caso (Cuando es modificado y cuando no)
    humano.atacar()
    # Puñetazo!
    rey.atacar()
    # Puñetazo!
    mago.atacar()
    # Hechizo!
    guerrero.atacar()
    # Espada!

'''A esta posibilidad de modificar el funcionamiento de un método de una clase base, se la conoce como Polimorfismo. '''