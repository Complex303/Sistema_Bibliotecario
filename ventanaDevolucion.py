import tkinter as tk
from tkinter import ttk
from Conexion import conexion
from tkinter import messagebox


class Devolucion:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Devolución de libro")
        self.ventana.geometry("450x550")
        self.ventana.resizable(False, False)
        self.ventana.config(bg='#ADD8E6')
        self.ventana.iconbitmap(r'icono.ico')


        self.fondo = tk.PhotoImage(file=r'library.png')
        self.label_fondo = tk.Label(self.ventana, image=self.fondo, bg='#ADD8E6')
        self.label_fondo.pack()

        
        self.label1 = tk.Label(self.ventana, text='Devolución de libros', fg='black', bg='#ADD8E6', 
                               font=('Andale Mono Regular', 14, 'italic'))
        self.label1.place(x=130, y=170)


        self.prestamo = tk.Label(self.ventana, text='Código del préstamo: ', fg='black', bg='#ADD8E6', 
                                 font=('Andale Mono Regular', 12, 'bold'))
        self.prestamo.place(x=10, y=240)

        self.datoprestamo = tk.StringVar()
        self.e_prestamo = tk.Entry(self.ventana, bd=2, bg='#eee8e8', textvariable=self.datoprestamo, 
                                 font=('Andale Mono Regular', 12), width=22)
        self.e_prestamo.place(x=200, y=240)

      
        self.l_comentario = tk.Label(self.ventana, text='Comentario: ', fg='black', bg='#ADD8E6', 
                                   font=('Andale Mono Regular', 12, 'bold'))
        self.l_comentario.place(x=10, y=300)

        self.e_comentario = tk.Text(self.ventana, bd=2, font=('Andale Mono Regular', 10), width=37, height=8)
        self.e_comentario.place(x=120, y=300)

       
        self.l_footer = tk.Label(self.ventana, text='Instituto Politécnico Victor Estrella Liz.')
        self.l_footer.config(bg='#ADD8E6', font=('Andale Mono Regular', 10, 'bold'))
        self.l_footer.place(x=100, y=520)  # Ajustar la posición

        # Estilo para los botones
        style = ttk.Style()
        style.configure('TButton',
                        background='#FFFFFF',
                        foreground='black',
                        font=('Andale Mono Regular', 10, 'bold'),
                        borderwidth=1,
                        relief='raised')
        style.map('TButton',
                  background=[('active', '#87CEFA')])

        # Botones
        self.btn_enviar = ttk.Button(self.ventana, text="Registrar", command=self.registrar_devolucion)
        self.btn_enviar.place(x=50, y=460)

        self.btn_borrar = ttk.Button(self.ventana, text="Limpiar", command= self.borrar)
        self.btn_borrar.place(x=160, y=460)

        self.btn_atras = ttk.Button(self.ventana, text="Regresar", command= self.regresar_atras)
        self.btn_atras.place(x=270, y=460)

        self.ventana.mainloop()

    def registrar_devolucion(self):
        self.codigo = self.datoprestamo.get().strip()
        self.comentario = self.e_comentario.get("1.0", tk.END).strip()

        if not self.codigo or not self.comentario:
            messagebox.showwarning('Advertencia', 'Todos los campos deben estar completos')
            return

        db = conexion()
        db.conectar()

        if db.conn:
            try:
                query_prestamoid = 'SELECT PrestamoID FROM Prestamo WHERE PrestamoID = ?'
                db.cursor.execute(query_prestamoid, (self.codigo,))
                resultado_codigo = db.cursor.fetchone()

                if resultado_codigo[0] == int(self.codigo):
                    prestamoid = resultado_codigo[0]

                    query_devolucion = """
                    INSERT INTO Devolucion (PrestamoID, FechaDevolucionReal, Comentarios)
                    VALUES (?, GETDATE(), ?)
                    """
                    db.cursor.execute(query_devolucion, (prestamoid, self.comentario))
                    db.conn.commit()

                    messagebox.showinfo("Éxito", "Devolución registrada con éxito")

                else:
                    messagebox.showerror("Error", "Código de préstamo incorrecto")

            except Exception as e:
                db.conn.rollback()
                messagebox.showerror("Error", f"Error al insertar la devolución: {str(e)}")
            finally:
                db.cerrar()
    def borrar(self):
        self.e_prestamo.delete(0, tk.END)
        self.e_comentario.delete('1.0', 'end')

    def regresar_atras(self):
        self.ventana.destroy()
        from Principal import principal
        principal()



