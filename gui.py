import tkinter as tk
from figure import Main
from PIL import Image, ImageTk

class MiVentana(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.geometry("650x650")
        
        imagen = Image.open("imagen.png")
        
        imagen_tk = ImageTk.PhotoImage(imagen)
        
        fondo = tk.Label(self, image=imagen_tk)
        fondo.place(x=0, y=0, relwidth=1, relheight=1)
        
        fondo.image = imagen_tk

        self.boton = tk.Button(self, text="Abrir imagen", command=self.boton_clic)
        
        self.boton.pack(pady=20, padx=50)
        
    def boton_clic(self):
        main = Main()
        main.draw()

mi_ventana = MiVentana()

mi_ventana.mainloop()
