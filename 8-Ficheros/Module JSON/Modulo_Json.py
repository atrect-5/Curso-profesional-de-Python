from os import path
jsonPath = path.dirname(__file__)+"\datos.json"


import persona, json
 


# Definimos una funcion que recibe un objeto que se llamara cuando json no pueda serializar algun objeto 
# Sin esta funcion, se elevaria una excepcion de JSON al no poderse serializar un objeto 'persona.Persona is not JSON serializable'
def to_json(python_object):            
    if isinstance(python_object, persona.Persona): # Evaluamos que el objeto recibido sea de nuestra clase 'persona'
        return {
            '__class__': 'persona.Persona',
            '__value__': {
                'nombre': python_object.nombre,
                'skills': python_object.skills
        }
    } # Si es de nuestra clase persona, se regresara un diccionario de clave '__class__' de valor 'persona.Persona', y una clave __value__ con valor de un diccionario.
    # Este diccionario tendra los datos de nuestros objetos que queremos enviar
    raise TypeError(repr(python_object) + ' is not JSON serializable') # De no ser de nuestra clase 'persona', se elevara una excepcion
 
# Creamos nuestro diccionario donde se almacenaran los datos de nuestras innstancias
data = {
    "personas": [
        persona.Persona("Lucas", ["Python", "C++", "JS"]),
        persona.Persona("Alejandro", ["Java", "C#"])
    ]
}
print(data)
# {'personas': [Persona(nombre=Lucas, skills=['Python', 'C++', 'JS']), Persona(nombre=Alejandro, skills=['Java', 'C#'])]}

 
# Escribimos los datos en el archivo .json
with open(jsonPath, 'w', encoding="utf-8") as file:
    # Especificamos 'default' como el nombre de nuestra funcion. Para cuando no pueda serializar nuestros objetos de la clase 'persona'
    json.dump(data, file, ensure_ascii=False, indent=2, default=to_json) 