import tkinter as tk
from tkinter import ttk
from Conexion import conexion

class Consulta:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Consulta de libros")
        self.ventana.geometry("600x500")
        self.ventana.resizable(False, False)
        self.ventana.config(bg='#ADD8E6')
        self.ventana.iconbitmap(r'icono.ico')

        style = ttk.Style()
        style.configure('TButton',
                        background='#4CAF50',  
                        foreground='black',  
                        font=('Andale Mono Regular', 10, 'bold'),  
                        borderwidth=1,  
                        relief='raised')  

        style.map('TButton',
                background=[('active', '#45a049')])

          # Definir los widgets como atributos de instancia
        self.entry = tk.Entry(self.ventana, width=40, bd=2, bg='#eee8e8', font=('Andale Mono Regular', 10, 'bold'))
        self.entry.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.btn_enviar = ttk.Button(self.ventana, text="Consultar", command=self.buscar_libro)
        self.btn_enviar.grid(row=0, column=1, padx=5, pady=10)

        self.btn_borrar = ttk.Button(self.ventana, text="Borrar", command=self.borrar)
        self.btn_borrar.grid(row=0, column=2, padx=5, pady=10)

        # Botón para regresar a la ventana anterior
        self.btn_regresar = ttk.Button(self.ventana, text="Regresar", command=self.volver_atras)
        self.btn_regresar.grid(row=0, column=3, padx=5, pady=10)

        frame_text = tk.Frame(self.ventana)
        frame_text.grid(row=1, column=0, columnspan=4, padx=10, pady=6, sticky="nsew")

        self.text_area = tk.Text(frame_text, height=25, width=70, state='disabled')
        self.text_area.grid(row=0, column=0, sticky='nsew')

        scrollbar = tk.Scrollbar(frame_text, orient=tk.VERTICAL, command=self.text_area.yview)
        scrollbar.grid(row=0, column=1, sticky='ns')

        self.text_area.config(yscrollcommand=scrollbar.set)

        frame_status = tk.Frame(self.ventana, bg='#ADD8E6')
        frame_status.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

        self.status_label = tk.Label(frame_status, text="Esperando una instrucción...", anchor="w", bg='#ADD8E6')
        self.status_label.pack()

        self.ventana.grid_rowconfigure(1, weight=1)
        self.ventana.grid_rowconfigure(2, weight=0)
        self.ventana.grid_columnconfigure(0, weight=1)
        self.ventana.grid_columnconfigure(1, weight=1)
        self.ventana.grid_columnconfigure(2, weight=1)
        self.ventana.grid_columnconfigure(3, weight=1)

        self.ventana.mainloop()

    def buscar_libro(self):
        libro = self.entry.get().strip()

        if not libro:
            self.text_area.config(state='normal')
            self.text_area.delete(1.0, tk.END)
            self.text_area.insert(tk.END, "Por favor, ingresa un título o un '*' para buscar todos los libros.\n")
            self.status_label.config(text="Por favor, ingrese una consulta.")
            self.text_area.config(state='disabled')
            return

        db = conexion()
        db.conectar()

        if db.conn:
            try:
                if libro == '*':
                    query = "SELECT [Titulo], [Autor], [Editorial], [Genero], [CantidadTotal], [CantidadDisponible] FROM Libro"
                else:
                    query = (f"SELECT [Titulo], [Autor], [Editorial], [Genero], [CantidadTotal], [CantidadDisponible] "
                            f"FROM Libro WHERE Titulo LIKE ?")

                
                db.cursor.execute(query, ('%' + libro + '%',) if libro != '*' else ())
                resultados = db.cursor.fetchall()
                numero_registro = len(resultados)

                self.text_area.config(state='normal')
                self.text_area.delete(1.0, tk.END)

                if resultados:
                    for row in resultados:
                        self.text_area.insert(tk.END, 
                        f"Título: {row[0]}\nAutor: {row[1]}\nEditorial: {row[2]}\nGénero: {row[3]}\n"
                        f"Cantidad Total: {row[4]}\nCantidad Disponible: {row[5]}\n")

                        self.text_area.insert(tk.END, "---------------------------------\n")
                    
                else:
                    self.text_area.insert(tk.END, "No se encontraron libros con ese título.\n")
                
                self.text_area.config(state='disabled')
                self.status_label.config(text=f"Registros encontrados: {numero_registro}")

            except Exception as err:
                print("Error al ejecutar la consulta:", err)
            finally:
                db.cerrar()

    def borrar(self):
        self.entry.delete(0, tk.END)
        self.text_area.config(state='normal') 
        self.text_area.delete(1.0, tk.END)
        self.text_area.config(state='disabled')  
        self.status_label.config(text="Esperando una instrucción...")

    def volver_atras(self):
        self.ventana.destroy()
        from Principal import principal
        principal()



