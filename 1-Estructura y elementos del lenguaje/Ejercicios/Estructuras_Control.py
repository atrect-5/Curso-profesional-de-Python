# Alejandro Gonzalez


# Ejercicio Numero 8
'''Dada una lista de valores numéricos, determine e imprima si la sumatoria de 
todos los valores excede a un valor máximo establecido en una variable.'''
print("Ejercicio Numero 8")
lista = [2, 3, 4, 5, 6, 7, 8, 3]
print(lista)
amount = 0
valorMaximo = 35
for count in lista:
    amount += count     # Aqui se van sumando 1 a 1 los numeros de la lista

if amount > valorMaximo: 
    print('La suma de los numeros si excede el valor maximo :c')
else:
    print('La suma es mas pequena que el valor maximo :)')
print('Sumatoria: ', amount, '\nValor Maximo: ', valorMaximo)
print('______________________________________')


# Ejercicio Numero 9
'''Utilizando la sentencia while, escriba un programa que imprima los múltiplos 
de 3 hasta que la sumatoria de todos los valores impresos sea mayor a 50.'''
print("Ejercicio Numero 9")
multiplos = 0
amount = 0

while amount <= 50:
    multiplos += 3          # Aqui se almacenan los multiplos de 3
    print(multiplos)        # Se imprime despues de aumentar la variable o si no, los numeros que se imprimen no superan el 50
    amount += multiplos     # Aqui se almacenan los numeros que se han impreso

print('la suma de los numeros impresos es: ', amount)