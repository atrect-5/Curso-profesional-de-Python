
from os import path
picklePath = path.dirname(__file__)+"\personas.pickle"


# Importamos la clase que hicimos anteriorente donde guardamos la lista de las habilidades de una persona y el modulo pickle
import persona, pickle
# Su guarda una lista de las personas que agreguemos con la clave 'personas'    
data = {"personas": []}
 
# Creamos 2 instancias de la clase
p1 = persona.Persona("Lucas")
p2 = persona.Persona("Alejandro")
# Les agregamos una skill a cada persona
p1.add_skill("Python")
p2.add_skill("Java")
 
# Agregamos nuestros objetos a la lista
data["personas"].append(p1)
data["personas"].append(p2)
 

# Creamos un archivo 'personas.pickle' y guardamos nuestra lista de personas
with open(picklePath, 'wb') as file:
    pickle.dump(data, file)
 
print(data)
# {'personas': [<persona.Persona object at 0x000001D989EBB410>, <persona.Persona object at 0x000001D989EBB3D0>]}