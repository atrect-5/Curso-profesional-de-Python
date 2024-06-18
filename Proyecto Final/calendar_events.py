# Alejandro Gonzalez (Diseñado por Lucas Lucik)
# Importamos los modulos que usaremos
import datetime as dt, sqlite3
from os import path

# Definimos la ruta de la base de datos y creamos la conexion a esta
DB_NAME =  path.join(path.dirname(__file__), 'calendar.sqlite3')
DB_CONEXION = sqlite3.connect(DB_NAME)

# Creamos las funciones para iniciar y cerrar la base de datos
def close_conexion (): 
    '''Cierra la conexion a la base de datos'''
    DB_CONEXION.close()
def start_database():
    '''Creamos las tablas 'si no existen' que usaremos en nuestra base de datos (Eventos y Asistentes)'''
    cursor = DB_CONEXION.cursor()    
    cursor.execute('''CREATE TABLE IF NOT EXISTS eventos(
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    titulo TEXT, 
                    ubicacion TEXT, 
                    inicio datetime, 
                    fin datetime, 
                    descripcion TEXT
    )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS asistentes(
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    mail TEXT, 
                    evento INTEGER REFERENCES eventos(id) ON DELETE CASCADE ON UPDATE CASCADE
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
        self.asistentes = asistentes # Lista de los 'mail' de los asistentes

    def __str__(self) -> str:
        return f'{self.titulo} | Del {self.inicio.strftime("%Y-%m-%d a las %H:%M")} al {self.fin.strftime("%Y-%m-%d a las %H:%M")}'

    # Este decorador indica que el método no pertenece a un objeto, sino a la propia clase. 
    @classmethod
    def objects(cls, _operator:str="AND", **kwargs):
        ''' Método de clase. Devuelve como instancias de Evento, los registros de la 
            base de datos que conincidan con las condiciones recibidas como kwargs.
 
            El atributo asistentes es una lista de mails, NO objetos instancia de Asistente.
 
        Parameters:
            dict kwargs: conjunto de pares "campo=valor" como condicón de filtro.
            str _operator: "AND" por defecto. Indica como se conjugan el conjunto de condiciones recibidas.
        Returns:
            list:   - Lista de objetos coincidentes con los criterios indicados.
                    - Lista vacía en caso que ningún registro coincida con los criterios indicados.
        Raises:
            RuntimeError: En caos que no exsta conexión a la base de datos.
        '''
        if not DB_CONEXION:
            raise RuntimeError('No hay conexion a la base de datos')
        eventos = []
        
        cursor = DB_CONEXION.cursor() # Declaramos nuestro cursor

        sqlQuery = 'SELECT * FROM eventos'
        # Si se agregaron kwards, se especifica la busqueda de la query
        if kwargs:
            sqlQuery += ' WHERE '
            sqlQuery += f' {_operator} '.join([f'{k} = "{v}"' for k, v in kwargs.items()])

        cursor.execute(sqlQuery)
        registros = cursor.fetchall()

        # Creamos un objeto tipo 'Evento' por cada registro que nos regresa la query sql
        for registro in registros:
            evento = cls(
                id = int(registro[0]),
                titulo = registro[1],
                ubicacion = registro[2],
                inicio = dt.datetime.fromisoformat(registro[3]),
                fin = dt.datetime.fromisoformat(registro[4]),
                descripcion = registro[5],
            )

            # Se obtiene la lista de asistentes con el metodo de clase 'objects' de la clase Asistentes
            asistentes = Asistente.objects(evento=registro[0])
            evento.asistentes = [asistente.mail for asistente in asistentes]
            eventos.append(evento)

        cursor.close()
        return eventos # Retornamos una lista de objetos tipo 'Evento'


    @classmethod
    def day_events(cls, day):
        ''' Método de clase. Devuelve como instancias de Evento, los registros de la 
            base de datos para el día indicado en el parámetro "day".
 
        Parameters:
            datetime.datetime day: día del que se se desea obtener los Eventos.
        Returns:
            list:   - Lista de objetos que incluyen el día indicado.
                    - Lista vacía en caso que no existan registros coincidentes.
        Raises:
            RuntimeError: En caos que no exsta conexión a la base de datos.
        '''
        if not DB_CONEXION:
            raise RuntimeError('No hay conexion a la base de datos')
        eventos = []
        cursor = DB_CONEXION.cursor()

        sqlQuery = f'SELECT * FROM eventos WHERE DATE("{str(day)}") BETWEEN DATE(inicio) AND DATE(fin)'
        
        cursor.execute(sqlQuery)
        registros = cursor.fetchall()

        # Creamos un objeto tipo 'Evento' por cada registro que nos regresa la query sql
        for registro in registros:
            evento = cls(
                id = int(registro[0]),
                titulo = registro[1],
                ubicacion = registro[2],
                inicio = dt.datetime.fromisoformat(registro[3]),
                fin = dt.datetime.fromisoformat(registro[4]),
                descripcion = registro[5],
            )

            # Se obtiene la lista de asistentes con el metodo de clase 'objects' de la clase Asistentes
            asistentes = Asistente.objects(evento=registro[0])
            evento.asistentes = [asistente.mail for asistente in asistentes]
            eventos.append(evento)

        cursor.close()
        return eventos


    @property
    def exists(self):
        ''' Indica si el objeto existe en la base de datos.
 
        Returns:
            bool:   True en caso que el objeto esta guardado en la base de datos (pk = self.pk). 
                    False en caso contrario.
        Raises:
            RuntimeError: En caos que no exsta conexión a la base de datos.
        '''
        if not DB_CONEXION:
            raise RuntimeError('No hay conexion a la base de datos')
        
        #Si self.id no esta definido, no existe en la bbdd
        if not self.id:
            return False
        
        cursor = DB_CONEXION.cursor()
        
        # Compruebo si obtengo registros de "id = self.id"
        cursor.execute(f"SELECT * FROM eventos where id={self.id}")
 
        existe = True if cursor.fetchone() else False
        cursor.close()
 
        return existe


    def save(self):
        '''Si el objeto existe en la base de datos, lo actualiza; sino, lo guarda.'''
        if not DB_CONEXION:
            raise RuntimeError('No hay conexion a la base de datos')
        cursor = DB_CONEXION.cursor()
        # Valores a guardar
        valores = (
            self.titulo,
            self.ubicacion,
            self.inicio,
            self.fin,
            self.descripcion,
            self.id
            )
        
        # Si el objeto no existe, insertamos los valores
        if not self.exists:
            sqlQuery = 'INSERT INTO eventos(titulo, ubicacion, inicio, fin, descripcion, id) VALUES (?,?,?,?,?,?)'
            cursor.execute(sqlQuery, valores)

            self.id = int(cursor.lastrowid)
            # Como el evento no existe, inserto los asistentes sin comprobar si existen
            [Asistente(mail=asistente, evento=self.id).save() for asistente in self.asistentes]

        # Si el objeto existe, actualiamos los valores.
        else:
            cursor.execute('UPDATE eventos SET titulo = ?, ubicacion = ?, inicio = ?, fin = ?, descripcion = ? WHERE id = ?', valores)
            # Elimino todos los asistentes que no estan incluidos en self.asistentes
            for asistente in Asistente.objects(evento=self.id):
                asistente.delete() if asistente.mail not in self.asistentes else None

            # Inserto los asistentes. El método save del objeto de clase Asistente se encarga de determinar si ya existe en la bbdd
            [Asistente(mail=asistente, evento=self.id).save() for asistente in self.asistentes]

        DB_CONEXION.commit()
        cursor.close()
                 

    def delete(self):
        ''' Elimina los eventos y asistentes correspondientes al objeto.
 
        Raises:
            ValueError: En caso que no exista el registro en la base de datos.
            RuntimeError: En caos que no exsta conexión a la base de datos.
        '''
        if not DB_CONEXION:
            raise RuntimeError('No hay conexion a la base de datos')
        
        if not self.exists:
            raise ValueError(f'El objeto de id = {self.id} no existe en la base de datos')
        cursor = DB_CONEXION.cursor()
        
        # Elimino todos los registros de asistentes del evento
        [asistente.delete() for asistente in Asistente.objects(evento=self.id)]

        sqlQuery = f'DELETE FROM eventos WHERE id = {self.id}'
        cursor.execute(sqlQuery)
 
        DB_CONEXION.commit()
        cursor.close()
 

    def add_asistente(self, mail):
        if not self.exists:
            raise ValueError("Guadar el evento antes de añadir un asistente")
        
        asistente = Asistente(mail=mail, evento=self.id)

        if asistente.mail not in self.asistentes:
            asistente.save()
            self.asistentes.append(asistente.mail)



    def delete_asistente(self, mail):
        if not self.exists:
            raise ValueError("Guadar el evento antes de eliminar un asistente")
        
        asistente = Asistente.objects(mail=mail, evento=self.id)
        if asistente:
            asistente[0].delete()
            

class Asistente:
    def __init__(self, mail:str, evento:int, id:int=None) -> None:
        self.id = id
        self.mail = mail
        self.evento = evento

    def __str__(self):
        return self.mail
    
    def __eq__(self, other):
        return self.mail == other.mail and self.evento == other.evento

    @classmethod
    def objects(cls, _operator:str="AND", **kwargs):
        ''' Método de clase. Devuelve como instancias de Asistentes, los registros de la 
            base de datos que conincidan con las condiciones recibidas como kwargs.
 
        Parameters:
            dict kwargs: conjunto de pares "campo=valor" como condicón de filtro.
            str _operator: "AND" por defecto. Indica como se conjugan el conjunto de condiciones recibidas.
        Returns:
            list:   - Lista de objetos coincidentes con los criterios indicados.
                    - Lista vacía en caso que ningún registro coincida con los criterios indicados.
        Raises:
            RuntimeError: En caos que no exsta conexión a la base de datos.
        '''
        asistentes = []
        if not DB_CONEXION:
            raise RuntimeError('No hay conexion a la base de datos')
        cursor = DB_CONEXION.cursor()
        
        sqlQuery = 'SELECT * FROM asistentes'
        if kwargs:
            sqlQuery += ' WHERE '
            sqlQuery += f' {_operator} '.join([f'{k} = "{v}"' for k, v in kwargs.items()])

        cursor.execute(sqlQuery)
        registros = cursor.fetchall()

        for registro in registros:
            asistentes.append(cls(
                id = registro[0],
                mail = registro[1],
                evento = registro[2]
            ))
        cursor.close()

        return asistentes


    @property
    def exists(self):
        ''' Indica si el objeto existe en la base de datos.
 
        Returns:
            bool: True en caso que el objeto esta guardado en la base de datos. False en caso contrario.
        Raises:
            RuntimeError: En caos que no exsta conexión a la base de datos.
        '''
        if not DB_CONEXION:
            raise RuntimeError('No hay conexion a la base de datos')
        cursor = DB_CONEXION.cursor()
        
        sqlQuery = f'SELECT * FROM asistentes WHERE (mail="{self.mail}" AND evento={self.evento}) OR (id={self.id if self.id else -1});'
        cursor.execute(sqlQuery)

        existe = True if cursor.fetchone() else False
        cursor.close()
 
        return existe

    def save(self):
        if not self.exists:
            cursor = DB_CONEXION.cursor()

            valores = (
                self.mail,
                self.evento,
                self.id
            )

            cursor.execute('INSERT INTO asistentes(mail, evento, id) VALUES(?,?,?)', valores)
            self.id = int(cursor.lastrowid)
            
            DB_CONEXION.commit()
            cursor.close()

    def delete(self):
        if not self.exists:
            raise ValueError(f'El objeto de id = {self.id} no existe en la base de datos')
        cursor = DB_CONEXION.cursor()

        sqlQuery = f'DELETE FROM asistentes WHERE id = {self.id}'
        cursor.execute(sqlQuery)
 
        DB_CONEXION.commit()
        cursor.close()
