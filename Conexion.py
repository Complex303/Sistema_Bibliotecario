import pyodbc # Importamos la librería pyodbc que permite conectarse y operar con bases de datos ODBC en Python.

class conexion: # Definimos una clase llamada Conexion que encapsula toda la funcionalidad relacionada con la conexión a la bd.
    def __init__(self):
        #cadena de conexion
        self.cadena_conexion = '''DRIVER={SQL SERVER};
                                  Server=Go-8ZG6503\\MSSSQLSERVER_DEV;
                                  Database=Sistema_Bibliotecario;
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


    

        
