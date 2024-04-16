'''en Python las estructuras de control de 
flujo no poseen llaves que marquen dónde 
comienzan y terminan; el delimitador de 
comienzo son los dos puntos (:) y el propio 
indentado del código indica que dichas 
sentencias pertenecen al mismo bloque.'''

# if
hoy = 'sabado'
if hoy == 'sabado':
    print('hoy es sabado')

# elif
'''Si la primer comparacion es falsa, hace las comparaciones siguientes'''
anno = 2019
if anno >= 1990 and anno < 2000:
    print("Es la década del 90")
elif anno >= 2000 and anno < 2010:
    print("Es la década del 00")
elif 2010 <= anno < 2020:
    print("Es la década del 10")
else:
    print("Solo analizamos pocas décadas")


# try 
'''La declaración try es utilizada para el manejo de excepciones. '''
try:
     print('as' * 'df')
except TypeError:
     print('Error multiplicando cadenas')
except:
     print('Error desconocido')
else: 
    print("Entra aqui si no hubo excepcion")
finally:
    print("Se ejecuta si o si, haya o no excepcion")


# while 
'''A diferencia de otros lenguajes, while puede tener un else'''
i = 0
while i<=5:
    print(i)
    i += 1
else:
    print("Finalizo el ciclo")

# Usando break para terminar el ciclo (no se ejecuta else)
i = 0
while i<=5:
    print(i)
    if i == 3:
        break
    i += 1
else:
    print("Finalizo el ciclo")



# for
'''El ciclo for se usa para iterar sobre una lista'''
dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]
for dia in dias:
    print(dia)

'''Para hacer un ciclo que se repita determinada catidad de veces,
se usa el metodo "range()" '''
for i in range(3):
    print(i)