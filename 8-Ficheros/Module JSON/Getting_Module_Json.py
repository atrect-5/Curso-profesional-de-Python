# Creamos la ruta al archivo 'datos.json', donde se guardaron los datos que creamos en el modulo pasado (Module_Json)
from os import path
jsonPath = path.dirname(__file__)+"\datos.json"


import json, persona


# Esta funcion nos permite extraer adecuadamente nuestros objetos del archivo json, sin ella obtendremos todo lo que hay dentro del archivo:
# __class__ persona.Persona
# __value__ {'nombre': 'Lucas', 'skills': ['Python', 'C++', 'JS']}
# __class__ persona.Persona
# __value__ {'nombre': 'Alejandro', 'skills': ['Java', 'C#']}

def from_json(json_object):
    if '__class__' in json_object: # Evaluamos si el objeto tiene la clave '__class__'
        if json_object['__class__'] == 'persona.Persona': # Evaluamos si el objeto es 'persona.Persona'
            return persona.Persona(**json_object['__value__']) # Regresamos un objeto de tipo 'persona.Persona' con los valores obtenidos de la clave '__value__'
    return json_object


with open(jsonPath, encoding="utf-8") as file:
    # Indicamos 'object_hook=from_json' Para que cuando obtenga un objeto, lo pase por la funcion definida y obtengamos los datos correctamente
    # 'data' guardara la lista de objetos que nos regrese la funcion
    data = json.load(file, object_hook=from_json)

    for persona_json in data["personas"]:
        print(persona_json)
    # Persona(nombre=Lucas, skills=['Python', 'C++', 'JS'])
    # Persona(nombre=Alejandro, skills=['Java', 'C#'])
