# Importamos los modulos que usaremos
import datetime as dt, sqlite3
from os import path

# Definimos la ruta de la base de datos y creamos la conexion a esta
DB_NAME =  path.dirname(__file__)+'calendar.sqlite3'
DB_CONEXION = sqlite3.connect(DB_NAME)

# Creamos las funciones para iniciar y cerrar la base de datos
def close_conexion ():
    '''Cierra la conexion a la base de datos'''
    DB_CONEXION.close()
def start_database():
    '''Creamos las tablas 'si no existen' que usaremos en nuestra base de datos (Eventos y Asistentes)'''
    cursor = DB_CONEXION.cursor()    
    cursor.execute('''CREATE TABLE IF NOT EXISTS Eventos(
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    titulo TEXT, 
                    ubicacion TEXT, 
                    inicio datetime, 
                    fin datetime, 
                    descripcion TEXT
    )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS Asistentes(
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    mail TEXT, 
                    evento INTEGER REFERENCES evento(pk) ON DELETE CASCADE ON UPDATE CASCADE
    )''')
    cursor.close()

class Evento:
    def __init__(self, id = None, titulo = "", ubicacion = "", inicio = dt.datetime.now(), fin = dt.datetime.now(), descripcion = "", asistentes = []) -> None:
        self.id = id
        self.titulo = titulo
        self.ubicacion = ubicacion
        self.inicio = inicio
        self.fin = fin
        self.descripcion = descripcion
        self.asistentes = asistentes

    def __str__(self) -> str:
        return f'{self.titulo} | Del {self.inicio.strftime("%Y-%m-%d a las %H:%M")} al {self.fin.strftime("%Y-%m-%d a las %H:%M")}'

    # Este decorador indica que el método no pertenece a un objeto, sino a la propia clase. 
    @classmethod
    def objects(cls, _operator:str="AND", **kwargs):
        pass

    @classmethod
    def day_events(cls, day):
        pass

    @property
    def exists(self):
        pass

    def save(self):
        pass

    def delete(self):
        pass

    def add_asistente(self, mail):
        pass

    def delete_asistente(self, mail):
        pass

class Asistente:
    def __init__(self, mail:str, evento:int, id:int=None) -> None:
        self.id = id
        self.mail = mail
        self.evento = evento

    def __str__(self):
        return self.mail
    
    def __eq__(self, other):
        return self.mail == other.email and self.evento == other.evento

    @classmethod
    def objects(cls, _operator:str="AND", **kwargs):
        pass 

    @property
    def exists(self):
        pass

    def save(self):
        pass

    def delete(self):
        pass