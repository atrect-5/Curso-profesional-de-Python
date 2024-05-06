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
        return True if self.diabetico == 'Si' else False


# Probamos el codigo
if __name__=='__main__':
    paciente = Paciente('1525', 'Eduardo', 'Garcia', '25','Si')
    print(f'Paciente: {paciente.id} - {paciente.nombre} {paciente.apellido}; Edad: {paciente.edad}; Es diabetico? {paciente.isDiabetic}')
    # Paciente: 1525 - Eduardo Garcia, Edad: 25, Es diabetico? True