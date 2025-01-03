import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from Conexion import conexion
from Licencia import Licencia


class Bienvenida: 
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('Acceso')
        self.ventana.iconbitmap(r'C:\Users\eddy\OneDrive\Escritorio\Sistema Bibliotecario\icono.ico')
        self.ventana.resizable(False, False)
        self.ventana.config(bg='#ADD8E6')
        self.ventana.geometry('450x550+600+200')

        self.fondo = tk.PhotoImage(file=r'library.png')
        self.label_fondo = tk.Label(self.ventana, image=self.fondo, bg='#ADD8E6').pack()

        self.label1 = tk.Label(self.ventana, text='Sistema Bibliotecario')
        self.label1.config(fg='black', bg='#ADD8E6', font=('Andale Mono Regular', 18, 'italic'))
        self.label1.place(x=110, y=170)

        self.label1 = tk.Label(self.ventana, text='Instituto Politecnico Victor Estrella Liz')
        self.label1.config(fg='black', bg='#ADD8E6', font=('Andale Mono Regular', 18, 'italic'))
        self.label1.place(x=20, y=210)

        self.label2 = tk.Label(self.ventana, text='Ingrese su nombre:')
        self.label2.config(fg='black', bg='#ADD8E6', font=('Andale Mono Regular', 12, 'bold'))
        self.label2.place(x=140, y=280)


        self.dato1 = tk.StringVar()
        self.entry1 = tk.Entry(self.ventana, bd=2, bg='#eee8e8', fg='#00008B', textvariable=self.dato1)
        self.entry1.config(font=('Andale Mono Regular', 12, 'bold'), width=27)
        self.entry1.place(x=90, y=320)

        self.label5 = tk.Label(self.ventana, text='Ingrese su constraseña:')
        self.label5.config(fg='black', bg='#ADD8E6', font=('Andale Mono Regular', 12, 'bold'))
        self.label5.place(x=125, y=370)

        self.dato2 = tk.StringVar()
        self.entry2 = tk.Entry(self.ventana, bd=2, bg='#eee8e8', fg='#00008B', textvariable=self.dato2, show = '*')
        self.entry2.config(font=('Andale Mono Regular', 12, 'bold'), width=27)
        self.entry2.place(x=90, y=410)

        self.boton1 = ttk.Button(self.ventana, text='Ingresar',   style='TButton', command= self.acceso)
        self.boton1.config(width=12)
        self.boton1.place(x=50, y=480)

        self.boton1 = ttk.Button(self.ventana, text='Limpiar', style='TButton', command = self.limpiar)
        self.boton1.config(width=12)
        self.boton1.place(x=250, y=480)

        estilo = ttk.Style()
        estilo.configure('TButton', font=('Arial', 10, 'bold'), padding=10)

        
        self.ventana.mainloop()

    def limpiar(self):
        self.entry1.delete('0', 'end')
        self.entry2.delete('0','end')

    
    def acceso(self):
        nombre_usuario = self.dato1.get()
        self.usuario = self.dato1.get()
        contraseña_usuario = self.dato2.get()
        self.contraseña = self.dato2.get()
        if not self.dato1.get():  
            messagebox.showerror('ATENCION', 'DEBE COLOCAR NOMBRE DE USUARIO')
        elif not self.dato2.get():  
            messagebox.showerror('ATENCION', 'DEBE COLOCAR CONTRASEÑA DE USUARIO')
        else:
            conn = conexion() # Crear una instancia de la clase Conexion
            conn.conectar() #llamamos a la funcion o metodo conectar, que es donde establece la conexión con la base de datos.
            if conn.conn:
                try:
                    conn.cursor.execute('Select Nombre, Contraseña from Personal')
                    Usuario = {};
                    for row in conn.cursor.fetchall():
                        Usuario[row[0]] = row[1] #Agrega el nombre de usuario como clave y la contraseña como valor en el diccionario usuarios
                    if nombre_usuario in Usuario:
                        if contraseña_usuario == Usuario[nombre_usuario]:
                            conn.mensaje() # Si el nombre de usuario y la contraseña coinciden, mostramos un mensaje de conexión exitosa
                            self.ventana.destroy()
                            Licencia()
                        else:
                            messagebox.showerror('ATENCION', 'CONTRASEÑA INCORRECTA')
                    else:
                        messagebox.showerror('ATENCION', 'USUARIO INCORRECTO')
                except Exception as e: # Si ocurre un error al ejecutar la consulta, mostramos un mensaje de error.
                    messagebox.showerror('ATENCION', f'ERROR AL VERIFICAR EL USUARIO: {e}')
                finally:  #En cualquier caso, cerramos la conexión a la base de datos.
                    conn.cerrar()
            else: # Si no se pudo establecer la conexión, mostramos un mensaje de error.
                messagebox.showerror('ATENCIÓN', 'Error al conectar a la base de datos')

if __name__ == '__main__':
    Ejecutar = Bienvenida()
