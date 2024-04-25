
'''Se trata de la caracteristica de python de editar el funcionamiento de un método fuera de la definición de la clase'''

# Se define la clase con su propio metodo
class MrMeeseeks:
    def aparecer(self):
        print("Hola!")

# Definimos una funcion fuera de la definicion de la clase
def aparecer_edit(self):
    print("Hola, soy el Señor Meeseeks, mírenme!")

# Con esto indicamos que ahora la funcion definida en la clase, va a ser la nueva funcion que definimos despues
MrMeeseeks.aparecer = aparecer_edit

# Creamos una insancia de la clase y usamos el metodo que editamos 
mm = MrMeeseeks()
mm.aparecer()
# Hola, soy el Señor Meeseeks, mírenme!

'''Inclusive se puede hacer este procedimiento en el interprete de python mientras se esta ejecutando el codigo del programa'''

# Duck Typing

# Se crea una clase 'Vivienda' con un metodo 'abiri_puerta'
class Vivienda:
    def abrir_puerta(self):
        print ("Abriendo puerta.")
 
# Se crea una clase 'Perosna' con un metodo 'ingresar_vivienda'
class Persona:
    def ingresar_vivienda(self, vivienda):
        vivienda.abrir_puerta() # Llama al metodo 'abrir_puerta' de la clase del parametro que recibe
        '''En este método no analizamos si el valor recibido es una instancia de la clase Vivienda; 
        si posee el método abrir_puerta, suponemos que es una y ejecutamos el método correspondiente.'''
        # Asumimos que una vivienda debe poseer el método abrir_puerta
 
# Creamos una instancia de cada clase anterior
departamento = Vivienda()
persona = Persona()
# Accedemos al metodo de la clase
persona.ingresar_vivienda(departamento)
# Abriendo puerta.