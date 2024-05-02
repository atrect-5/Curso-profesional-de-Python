# Definimos la ruta de nuestro archivo json
from os import path
jsonPath = path.dirname(__file__)+"\datos.json"


# importamos la libreria JSON
import json
# Creamos nuestro diccionario
data = {
    "personas": [
        {
            "nombre": "Lucas",
            "apellido": "Lucyk",
            "pais": "Argentina"
        },
        {
            "nombre": "Alejandro",
            "apellido": "Gonzalez",
            "pais": "México"
        },
        {
            "nombre": "Ana",
            "apellido": "Perez",
            "pais": "Uruguay"
        },
    ]
}

# Creamos nuestro archivo o sobreescribimos el que exista ('w').
with open(jsonPath, 'w', encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4) # Guardamos los datos en nuestro archivo json


# Si queremos leer los daos de un archivo json: 
with open(jsonPath, encoding="utf-8") as file:
    data = json.load(file)
 
    print(type(data))
    # <class 'dict'>
 
    for persona in data["personas"]:
        [print(k,':', v) for k,v in persona.items()]
        # nombre : Lucas
        # apellido : Lucyk
        # pais : Argentina
        # nombre : Alejandro
        # apellido : Gonzalez
        # pais : México
        # nombre : Ana
        # apellido : Perez
        # pais : Uruguay