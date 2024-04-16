# Alejandro Gonzalez

# Ejercicio Numero 5
'''Cree un programa que almacene en variables los conjuntos {1,5,7,3,4,2} y {1,4,9,15,21} e indique:
 a-La intersección entre ambas variables (valores que se encuentran en ambas variables).
 b-Los valores que se encuentran en cualquiera de los dos conjuntos pero no en ambos a la vez.'''
print('Ejercicio Numero 5')
conjunto_1 = {1,5,7,3,4,2}
conjunto_2= {1,4,9,15,21}
print('Conjunto 1: ', conjunto_1,'   |   Conjunto 2: ', conjunto_2)

interseccion = conjunto_1 & conjunto_2
diferencia_simetrica = conjunto_1 ^ conjunto_2
print('Interseccion: ', interseccion,'\nDiferencia_simetrica: ', diferencia_simetrica)
print('Type(conjunto): ', type(conjunto_1))
print('______________________________________')


# Ejercicio Numero 6
'''Cree una variable persona que almacene como diccionario las claves nombre, sexo y 
teléfono con cualquier valor a elección.'''
print('Ejercicio Numero 6')
diccionario = {'Nombre':'Alejandro', 'Apellido':'Gonzalez', 'Escuela':'Azul School', 'Edad':'23 years'}
print(diccionario)
print('Nombre: ', diccionario['Nombre'])
print('Apellido: ', diccionario['Apellido'])
print('Escuela: ', diccionario['Escuela'])
print('Edad: ', diccionario['Edad'])
print('Type(diccionario): ', type(diccionario))
print('______________________________________')


# Ejercicio Numero 7
'''Utilizando la función dict, cree un diccionario de 5 artículos con un precio determinado. 
Las claves deben ser en formato ‘articulo_x’ y el valor debe ser un entero.'''
print('Ejercicio Numero 7')
articulos = dict([('Papas', 18), ('Cacahuates', 10), ('Pistaches', 20), ('Gomitas', 14)])
print(articulos)
print('Precio Papas: ', articulos['Papas'])
print('Precio Cacahuates: ', articulos['Cacahuates'])
print('Precio Pistaches: ', articulos['Pistaches'])
print('Precio Gomitas: ', articulos['Gomitas'])
print('Type(articulos): ', type(articulos))