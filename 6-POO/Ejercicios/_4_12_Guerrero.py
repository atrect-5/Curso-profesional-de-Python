# Alejandro Gonzalez : Ejercicios Propuestos

# Ejercicios Propuestos 4-12, Ejercicios Opcionales 1-5

class Guerrero: # Definimos la clase y las variables de clase 'vida' y 'estado_arma' con sus valores (Ej. 4)
   
    def __init__(self, name) -> None:
        self.name = name # Esta propiedad es para identificar al guerrero (Yo)
        self.vida = 100
        self.estado_arma = 100
        # Creamos un nuevo atributo con los puntos del estado del escudo (Ej.10)
        self.estado_escudo = 100

    # Definimos el metodo 'atacar' que le quita 20 de vida al objeto que recibe (Ej. 5)
    def atacar(self, another): 
        # Se comprueba que el Guerrero este con vida para poder atacar (Ej. 12.e)
        if not self.isalive:
            print('El Guerrero', self.name, 'no puede atacar, ya que esta muerto')
            return
        # Se agrega el estado en el que esta el guerrero (Atacando o defendiendo) (Ej.9)
        self.set_estado()
        # Si el atacante esta en modo de 'defensa', no podra atacar (Ej. 12.d)
        if self.estado_actual == 'defensa':
            print('El Guerrero', self.name, 'no puede atacar, con un estado de defensa')
            return
        another.set_estado()
        # Solo se modificaran los valores si el arma tiene un estado mayor a 2 y aun sirve (Ej. 7)
        if self.estado_arma >= 2: 
            if another.estado_actual == 'ataque':
                another.vida -= 20 # Si el que es atacado tambien esta en modo de ataque, su vida se reduce en 20 (Ej. 12.b)
            else:
                another.estado_escudo -= 5 # Si el estado del atacado es modo defensa, el estado de su escudo se reduce en 5 (Ej. 12.a)
            # Agregamos que cuando se "ataca", se le quita 2 al estado del arma (Ej. 6, 12.c)
            self.estado_arma -= 2
        else:
            print('El Guerrero ', self.name, ' No tiene buen estado del arma')

    # Indica si nuestro guerrero esta vivo (Ej. 8)
    @property
    def isalive(self):
        if self.vida > 0:
            return True
        else:
            return False
        
    # Convertir el atributo 'estado' en una propiedad que no deje defender cuando el estado del escudo es 0 (Ej. 11)
    def set_estado(self):   
        name = 'Indica el estado del Guerrero '+self.name+' : '
        while True:
            estado=input(name) 
            if (self.estado_escudo == 0 and estado == 'defensa'):
                print('No se puede poner estado de defensa sin escudo')
                self.estado_actual = 'ataque'
                break
            elif (estado == 'ataque' or estado == 'defensa'):
                self.estado_actual = estado
                break
            else:
                print('El estado debe ser \'ataque\' o \'defensa\'')
        
    # Nos muestra los datos de nuestros guerreros (Yo)
    @property
    def status(self):
        print('Guerrero',self.name, '| Vida : ',self.vida, ', Esta vivo?',self.isalive)
        print('> Estado del arma : ', self.estado_arma, '| Estado escudo : ', self.estado_escudo)
    # Nos muestra si el estado del guerrero (Atacando o Defendiendo) (Yo)
    @property
    def actividad(self):
        if self.estado_actual == 'ataque':
            estado = "Atacando..."
        else:
            estado = "Defendiendo..."
        print('El Guerrero', self.name,'esta', estado)

if __name__ == '__main__':
    guerrero1 = Guerrero(input('Nombre a tu primer Guerrero : '))
    guerrero1.status
    print('_____________________________________')
    guerrero2 = Guerrero(input('Nombra a tu segundo Guerrero : '))
    guerrero2.status
    print('_____________________________________')

    seguir = 'y'
    while seguir=='y':
        guerrero1.atacar(guerrero2)
        guerrero1.status
        guerrero2.status
        seguir=input('Seguir? -> ')
    print('_____________________________________')
