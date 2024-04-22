# Alejandro Gonzalez

# Ejercicio Numero 2
'''Tomando 3.14 como valor de PI, escriba una función que reciba el 
valor del radio de un círculo y retorne el valor de su área:'''
print('Ejercicio Numero 2')

def Area_Circulo(radio:int) -> int: # Definimos la fucion que calcula el area
    '''Devuelve el Area de un circulo segun su radio
    Parameters:
        int radio: radio del circulo
    Returns:
        int: Area del circulo'''
    PI = 3.1416
    return radio ** 2 * PI # Regresamos el valor de la operacion para obener el area
    
def Perimetro_Circulo(radio:int) -> int: # Definimos la fucion que calcula el perimetro
    '''Devuelve el Perimetro de un circulo segun su radio
    Parameters:
        int radio: radio del circulo
    Returns:
        int: Perimetro del circulo'''
    PI = 3.1416
    return radio * 2 * PI # Regresamos el valor de la operacion para obener el perimetro

# Registramos el radio que tendra el circulo
radio = int(input("Radio del circulo a calcular el area y perimetro: "))

# Llamamos a las funciones para calcular el area y permietro, e imprimimos los valores que regresan las funciones
print('Area : {0:.2f} cm^2 \nPermietro : {1:.2f} cm'.format(Area_Circulo(radio), Perimetro_Circulo(radio)))