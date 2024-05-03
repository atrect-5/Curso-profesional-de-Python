# Creamos la ruta al archivo 'personas.pickle', donde se guardaron los datos que creamos en el modulo parado (Module_Pickle)
from os import path
picklePath = path.dirname(__file__)+"\personas.pickle"


import persona, pickle

# Abrimos el archivo 'personas.pickle' para leer el contenido
with open(picklePath, 'rb') as file:
    # Se obtiene el contenido del archivo .pickle (El diccionario con la lista de las personas que guardamos)
    data = pickle.load(file)
    
    # Imprimimos la lista que obtuvimos
    for persona in data["personas"]:
        print(persona.nombre, persona.skills)
        # Lucas ['Python']
        # Alejandro ['Java']