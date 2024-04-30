# Alejandro Gonzalez : Ejercicios Opcionales

class Guerrero: # Definimos la clase y las variables de clase 'vida' y 'estado_arma' con sus valores (Ej. 4)
   
    def __init__(self, name, arma, escudo) -> None: # Ahora se reciben argumentos tipo Arma y Escudo para gestionar dichos elementos (Eo. 3)
        self.name = name # Esta propiedad es para identificar al guerrero (Yo)
        self.vida = 100
        self.estado_arma = arma
        # Creamos un nuevo atributo con los puntos del estado del escudo (Ej.10)
        self.estado_escudo = escudo
        

    # Definimos el metodo 'atacar' que le quita 20 de vida al objeto que recibe (Ej. 5)
    def atacar(self, another): 
        # Se comprueba que el Guerrero este con vida para poder atacar (Ej. 12.e)
        if not self.isalive:
            print('El Guerrero', self.name, 'no puede atacar, ya que esta muerto')
            return
        # Se comprueba que el Guerrero que es atacado siga vivo
        if not another.isalive:
            print('El Guerrero', another.name, 'no puede ser atacado, ya que esta muerto')
            return
        # Se agrega el estado en el que esta el guerrero (Atacando o defendiendo) (Ej.9)
        self.set_estado()
        # Si el atacante esta en modo de 'defensa', no podra atacar (Ej. 12.d)
        if self.estado_actual == 'defensa':
            print('El Guerrero', self.name, 'no puede atacar, con un estado de defensa')
            return
        another.set_estado()
        # Se modifica ahora con los valores tomados en cuenta de las nuevas clases Arma y Escudo (Eo.5)
        # Solo se modificaran los valores si el arma tiene un estado mayor a 2 y aun sirve (Ej. 7)
        if self.estado_arma.estado >= 2: 
            if another.estado_actual == 'ataque':
                another.vida -= self.estado_arma.dano # Si el que es atacado tambien esta en modo de ataque, su vida se reduce lo que el dano del arma (Eo .5)
            else:
                self.estado_arma.estado -= 10 # Si el atacado recibe el golpe con el escudo, el arma del atacante recibira un desgaste adicional (Eo. 5)
                another.estado_escudo.estado -= 5 # Si el estado del atacado es modo defensa, el estado de su escudo se reduce en 5(Ej. 12.a)
                # El dano a la vida es la diferencia del dano que produce el arma y la absorcion que amortigua el escudo (Eo. 5)
                if self.estado_arma.dano > another.estado_escudo.absorcion:
                    another.vida -= (self.estado_arma.dano - another.estado_escudo.absorcion)
            # Agregamos que cuando se "ataca", se le quita 2 al estado del arma (Ej. 6, 12.c)
            self.estado_arma.estado -= 2
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
            if (self.estado_escudo.estado == 0 and estado == 'defensa'):
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
        print('> Arma : ', self.estado_arma.nombre,', Dano : ', self.estado_arma.dano, ', Estado del arma : ',self.estado_arma.estado)
        print('> Escudo : ', self.estado_escudo.nombre, ', Absorcion : ', self.estado_escudo.absorcion, ', Estado del escudo : ', self.estado_escudo.estado)

# Creando una clase Arma (Eop. 1)
class Arma:
    def __init__(self, nombre, dano, estado) -> None:
        self.nombre = nombre
        self.dano = dano
        self.estado = estado

# Creando una clase escudo (Eop. 2)
class Escudo:
    def __init__(self, nombre, absorcion, estado) -> None:
        self.nombre = nombre
        self.absorcion = absorcion
        self.estado = estado


if __name__ == '__main__':
    arma=Arma('Excalibur', 50, 100)
    arma2=Arma('Palo', 2, 100)
    escudo=Escudo('Tapa', 2, 100)
    escudo2=Escudo('Hyliano', 45, 100)

    guerrero1 = Guerrero(input('Nombre a tu primer Guerrero : '), arma, escudo)
    guerrero1.status
    print('_____________________________________')
    guerrero2 = Guerrero(input('Nombra a tu segundo Guerrero : '), arma2, escudo2)
    guerrero2.status
    print('_____________________________________')

    seguir = 'y'
    while seguir=='y':
        guerrero1.atacar(guerrero2)
        guerrero1.status
        guerrero2.status
        seguir=input('Seguir? -> ')
        print('_____________________________________')