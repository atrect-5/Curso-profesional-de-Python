# Alumno: Alejandro Gonzalez


# Ejercicio Numero 1
'''En un archivo .py, crear un programa donde el radio, la altura de un cilindro y 
PI se almacenen en distintas variables, con los valores 5.25, 13.2 y 3.14 
respectivamente. Luego, cree una nueva variable “volumen” con la fórmula correspondiente
utilizando las variables anteriores.'''
print("Ejercicio Numero 1")
PI = 3.14159            # En mayusculas indca constante
radio = 5.25
altura = 13.2

volumen = radio ** 2 * PI * altura
print(volumen, " cm ^ 3")

superficie = 2 * (PI * radio ** 2) + ((2 * radio) * PI * altura)
print(superficie, " cm ^ 2")
print('______________________________________')


# Ejercicio Numero 2
'''Cree un programa con 3 variables (texto_1, texto_2, texto_final). La primera debe ser 
la cadena “Este es el curso de Python “, la segunda debe ser ” de Azul School!” y la última 
debe ser la concatenación de ambas cadenas.
Por último, accede a la última variable texto_final para obtener la cadena “Python”, 
utilizando la expresión variable[posicion_inicial : posicion_final].'''
print("Ejercicio Numero 2")
texto_1 = "Este es el curso de Python "
texto_2 = 'de Azul School!'
texto_final = texto_1 + texto_2
print(texto_1, '\n', texto_2)
print(texto_final)

variable = texto_final[20:26]
print(variable)
print('______________________________________')


# Ejercicio Numero 3
'''Cree una variable con la cadena “Esto es una cadena de Python”, separando cada palabra 
con un salto de línea. Puede verificar si es correcto utilizando print(variable).'''
print('Ejercicio Numero 3')
cadena = 'Esto\nes\nuna\ncadena\nde\nPython'
print(cadena)