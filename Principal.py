import sys
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


class principal:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Ventana Principal")
        self.ventana.resizable(False, False)
        self.ventana.geometry('850x550+310+100')
        self.ventana.config(bg='#ADD8E6')
        self.ventana.iconbitmap(r'icono.ico')

        # Barra de menú principal
        self.menubar1 = tk.Menu(self.ventana)
        self.ventana.config(menu=self.menubar1)

        # Menú Mantenimiento
        self.opciones1 = tk.Menu(self.menubar1, tearoff=0)
        self.menubar1.add_cascade(label='Mantenimiento', menu=self.opciones1)
        self.opciones1.add_command(label='Agregar nuevo', font=('Arial', 10, 'bold'))
        self.opciones1.add_command(label='Editar', font=('Arial', 10, 'bold'))
        self.opciones1.add_command(label='Eliminar', font=('Arial', 10, 'bold'))
        self.opciones1.add_separator()
        self.opciones1.add_command(label='Salir', command=self.salir, font=('Arial', 10, 'bold'))

        # Menú Consulta
        self.opciones2 = tk.Menu(self.menubar1, tearoff=0)
        self.menubar1.add_cascade(label='Consulta', menu=self.opciones2)
        self.opciones2.add_command(label='Buscar registro', font=('Arial', 10, 'bold'))
        self.opciones2.add_command(label='Ver todos', font=('Arial', 10, 'bold'))

        # Menú Reporte
        self.opciones3 = tk.Menu(self.menubar1, tearoff=0)
        self.menubar1.add_cascade(label='Reporte', menu=self.opciones3)
        self.opciones3.add_command(label='Generar reporte', font=('Arial', 10, 'bold'))
        self.opciones3.add_command(label='Exportar a PDF', font=('Arial', 10, 'bold'))
        self.opciones3.add_command(label='Exportar a Excel', font=('Arial', 10, 'bold'))

        # Menú Configuración
        self.opciones4 = tk.Menu(self.menubar1, tearoff=0)
        self.menubar1.add_cascade(label='Configuración', menu=self.opciones4)
        self.opciones4.add_command(label='Preferencias', font=('Arial', 10, 'bold'))
        self.opciones4.add_command(label='Cambiar tema', font=('Arial', 10, 'bold'))

        # Menú Ayuda
        self.opciones5 = tk.Menu(self.menubar1, tearoff=0)
        self.menubar1.add_cascade(label='Ayuda', menu=self.opciones5)
        self.opciones5.add_command(label='Acerca de...', command=self.acerca, font=('Arial', 10, 'bold'))
        self.opciones5.add_command(label='Documentación', font=('Arial', 10, 'bold'))

        # Imagen en la ventana principal
        self.imagen = tk.PhotoImage(file=r'C:\Users\eddy\OneDrive\Escritorio\Sistema Bibliotecario\biblioprincipal.png')
        self.labelimagen = tk.Label(self.ventana, image=self.imagen)
        self.labelimagen.place(x=-10, y=0)

        self.logo = tk.PhotoImage(file = r'C:\Users\eddy\OneDrive\Escritorio\Sistema Bibliotecario\Biblioo.png')
        self.labellogo = tk.Label(self.ventana, image = self.logo).place(x = 556, y = 20)

        # Botones atractivos al lado derecho de la imagen
        self.boton_buscar = ttk.Button(self.ventana, text="Buscar libros", style='TButton',  command=self.buscar_libros)
        self.boton_buscar.place(x=580, y=220, width=160, height=60)

        self.boton_prestar = ttk.Button(self.ventana, text="Prestar libros", style='TButton', command=self.prestar_libros)
        self.boton_prestar.place(x=580, y=300, width=160, height=60)

        self.boton_recibir = ttk.Button(self.ventana, text="Recibir libro", style='TButton', command=self.recibir_libro)
        self.boton_recibir.place(x=580, y=380, width=160, height=60)

        self.boton_inventario = ttk.Button(self.ventana, text="Gestionar inventario", style='TButton', 
                                           command=self.gestionar_inventario)
        self.boton_inventario.place(x=580, y=460, width=160, height=60)

        # Estilo de botones
        estilo = ttk.Style()
        estilo.configure('TButton', font=('Arial', 10, 'bold'), padding=10)

        self.ventana.mainloop()

    def salir(self):
        self.ventana.quit()

    def acerca(self):
        messagebox.showinfo("Acerca de", "Información sobre la aplicación")

    def buscar_libros(self):
        self.ventana.destroy()
        from VentanaConsulta import Consulta
        Consulta()

    def prestar_libros(self):
        self.ventana.destroy()
        from ventanaPedido import Prestamo
        Prestamo()

    def recibir_libro(self):
        self.ventana.destroy()
        from ventanaDevolucion import Devolucion
        Devolucion()

    def gestionar_inventario(self):
        self.ventana.destroy()
        from GestionLibro import formulario
        formulario()

    
    def salir(self): 
        seleccion = messagebox.askokcancel('SALIR', 'DESEA SALIR DEL SISTEMA?')
        if seleccion == True:
            sys.exit()


