
from os import path
lorem = path.dirname(__file__)+'\lorem.txt'


#abrimos y guardamos en variable file
with open(lorem) as file:
     
    #imprimimos el contenido en caso de ser posible
    print(file.read() if file.readable() else "No se puede leer.")
    # Lorem ipsum ......
    file.seek(0)

# READLINE()
    #imprimimos hasta encontrar un salto de línea
    print(file.readline())
    # Lorem ipsum .... ('\n')
    file.seek(0)

# READLINES()
    #guardamos e imprimimos hasta encontrar un salto de línea
    lineas = file.readlines(1)
    print(type(lineas), "| Elementos:", len(lineas))
    # <class 'list'> | Elementos: 1
    print("Var lineas:", lineas)
    # Var lineas: ['Lorem ipsum dolor sit amet, consectetur adipiscing elit, \n']

# WRITELINES()
# Importamos webbrowser que lo utilizaremos para abrir un archivo con el navegador
import webbrowser

# Creamos la ruta donde se va a guardar nuestro archivo
filePath = path.dirname(__file__)+"\pagina_python.html"

# Creamos nuestra lista que escribiremos en nuestro archivo 
lineas = [
    '<!DOCTYPE html>\n',
    '<html lang="es">\n',
    '\t<head>\n',
    '\t\t<meta charset="utf-8">\n',
    '\t\t<title>Python Web</title>\n',
    '\t\t<meta name="viewport" content="width=device-width, initial-scale=1.0">\n',
    '\t</head>\n',
    '\t<body>\n',
    '\t\t<p>Hola mundo! : 0</p>\n',
    '\t\t<p>Esto es una página web creada en Python!! : 0</p>\n',
    '\t</body>\n',
    '</html>\n',
]

# Abrimos nuestro archivo, indicando que sobreescribiremos lo que tenga el archivo ('w') y que usaremos codificacion 'utf-8'
with open(filePath, mode="w", encoding="utf-8") as file:
    file.writelines(lineas)

# Nos abre el navegador predeterminado con nuestro archivo que hicimos o sobreescribimos
webbrowser.open(filePath)