from Conexion import conexion

class libros:
    #@staticmethod
    def ingresarLibros(Titulo, Autor, Editorial, CantidadTotal, CantidadDisponible, Genero,):
        try:
            # Crear una instancia de la clase conexion
            cone = conexion()
            cone.conectar()
            cursor = cone.cursor
            sql = '''INSERT INTO Libro ([Titulo], [Autor], [Editorial], [CantidadTotal], [CantidadDisponible], [Genero])
            VALUES (?, ?, ?, ?, ?, ?);
            '''
            valores = (Titulo, Autor, Editorial,CantidadTotal, CantidadDisponible, Genero,)
            cursor.execute(sql, valores)
            Select = '''SELECT @@ROWCOUNT;'''
            Registro_Afectados = cursor.execute(Select).fetchone()[0]
            print(str(Registro_Afectados) + ' Registros ingresados')
            cone.conn.commit()
            return True
            
        except Exception as error:
            print('Error de ingreso de datos {}'.format(error))
            cone.conn.rollback()
            return False
        finally:
            cone.cerrar()

    def mostrarClientes():
         try:
            # Crear una instancia de la clase conexion
            cone = conexion()
            cone.conectar()
            cursor = cone.cursor
            cursor.execute('Select * from Libro;')
            miResultado = cursor.fetchall()
            cone.conn.commit()
            return miResultado
         
         except Exception as error:
            print('Error al consulta de datos {}'.format(error))
            return False
         


    def ModificarLibro(LibroID, Titulo, Autor, Editorial, CantidadTotal, CantidadDisponible, Genero,):
        try:
            # Crear una instancia de la clase conexion
            cone = conexion()
            cone.conectar()
            cursor = cone.cursor
            sql = '''UPDATE Libro SET Titulo = ?, Autor = ?, Editorial = ?, 
            CantidadTotal = ?, CantidadDisponible = ?, Genero = ? 
            WHERE LibroID = ?;
            '''
            valores = (Titulo, Autor, Editorial,CantidadTotal, CantidadDisponible, Genero, LibroID)
            cursor.execute(sql, valores)
            Select = '''SELECT @@ROWCOUNT;'''
            Registro_Afectados = cursor.execute(Select).fetchone()[0]
            print(str(Registro_Afectados) + ' Registros Actualizados')
            cone.conn.commit()
            return True
            
        except Exception as error:
            print('Error de actualizacion de datos {}'.format(error))
            cone.conn.rollback()
            return False
        finally:
            cone.cerrar()

    def EliminarLibro(LibroID):
        try:
            # Crear una instancia de la clase conexion
            cone = conexion()
            cone.conectar()
            cursor = cone.cursor
            sql = 'DELETE FROM Libro where LibroID = ?';
            valores = (LibroID)
            cursor.execute(sql, valores)
            Select = '''SELECT @@ROWCOUNT;'''
            Registro_Afectados = cursor.execute(Select).fetchone()[0]
            print(str(Registro_Afectados) + ' Registro Eliminado')
            cone.conn.commit()
            return True
            
        except Exception as error:
            print('Error en la eliminacion de registro {}'.format(error))
            cone.conn.rollback()
            return False
        finally:
            cone.cerrar()

        

    








































# from Conexion import *

# class libros:
#     def ingresarLibros(Titulo, Autor, Editorial, Genero, CantidadTotal, CantidadDisponible):
#         try:
#             cone = conexion
#             cone.conectar()
#             cursor = cone.cursor()
#             sql = '''INSERT INTO Libro ([Titulo], [Autor], [Editorial], [Genero], [CantidadTotal], [CantidadDisponible])
#             VALUES ('%s', '%s', '%s', '%s', %s, %s);'''
#             #la variable valores tiene que ser una tupla
#             #como minima expresion es: (valor,) la coma hace que sea tupla
#             #las tuplas son listas inmutables, eso quiere decir que no se puede modificar
#             valores = (Titulo, Autor, Editorial, Genero, CantidadTotal, CantidadDisponible)
#             cursor.execute(sql,valores)
#             cone.commit()
#             Select = '''SELECT @@ROWCOUNT;'''
#             Registro_Afectados = cursor.execute(Select)
#             print(Registro_Afectados, 'Registros ingreasdos')
            
#         except Exception as error:
#             print('Error de ingreso de datos {}'.format(error))

