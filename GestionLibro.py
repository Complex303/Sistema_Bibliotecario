import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Conexion import conexion
from GestionLibroInsertar import libros

class FormularioLibro:

    global base
    base = None

    global entry_id
    entry_id = None

    global entry_titulo
    entry_titulo = None

    global entry_autor
    entry_autor = None

    global entry_editorial
    entry_editorial = None

    global entry_cantidadT
    entry_cantidadT = None

    global entry_cantidadD
    entry_cantidadD = None

    global combo
    combo = None

    global group_box
    group_box= None

    global group_box2
    group_box2 = None

    global tree
    tree = None


def formulario():
        global base
        global entry_id
        global entry_titulo
        global entry_autor
        global entry_editorial
        global entry_cantidadT
        global entry_cantidadD
        global combo
        global group_box
        global group_box2
        global tree


        try:
            base = tk.Tk()
            base.geometry('1400x500+20+20')  # Asegura una ventana lo suficientemente ancha
            base.title('Gestión de libros')
            base.config(bg='#ADD8E6')

            # Crear un LabelFrame para agrupar los elementos
            group_box = tk.LabelFrame(base, text='Datos del libro', padx=5, pady=5)
            group_box.grid(row=0, column=0, padx=10, pady=10, sticky='w')

            # Definir las etiquetas y campos de entrada
            label_id = tk.Label(group_box, text='ID:', width=13, font=('Arial', 12), anchor='w')
            label_id.grid(row=0, column=0, sticky='w')
            entry_id = tk.Entry(group_box)
            entry_id.grid(row=0, column=1, sticky='w')

            label_titulo = tk.Label(group_box, text='Título:', width=13, font=('Arial', 12), anchor='w')
            label_titulo.grid(row=1, column=0, sticky='w')
            entry_titulo = tk.Entry(group_box)
            entry_titulo.grid(row=1, column=1, sticky='w')

            label_autor = tk.Label(group_box, text='Autor:', width=13, font=('Arial', 12), anchor='w')
            label_autor.grid(row=2, column=0, sticky='w')
            entry_autor = tk.Entry(group_box)
            entry_autor.grid(row=2, column=1, sticky='w')

            label_editorial = tk.Label(group_box, text='Editorial:', width=13, font=('Arial', 12), anchor='w')
            label_editorial.grid(row=3, column=0, sticky='w')
            entry_editorial = tk.Entry(group_box)
            entry_editorial.grid(row=3, column=1, sticky='w')

            label_cantidadT = tk.Label(group_box, text='Cantidad total:', width=13, font=('Arial', 12), anchor='w')
            label_cantidadT.grid(row=4, column=0, sticky='w')
            entry_cantidadT = tk.Entry(group_box)
            entry_cantidadT.grid(row=4, column=1, sticky='w')

            label_cantidadD = tk.Label(group_box, text='Cantidad disponible:', width=20, font=('Arial', 12), anchor='w')
            label_cantidadD.grid(row=5, column=0, sticky='w')
            entry_cantidadD = tk.Entry(group_box)
            entry_cantidadD.grid(row=5, column=1, sticky='w')

            label_genero = tk.Label(group_box, text='Género:', width=13, font=('Arial', 12), anchor='w')
            label_genero.grid(row=6, column=0, sticky='w')
            seleccionGenero = tk.StringVar()
            combo = ttk.Combobox(group_box, values=[' ', 'Realismo mágico', 'Distopía', 'Novela', 'Romántico', 'Drama', 
                'Fantasía', 'Thriller', 'Novela negra', 'Histórica', 'Fábula', 'Ciencia ficción', 
                'No ficción', 'Misterio', 'Aventura', 'Policíaco', 'Horror', 'Poesía', 
                'Biografía', 'Autobiografía', 'Ensayo', 'Satírico', 'Épico', 'Literatura infantil',
                'Gótico', 'Suspenso', 'Teatro', 'Novela gráfica'], textvariable=seleccionGenero, width=17)
            combo.grid(row=6, column=1)

            # Botones de acción
            tk.Button(group_box, text='Guardar', width=10, command = guardarRegistros).grid(row=7, column=0, sticky= 'w', pady= 5)
            tk.Button(group_box, text='Modificar', width=10, command= ModificarRegistros).grid(row=7, column=1, sticky= 'w', pady=5)
            tk.Button(group_box, text='Eliminar', width=10, command = EliminiarRegistros).grid(row=7, column=2, pady=5)
            btn_atras = ttk.Button(base, text="Regresar", command = regresar_atras)
            btn_atras.place(x=20, y=450)

            style = ttk.Style()
            style.configure('TButton',
                        background='#FFFFFF',
                        foreground='black',
                        font=('Andale Mono Regular', 10, 'bold'),
                        borderwidth=1,
                        relief='raised')

            style.map('TButton',
                  background=[('active', '#87CEFA')])

            # Crear otro LabelFrame para el Treeview
            group_box2 = tk.LabelFrame(base, text='Lista de libros', padx=5, pady=5)
            group_box2.grid(row=0, column=1, padx=5, pady=35)

            # Crear el Treeview
            tree = ttk.Treeview(group_box2, columns=('ID', 'Titulo', 'Autor', 'Editorial', 'Genero', 
                                                     'CantidadTotal', 'CantidadDisponible'), show='headings', height='14',)

            # Configurar las columnas
            tree.column('#1', anchor='center', width=50)
            tree.heading('#1', text='ID')

            tree.column('#2', anchor='center', width=200)
            tree.heading('#2', text='Título')

            tree.column('#3', anchor='center', width=150)
            tree.heading('#3', text='Autor')

            tree.column('#4', anchor='center', width=150)
            tree.heading('#4', text='Editorial')

            tree.column('#5', anchor='center', width=120)
            tree.heading('#5', text='Género')

            tree.column('#6', anchor='center', width=120)
            tree.heading('#6', text='Cantidad Total')

            tree.column('#7', anchor='center', width=150)
            tree.heading('#7', text='Cantidad Disponible')

             # Crear la barra de desplazamiento
            scrollbar = ttk.Scrollbar(group_box2, orient='vertical', command=tree.yview)
            tree.configure(yscroll=scrollbar.set)
            
            # Colocar la barra de desplazamiento en el lado derecho del Treeview
            scrollbar.pack(side='right', fill='y')

            # Empaquetar el Treeview
            tree.pack(side='left', fill='both', expand=True)


            #row = libros.mostrarClientes()[0] #si quiero solo acceder a la primera fila

            #primero_cinco = libros.mostrarClientes()[:5] #para mostrar los primeros cincos registros
            #for row in primero_cinco: 

            #agregar los datos a la tabla
            #mostrar tabla

            for row in libros.mostrarClientes():
            # Inserta cada columna de la fila en su respectivo lugar
                tree.insert("", "end", values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))


            #ejecutar la funcion al hacer click y mostrar el resultado de los entry

            tree.bind('<<TreeviewSelect>>',seleccionarRegistros)

            tree.pack()

            base.mainloop()

        except ValueError as error:
            print('Error al mostrar la interfaz: {}'.format(error))

def guardarRegistros():
        global entry_titulo, entry_autor, entry_editorial, entry_cantidadT, entry_cantidadD, combo, group_box

        try:
            #verificar que los widgets esten inicializados
            if entry_titulo is None or entry_autor is None or entry_editorial is None or entry_cantidadT is None or \
                  entry_cantidadD is None or combo is None:
                print('Los widgets no estan inicializados')
                return
            
            titulo = entry_titulo.get()
            autor = entry_autor.get()
            editoria = entry_editorial.get()
            cantidadTotal = entry_cantidadT.get()
            cantidadDisponible = entry_cantidadD.get()
            genero = combo.get()

            # Verificar que los campos no estén vacíos
            if (not titulo or not autor or not editoria or not cantidadTotal or
                not cantidadDisponible or not genero):
                messagebox.showwarning('Advertencia', 'Por favor, complete todos los campos.')
                return

            # Verificar que los campos numéricos sean enteros
            try:
                cantidadTotal = int(cantidadTotal)
                cantidadDisponible = int(cantidadDisponible)
            except ValueError:
                messagebox.showwarning('Advertencia', 'Cantidad Total y Cantidad Disponible deben ser números enteros.')
                return

            result = libros.ingresarLibros(titulo, autor, editoria, cantidadTotal, cantidadDisponible, genero)
            
            if result:
                messagebox.showinfo('Informacion', 'Los datos fueron guardados')

            actulizarTreeView()

            entry_titulo.delete(0, tk.END)
            entry_autor.delete(0, tk.END)
            entry_editorial.delete(0, tk.END)
            entry_cantidadT.delete(0, tk.END)
            entry_cantidadD.delete(0, tk.END)
            combo.current(0)
        
        except ValueError as err:
            print('Error al ingresar los datos {}'.format(err))


def actulizarTreeView():
     global tree

     try:
          #borrar todos los elementos actuales de mi treeview
          tree.delete(*tree.get_children())

          #obtener los datos que deseamos mostrar
          datos = libros.mostrarClientes()

          #insertar los nuevos datos en el treeview
          for row in libros.mostrarClientes():
            # Inserta cada columna de la fila en su respectivo lugar
                tree.insert("", "end", values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

     except ValueError as error:
          print('Error al actualizar tabla {}'.format(error))


def seleccionarRegistros(event):
     try:
          itemSeleccionado = tree.focus()

          if itemSeleccionado:
               values = tree.item(itemSeleccionado)['values']

               entry_id.delete(0, tk.END)
               entry_id.insert(0, values[0])

               entry_titulo.delete(0, tk.END)
               entry_titulo.insert(0, values[1])

               entry_autor.delete(0, tk.END)
               entry_autor.insert(0, values[2])

               entry_editorial.delete(0, tk.END)
               entry_editorial.insert(0, values[3])

               combo.set(values[4])

               entry_cantidadT.delete(0, tk.END)
               entry_cantidadT.insert(0, values[5])

               entry_cantidadD.delete(0, tk.END)
               entry_cantidadD.insert(0, values[6])

     except ValueError as error:
        print('Error al seleccionar registro {}'.format(error))



def ModificarRegistros():
        global entry_id, entry_titulo, entry_autor, entry_editorial, entry_cantidadT, entry_cantidadD, combo, group_box

        try:
            #verificar que los widgets esten inicializados
            if entry_id is None or entry_titulo is None or entry_autor is None or \
                  entry_editorial is None or entry_cantidadT is None or \
                  entry_cantidadD is None or combo is None:
                print('Los widgets no estan inicializados')
                return
            
            idLibro = entry_id.get()
            titulo = entry_titulo.get()
            autor = entry_autor.get()
            editoria = entry_editorial.get()
            cantidadTotal = entry_cantidadT.get()
            cantidadDisponible = entry_cantidadD.get()
            genero = combo.get()

            # Verificar que los campos no estén vacíos
            if (not idLibro or not titulo or not autor or not editoria or not cantidadTotal or
                not cantidadDisponible or not genero):
                messagebox.showwarning('Advertencia', 'Por favor, complete todos los campos.')
                return

            # Verificar que los campos numéricos sean enteros
            try:
                cantidadTotal = int(cantidadTotal)
                cantidadDisponible = int(cantidadDisponible)
            except ValueError:
                messagebox.showwarning('Advertencia', 'Cantidad Total y Cantidad Disponible deben ser números enteros.')
                return

            result = libros.ModificarLibro(idLibro, titulo, autor, editoria, cantidadTotal, cantidadDisponible, genero)
            
            if result:
                messagebox.showinfo('Informacion', 'Los datos fueron Actualizados')

            actulizarTreeView()

            entry_id.delete(0, tk.END)
            entry_titulo.delete(0, tk.END)
            entry_autor.delete(0, tk.END)
            entry_editorial.delete(0, tk.END)
            entry_cantidadT.delete(0, tk.END)
            entry_cantidadD.delete(0, tk.END)
            combo.current(0)
        
        except ValueError as err:
            print('Error al actualizar los datos {}'.format(err))



def EliminiarRegistros():
        global entry_id, entry_titulo, entry_autor, entry_editorial, entry_cantidadT, entry_cantidadD, combo

        try:
            #verificar que los widgets esten inicializados
            if entry_id is None:
                print('Los widgets no estan inicializados')
                return
            
            idLibro = entry_id.get()
            

            # Verificar que los campos no estén vacíos
            if not idLibro:
                messagebox.showwarning('Advertencia', 'Debe completar el campo ID para hacer la eliminacion.')
                return


            result = libros.EliminarLibro(idLibro)
            
            if result:
                messagebox.showinfo('Informacion', 'los datos fueron elimnados')

            actulizarTreeView()

            entry_id.delete(0, tk.END)
            entry_titulo.delete(0, tk.END)
            entry_autor.delete(0, tk.END)
            entry_editorial.delete(0, tk.END)
            entry_cantidadT.delete(0, tk.END)
            entry_cantidadD.delete(0, tk.END)
            combo.current(0)
        
        except ValueError as err:
            print('Error al eliminar el registro {}'.format(err))

def regresar_atras():
        base.destroy()
        from Principal import principal
        principal()




