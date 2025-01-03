import sys
import tkinter as tk
from tkinter import messagebox
from tkinter.font import NORMAL
from Principal import principal


class Licencia:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('LICENCIA Y CONDICIONES')
        self.ventana.resizable(False, False)
        self.ventana.config(bg = 'white')
        self.ventana.geometry('600x350+500+250')
        self.ventana.iconbitmap(r'icono.ico')

        self.logo = tk.PhotoImage(file = r'C:\Users\eddy\OneDrive\Escritorio\Sistema Bibliotecario\Biblio.png')
        self.labellogo = tk.Label(self.ventana, image = self.logo).place(x = 480, y = 230)

        self.label1 = tk.Label(self.ventana, text='TERMINOS Y CONDICIONES')
        self.label1.config(font=('Arial', 13, 'bold'), bg = '#FFFFFF')
        self.label1.place(x=180, y=10)

        self.texto_condiciones = tk.Text(self.ventana, font=('Arial', 8), width=96, height=12)
        self.texto_condiciones.configure(bg='#FFFFFF', state='normal')
        self.texto_condiciones.insert('insert', '''       
    TÉRMINOS Y CONDICIONES"

    A.  PROHIBIDA SU VENTA O DISTRIBUCIÓN SIN AUTORIZACIÓN DE EDDY UREÑA HERNANDEZ.
    B.  PROHIBIDA LA ALTERACIÓN DEL CÓDIGO FUENTE O DISEÑO DE LAS INTERFACES GRÁFICAS.
    C.  EDDY UREÑA HERNANDEZ NO SE HACE RESPONSABLE DEL MAL USO DE ESTE SOFTWARE.

    LOS ACUERDOS LEGALES EXPUESTOS A CONTINUACION RIGEN EL USO QUE USTED HAGA DE ESTE SOFTWARE
    (EDDY UREÑA HERNANDEZ), NO SE RESPONSABILIZA DEL USO QUE USTED"
    HAGA CON ESTE SOFTWARE Y SUS SERVICIOS. PARA ACEPTAR ESTOS TERMINOS HAGA CLIC EN (ACEPTO)"
    SI USTED NO ACEPTA ESTOS TERMINOS, HAGA CLIC EN (NO ACEPTO) Y NO UTILICE ESTE SOFTWARE."
         ''')
        
        self.texto_condiciones.place(x=10, y=40)
        self.texto_condiciones.config(state='disabled')

        self.acepto = tk.IntVar()
        self.check_acepto = tk.Checkbutton(self.ventana, text='Yo acepto', bg = '#FFFFFF', font=('Arial', 12, 'bold'), 
                                           command = self.aceptar)
        self.check_acepto.place(x=10, y=230)

        self.boton_continuar = tk.Button(self.ventana, text = 'Acepto',  font = ('Arial', 11, 'bold'), width = 7, height = -20, 
                                         bd = 3, state = 'disabled', command= self.acceso)
        self.boton_continuar.place(x = 10, y = 290)

        self.boton_cancelar = tk.Button(self.ventana, text = 'Cancelar', font = ('Arial', 11,'bold'), width = 7, height= -20, 
                                        bd = 3, state = NORMAL, command = self.cancelar)
        self.boton_cancelar.place(x = 110, y = 290 )

        self.ventana.mainloop()

    def aceptar(self):
        if self.boton_continuar['state'] == 'disabled':
            self.boton_continuar.config(state = NORMAL)
        else:
            self.boton_continuar.config(state = 'disabled')

    def acceso(self):
        self.ventana.destroy()
        principal()

    def cancelar(self):
        seleccion = messagebox.askokcancel('Salir', 'Desea salir del sistema?')
        if seleccion == True:
            sys.exit()
