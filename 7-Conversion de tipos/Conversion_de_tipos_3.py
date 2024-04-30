
# Creamos nuestra clase
class Numeros:
    def __init__(self, *args):
        self.valores = args # Almacena una lista de valores
 
    # Se accede a este metodo cuando se usa el metodo 'int()'
    def __int__(self):
        # Si no hay numeros en la lista, retorna 0
        if not self.valores: 
            return 0
 
        #número con la sumatoria de todos los valores del objeto
        suma = sum(self.valores)
 
        #retornamos el valor generado por el método __int__ de la variable
        return suma
    
    # Se accede a este metodo cuando se usa el metodo 'float()'
    def __float__(self):
        if not self.valores:
            return 0.0
             
        return sum(self.valores) / len(self.valores) # Regresa el promedio de los valores recibidos
 
if __name__ == '__main__':
    # int() sobreescribiendo el metodo en la clase
    nn = Numeros(1, 2, 3)
    # Se llama al metodo '__int__' creado anteriormente en la clase
    print(int(nn))
    # 6

    # funcionamiento comun de int()
    # Tambien nos permite especificar la base del numero que queremos convertir 
    valor_binario = "100"
    base_10 = int(valor_binario, 2) 
    print("Valor:", base_10, "Tipo:", type(base_10)) # (Lo convierte a un numero base 10, tomando en cuenta que lo recibe como base 2)
    # Valor: 4 Tipo: <class 'int'>


    # float() sobreescribiendo el metodo en la clase
    nn = Numeros(1, 2, 3)
    # Se llama al metodo '__float__' creado anteriormente en la clase
    print(float(nn))
    # 2.0

    # funcionamiento comun de float()
    n0 = float("-55.5")
    n1 = float("Infinity")
    n2 = float("inf")
    n3 = float("NaN")
 
    print(type(n0), type(n1), type(n2), type(n3))
    # <class 'float'> <class 'float'> <class 'float'> <class 'float'>
 
    print(n0 + n1)
    # inf
    print(n1 + n2)
    # inf
    print(n1 - n2)
    # nan