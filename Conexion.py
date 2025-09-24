import pyodbc # Importamos la librería pyodbc que permite conectarse y operar con bases de datos ODBC en Python.
import os
from dotenv import load_dotenv

load_dotenv()  # Cargar las variables de entorno desde el archivo .env

class conexion: # Definimos una clase llamada Conexion que encapsula toda la funcionalidad relacionada con la conexión a la bd.
    def __init__(self):

        driver = os.getenv("DRIVER")
        server = os.getenv("Server")
        database = os.getenv("Database")


        #cadena de conexion
        self.cadena_conexion = f'''DRIVER={driver};
                                  Server={server};
                                  Database={database};
                                  Trusted_Connection=yes;'''
        self.conn = None
        self.cursor = None

    def conectar(self):
        try:
            self.conn = pyodbc.connect(self.cadena_conexion)
            self.cursor = self.conn.cursor()
        except Exception as err:
            print('ERROR EN LA CONEXION CON SQL SERVER', err)
            self.conn = None

    def mensaje(self):
        self.cursor.execute('SELECT @@VERSION')
        select = self.cursor.fetchone()
        print('Conectado correctamente!!', select)

    def cerrar(self):
        if self.cursor:
            try:
                self.cursor.close() 
            except Exception as err:
                print('Error cerrando el cursor', err)
        if self.conn:
            try:
                self.conn.close()
                print('Conexion Cerrada correctamente!!')
            except Exception as err:
                print('Error cerrando la conexion', err)


    

        
