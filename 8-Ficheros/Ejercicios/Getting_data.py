# Alejandro Gonzalez
# Ejercicio numero 5
'''5.- Cree un nuevo programa que tome los archivos “pacientes.pickle” y 
“pacientes.json”, los de-serialice con el módulo correspondiente y los 
guarde en un diccionario “data_pickle” y “data_json” respectivamente.
En el caso del módulo json, considere crear los objetos al momento de 
leerlos. ** Ambos diccionarios creados deben dar True al evaluar 
igualdad (data_json == data_pickle)'''

import json, pickle
from pacientes import Paciente
from os import path
# Creamos las rutas a nuestros archivos
pacienteJsonPath = path.dirname(__file__)+"\pacientes.json"
pacientePicklePath = path.dirname(__file__)+'\pacientes.pickle'

# Obtenemos los datos del archivo 'pacientes.pickle'
with open(pacientePicklePath, 'rb') as pacientePickle:
    data_pickle = pickle.load(pacientePickle)

    print('Objetos obtenidos en \'data_pickle\'')
    for k,v in data_pickle.items():
        print('Datos del',v)

# Se crea la funcion que va a crear los objetos de la informacion obtenida en el archivo 'json'
def from_json(json_object):
    '''Regresa un diccionario que guarda como valor los objetos 'Paciente' con clave 'paciente.id' '''
    data = {}
    for k,v in json_object.items(): # Recorremos el diccionario creando los objetos 'Paciente'
        id, nombre, apellido, edad, diabetico = v
        paciente = Paciente(id, nombre, apellido, edad, diabetico)
        data[k] = paciente 
    return data

# Obtenemos los datos del archivo 'pacientes.json'
with open(pacienteJsonPath, 'r', encoding='utf-8') as pacienteJson:
    data_Json = json.load(pacienteJson, object_hook=from_json)

    print('Objetos obtenidos en \'data_Json\'')
    for k,v in data_pickle.items():
        print('Datos del',v)
print('Son iguales los diccionarios \'data_Json\' y \'data_pickle\'? : ',data_Json == data_pickle)