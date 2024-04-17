
# Metodos de diccionarios 

'''Update'''
paises_america = {}
# agregando contenido al diccionario
paises_america.update({"norte": ["EEUU", "México", "Canadá"]}) , # Definimos en la instancia la clave con su valor
paises_america.update(centro=["Panamá", "Honduras", "Costa Rica", "Guatemala"]) # Pasando la tupla centro como clave con su valor
ads = {"sur": ["Argentina", "Brasil", "Chile", "Uruguay"]} # Se crea un diccionario nuevo
paises_america.update(ads) # Se añade el diccionario nuevo al diccionario principal (se agregan sus claves y valores)
print(paises_america)
# {'norte': ['EEUU', 'México', 'Canadá'], 'centro': ['Panamá', 'Honduras', 'Costa Rica', 'Guatemala'], 'sur': ['Argentina', 'Brasil', 'Chile', 'Uruguay']}

'''Get'''
print(paises_america.get('sur')) # Obtenemos el valor guardado en la clave 'sur' del dict
# ['Argentina', 'Brasil', 'Chile', 'Uruguay']
print(paises_america.get('otra region')) # Buscamos una clave que no existe en el diccionario 'otra region'
# None
print(paises_america.get('otra region', 'No se encontro')) # Si definimos un valor por default, al no encontrarse la clave nos devolvera el default
# No se encontro

'''Keys'''
print(paises_america.keys()) # Imprime las claves almacenadas en el dict
# dict_keys(['norte', 'centro', 'sur'])

'''Values'''
print(paises_america.values()) # Imprime los valores almacenadas en el dict, sin las claves
# dict_values([['EEUU', 'México', 'Canadá'], ['Panamá', 'Honduras', 'Costa Rica', 'Guatemala'], ['Argentina', 'Brasil', 'Chile', 'Uruguay']])

'''Items'''
print(paises_america.items()) # Devuelve todos los elementos del diccionario
# dict_items([('norte', ['EEUU', 'México', 'Canadá']), ('centro', ['Panamá', 'Honduras', 'Costa Rica', 'Guatemala']), ('sur', ['Argentina', 'Brasil', 'Chile', 'Uruguay'])])

for k,v in paises_america.items(): # Se obtiene el valor de cada clave en 'k' y cada valor en 'v', luego se imprime y avanza al siguiente elemento
    print(k,v)
# norte ['EEUU', 'México', 'Canadá']
# centro ['Panamá', 'Honduras', 'Costa Rica', 'Guatemala']
# sur ['Argentina', 'Brasil', 'Chile', 'Uruguay']


'''Reversed'''
for k,v in reversed(paises_america.items()): # Se imprime el valor de 'k' y 'v' de manera inversa a como fue creado el dict
    print(k,v)
# sur ['Argentina', 'Brasil', 'Chile', 'Uruguay']
# centro ['Panamá', 'Honduras', 'Costa Rica', 'Guatemala']
# norte ['EEUU', 'México', 'Canadá']

'''Pop'''
paises_america.pop("norte") # Se borra el valor que tenga la clave 'norte'
print(paises_america)
# {'centro': ['Panamá', 'Honduras', 'Costa Rica', 'Guatemala'], 'sur': ['Argentina', 'Brasil', 'Chile', 'Uruguay']}
mensaje = paises_america.pop("norte", "No existe la clave") # Si no encientra la clave, manda el argumento por default (KeyError si no se especifica)
print(mensaje) # La salida anterior se guarda en 'mensaje', para ver que es lo que regresa el metodo anterior
# No existe la clave

'''Pop item'''
mensaje = paises_america.popitem() # Se elimina el ultimo elemento (El metodo regresa el valor eliminado, se guarda en 'mensaje para verlo')
print(mensaje)
# ('sur', ['Argentina', 'Brasil', 'Chile', 'Uruguay'])
print(paises_america) # Ya que se elimino el ultimo de dos elemenos, solo queda uno
# {'centro': ['Panamá', 'Honduras', 'Costa Rica', 'Guatemala']}

'''Set default'''
mensaje = paises_america.setdefault('centro', 'algun pais') # Se intenta agregar 'centro', pero si existe regresa el valor que de hecho tiene
print(mensaje)
# ['Panamá', 'Honduras', 'Costa Rica', 'Guatemala']
paises_america.setdefault('sur', ['Argentina', 'Brasil', 'Chile', 'Uruguay']) # Si no existe, lo agrega al diccionario
print(paises_america)
# {'centro': ['Panamá', 'Honduras', 'Costa Rica', 'Guatemala'], 'sur': ['Argentina', 'Brasil', 'Chile', 'Uruguay']}

'''Clear'''
paises_america.clear() # Elimina los elementos del dict 'paises_america'
print(paises_america)
# {}