
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
