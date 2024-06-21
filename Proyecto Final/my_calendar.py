# Alejandro Gonzalez (Diseñado por Lucas Lucik)
# Importamos nuestros modulos que realizamos
import calendar_events as ce, interfaz as ci
 
if __name__ == '__main__':
     
    #Iniciamos la base de datos y lanzamos la interfaz creada
    ce.start_database()
    app = ci.App()