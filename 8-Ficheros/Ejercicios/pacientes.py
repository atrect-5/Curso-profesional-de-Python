# Alejandro Gonzalez 

# Ejercicio Numero 1
'''1.- Cree una clase Paciente que herede de collections.namedtuple con los atributos id, 
nombre, apellido, edad y diabético. Además, agregue la property “es_diabetico” que deberá devolver 
True si el valor del atributo “diabético” es “Sí”. ** Guarde el código en un archivo “pacientes.py”'''

# Importamos 'namedtuple' para crear la clase
from collections import namedtuple
# Creamos nuestra clase que hereda de 'namedtuple' con las caracteristicas que se requieren
_Paciente = namedtuple('Paciente', 'id nombre apellido edad diabetico')
# Creamos nuestra clase 'Paciente' que hereda de '_Paciente' (Por lo anto tambien de 'namedtuple')
class Paciente(_Paciente):

    # Creamos nuestra property
    @property
    def isDiabetic(self):
        '''Regresa 'True' en caso de que el paciente sea diabetico, 'False' en caso contrario'''
        return True if self.diabetico == 'Sí' else False
    
    # Agregamos una funcion para imprimir en pantalla los objetos de la clase
    def __str__(self):
        return f'Paciente: {self.id} - {self.nombre} {self.apellido}'.ljust(32)+f' | Edad: {self.edad} | Es diabetico?: {self.isDiabetic}'


# Ejercicio Numero 2 
'''2.- Dado el archivo “pacientes.txt”, abra y extraiga sus datos. Con ellos, cree instancias de 
la clase Paciente -definida en el ejercicio anterior- y guárdelos en un diccionario “data”, donde 
la clave de cada objeto será su correspondiente id. **Considere eliminar los saltos de línea de 
los valores leídos y convertir los datos id y edad antes de crear el objeto.'''
# pacientes.txt
'''
1;Juan;Perez;42;Sí
2;Jose;García;15;No
3;Manuel;Rodriguez;50;Sí
4;Alicia;Ramirez;12;No
5;Lucas;Lucyk;25;No
'''
# Creamos la ruta a nuestro texto con la informacion de los pacientes
from os import path
pacientepath = path.dirname(__file__)+'\pacientes.txt'
if __name__=='__main__':
    data = {}
    # Abrimos el archivo txt
    with open(pacientepath, encoding="utf-8") as pacientetxt:
        # Guardamos cada linea leida del archivo en la lista 'pacientesList', eliminando los saltos de linea
        pacientesList = [paciente.rstrip() for paciente in pacientetxt.readlines()]
        # Obtenemos los datos individualmente y creamos un objeto con estos datos
        for _paciente in pacientesList:
            paciente = Paciente(id=int(_paciente.split(';')[0]), # Convertimos el id obtenido en entero
                                nombre=_paciente.split(';')[1],
                                apellido=_paciente.split(';')[2],
                                edad=int(_paciente.split(';')[3]), # Convertimos la edad obtenida en entero
                                diabetico=_paciente.split(';')[4]) 
            # Guardamos los datos de todos los paceintes en un diccionario donde el valor es el id de cada paciente
            data[str(paciente.id)] = paciente 
        
# Ejercicio Numero 3
'''3.- Extienda el código del ejercicio anterior para serializar los objetos del diccionario “data” 
con el módulo pickle. **Guarde el contenido como “pacientes.pickle”.'''
import pickle # Importamos el modulo pickle
pacientePicklePath = path.dirname(__file__)+'\pacientes.pickle' # Creamos la direccion para que se guarde el archivo pickle
if __name__=='__main__':
    # Abrimos el archivo en modo escritura, indicando que si no existe lo va a crear y va a interpretar el contenido como binario
    with open(pacientePicklePath, 'wb') as pacientePickle:
        # Escribimos 'data' en el archivo pickle
        pickle.dump(data, pacientePickle)
    
    print(data)