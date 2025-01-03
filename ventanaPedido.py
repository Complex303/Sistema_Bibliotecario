import tkinter as tk
from tkinter import ttk
from Conexion import conexion
from tkinter import messagebox
from datetime import datetime

class Prestamo:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Registrar Prestamo de libro")
        self.ventana.geometry("650x550")
        self.ventana.resizable(False, False)
        self.ventana.config(bg='#ADD8E6')
        self.ventana.iconbitmap(r'icono.ico')

        #imagen logo. # Cargamos una imagen de fondo desde el archivo "coca-cola-p.png" y la colocamos en la ventana
        self.fondo = tk.PhotoImage(file='library.png')
        self.label_fondo = tk.Label(self.ventana, image=self.fondo, bg='#ADD8E6').place(x=0, y=0)

        #label detalle
        self.l_detalle = tk.Label(self.ventana, text='Datos del prestamo de libro')
        self.l_detalle.config(bg='#ADD8E6', font=('Andale Mono Regular', 18, 'bold'))
        self.l_detalle.place(x=300, y=40)

        #label nombre completo
        self.l_nombre = tk.Label(self.ventana, text='Nombre completo del estudiante')
        self.l_nombre.config(bg='#ADD8E6', font=('Andale Mono Regular', 11, 'bold'))
        self.l_nombre.place(x=28, y=180)

        #entry nombre completo
        self.datonombre = tk.StringVar() 
        self.e_nombre = tk.Entry(self.ventana, bd=2, bg='#eee8e8', textvariable=self.datonombre)
        self.e_nombre.config(font=('Andale Mono Regular', 12), width=22)
        self.e_nombre.place(x=30, y=205)

        
        self.l_titulo = tk.Label(self.ventana, text='Titulo del libro') 
        self.l_titulo.config(bg='#ADD8E6', font=('Andale Mono Regular', 11, 'bold'))
        self.l_titulo.place(x=28, y=240)

        self.datotitulo = tk.StringVar() 
        self.e_titulo = tk.Entry(self.ventana, bd=2, bg='#eee8e8', textvariable=self.datotitulo)
        self.e_titulo.config(font=('Andale Mono Regular', 12), width=22)
        self.e_titulo.place(x=30, y=265)

        self.l_fecha = tk.Label(self.ventana, text='Fecha Devolucion')
        self.l_fecha.config(bg='#ADD8E6', font=('Andale Mono Regular', 11, 'bold'))
        self.l_fecha.place(x=28, y=300)

        self.datofecha = tk.StringVar()
        self.e_fecha = tk.Entry(self.ventana, bd=2, bg='#eee8e8', textvariable=self.datofecha)
        self.e_fecha.config(font=('Andale Mono Regular', 12,), width=22)
        self.e_fecha.place(x=30, y=325)

        estilo = ttk.Style()
        estilo.theme_use('clam')
        estilo.configure('TCombobox', background='#ADD8E6')

        self.l_gestion = tk.Label(self.ventana, text='Gestionado por')
        self.l_gestion.config(bg='#ADD8E6', font=('Andale Mono Regular', 11, 'bold'))
        self.l_gestion.place(x=350, y=180)

        self.var_combo1 = tk.StringVar()
        self.op_combo1 = (' ', 'Juan Perez', 'Ana Gomez', 'Carlos Lopez')
        self.combobox1 = ttk.Combobox(self.ventana, state='readonly', width=22,
                                      font=('Andale Mono Regular', 9, 'bold'),
                                      textvariable=self.var_combo1, values=self.op_combo1)
        self.combobox1.current(0)
        self.combobox1.place(x=350, y=210)

        self.l_resultadoPrestamo = tk.Label(self.ventana, text='Prestamo Registrado con exito!!')
        self.l_resultadoPrestamo.config(bg='#ADD8E6', font=('Andale Mono Regular', 11, 'bold'))
        self.l_resultadoPrestamo.forget()
        
        self.area_resultado = tk.Text(self.ventana, bd=2, font=('Andale Mono Regular', 10))
        self.area_resultado.config(width=43, height=8, state='disabled')
        self.area_resultado.forget()

        self.l_footer = tk.Label(self.ventana, text='Instituto Politecnico Victor Estrella Liz.')
        self.l_footer.config(bg='#ADD8E6', font=('Andale Mono Regular', 10, 'bold'))
        self.l_footer.place(x=200, y=500)

        self.btn_enviar = ttk.Button(self.ventana, text="Registrar", command = self.insertar_prestamo)
        self.btn_enviar.place(x=30, y=375)

        self.btn_borrar = ttk.Button(self.ventana, text="Limpiar", command= self.limpiar_datos)
        self.btn_borrar.place(x=140, y=375)

        self.btn_atras = ttk.Button(self.ventana, text="Regresar", command = self.regresar_atras)
        self.btn_atras.place(x=20, y=500)

        self.btn_imprimir = ttk.Button(self.ventana, text="Imprimir", command  = self.generarReporte)
        self.btn_imprimir.place(x=520, y=500)

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
        
        self.ventana.mainloop()
        
    def insertar_prestamo(self):
        self.titulo = self.e_titulo.get().strip()
        self.nombre_estudiante = self.datonombre.get().strip()
        self.gestionado_por = self.var_combo1.get().strip()
        self.fecha_devolucion = self.e_fecha.get().strip()

    # Verificar que todos los campos estén llenos
        if not self.titulo or not self.nombre_estudiante or not self.gestionado_por or not self.fecha_devolucion:
            messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")
            return

        db = conexion()
        db.conectar()

        if db.conn:
            try:
            # 1. Buscar el LibroID basado en el título
                query_libro = "SELECT LibroID FROM Libro WHERE Titulo = ?"
                db.cursor.execute(query_libro, (self.titulo,))
                resultado_libro = db.cursor.fetchone()

                # 2. Buscar el UsuarioID basado en el nombre del estudiante
                query_usuario = "SELECT UsuarioID FROM Usuario WHERE Nombre = ?"
                db.cursor.execute(query_usuario, (self.nombre_estudiante,))
                resultado_usuario = db.cursor.fetchone()

                # 3. Buscar el EmpleadoID basado en el nombre del "Gestionado por"
                query_empleado = "SELECT PersonalID FROM Personal WHERE Nombre = ?"
                db.cursor.execute(query_empleado, (self.gestionado_por,))
                resultado_empleado = db.cursor.fetchone()

                # Si todos los valores existen en la base de datos
                if resultado_libro and resultado_usuario and resultado_empleado:
                    libro_id = resultado_libro[0]
                    usuario_id = resultado_usuario[0]
                    empleado_id = resultado_empleado[0]

                    # 4. Insertar el préstamo en la tabla Prestamo usando los IDs y la fecha de devolución
                    query_prestamo = """
                    INSERT INTO Prestamo (UsuarioID, LibroID, FechaPrestamo, Estado, GestionadoPor, FechaDevolucion)
                    VALUES (?, ?, GETDATE(), 1, ?, ?)
                    """
                    db.cursor.execute(query_prestamo, (usuario_id, libro_id, empleado_id, self.fecha_devolucion))
                    db.conn.commit()
                    
                    messagebox.showinfo("Éxito", "Préstamo registrado con éxito.")

                    self.l_resultadoPrestamo.place(x=350, y=280)
                    self.area_resultado.place(x=310, y=320)
                    fecha_actual = datetime.now()
                    fecha_formato = fecha_actual.strftime('%Y-%m-%d')

                    self.reporte = f"""Préstamo Registrado:
Nombre del Estudiante: {self.nombre_estudiante}
Título del Libro: {self.titulo}
Fecha de entrega: {fecha_formato}
Fecha de Devolución: {self.fecha_devolucion}
Gestionado por: {self.gestionado_por}
"""

                   
                    self.area_resultado.config(state='normal')
                    self.area_resultado.delete(1.0, tk.END)  
                    self.area_resultado.insert(tk.END, self.reporte)  
                    self.area_resultado.config(state='disabled') 

                else:
                    messagebox.showerror("Error", "Algunos datos no se encontraron en la base de datos.")
                
            except Exception as e:
                db.conn.rollback()
                messagebox.showerror("Error", f"Error al insertar el préstamo: {str(e)}")
            finally:
                db.cerrar()


    def limpiar_datos(self):
        self.e_nombre.delete(0, tk.END)
        self.e_titulo.delete(0, tk.END)
        self.e_fecha.delete(0, tk.END)
        self.combobox1.current(0)
        self.area_resultado.config(state = 'normal')
        self.area_resultado.delete('1.0', 'end')
        self.area_resultado.config(state = 'disabled')

    def regresar_atras(self):
        self.ventana.destroy()
        from Principal import principal
        principal()

    def generarReporte(self):
        with open("reporte_prestamo.txt", "w") as file:
            file.write(self.reporte)

        messagebox.showinfo("Exportar", "Reporte exportado con éxito")

