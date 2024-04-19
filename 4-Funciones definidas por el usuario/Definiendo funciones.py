
VALIDOS = ('Lucas', 'Juan', 'Marcos') # Creamos una variable con nombres validos para nuestra funcion

def es_valido(nombre, edad): # Definimos la funcion: def NombreFuncion (argumentos que recibe)
    if nombre in VALIDOS and edad >= 18: 
       return True # Si el nombre es valido (esta en tupla validos) y edad es mas de 18, retorna True


# Se llama funcion es_valido, con un nombre y edad recividos como parametro y se imprime resultado
print(es_valido(input("Ingrese su nombre: "), int(input("Ingrese su edad: "))))  
# Ingrese su nombre: Lucas
# Ingrese su edad: 19
# True

# Se imprime que tipo es el retorno de la funcion 'es_valido' cuando se pasan valores incorrectos (No se retorna nada en la funcion)
print(type(es_valido("John", 15)))
# <class 'NoneType'>


# Se define una funcion en la que se especifica que tipo de datos recive y devuelve (para una mejor comprension futura)
'''Esta funcion recive 'frase' de tipo string, 'invertida' de tipo bool que por defecto sera False'''
def ordenar_frase(frase: str, invertida: bool = False) -> str: # Se define una funcion para acomodar una frase con las palabras acomodadas por longitud
     return " ".join(sorted(frase.split(), key=len, reverse=invertida))

print(ordenar_frase("El veloz murciélago  hindú comía feliz cardillo y kiwi")) # Se llama a la funcion y se imprime el retorno
# y El kiwi veloz hindú comía feliz cardillo murciélago


print(ordenar_frase.__annotations__) # Imprime las especificaciones de la funcion 'ordenar_frase' con el atributo __annotations__
# {'frase': <class 'str'>, 'invertida': <class 'bool'>, 'return': <class 'str'>}
