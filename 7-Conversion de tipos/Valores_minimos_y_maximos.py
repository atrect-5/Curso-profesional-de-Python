
if __name__ == '__main__':
    # min() && max()
    valores = [10, 20, 30, 40]
 
    print("min:", min(valores)) # Devuelve el valor mas pequeno de la lista
    # min: 10
    print("max:", max(valores)) # Devuelve el valor mas alo de la lista
    # max: 40


    frase = "Nunca confíes en un ordenador que no puedas lanzar por una ventana"
    print(min(frase.split(), key=len)) # 'key=len' indica que usara la longitud del objeto (string) para determinar cual es el mayor o menor
    # en
    print(max(frase.split(), key=len))
    # ordenador


# Creando nuestra propia funcion para usar como 'key' en min() y max() / (Debe retornar un numero entero)
def suma_de_valores(palabra):
    """ Retorna la sumatoria de valores ASCII de todas las letras de una palabra"""
 
    #para cadena vacía
    if not palabra:
        return 0
 
    #Sumatoria de ord() de cada letra 
    val = 0
    for letra in palabra:
        val += ord(letra)
 
    return val
 
if __name__ == '__main__':
 
    frase = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed imperdiet risus massa, non varius arcu. "
 
    minimo = min(frase.split(), key=suma_de_valores) # Usamos nuestra funcion para decidir cual es el valor mas grande de la cadena
    maximo = max(frase.split(), key=suma_de_valores)
 
    print("Mínimo:", minimo, "| Suma ascii:", suma_de_valores(minimo))
    # Mínimo: Sed | Suma ascii: 284
    print("Máximo:", maximo, "| Suma ascii:", suma_de_valores(maximo))
    # Máximo: consectetur | Suma ascii: 1199
