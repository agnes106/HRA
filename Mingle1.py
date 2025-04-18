from tkinter import *
from PIL import Image, ImageTk   # pro nacteni obrazku na pozadi, PIL= python imaginary library--> museli jsme nainstalovat pillow 

class MingleHra:
    def __init__(self):
        self.okno = Tk()
        self.okno.title("Mingle")
        self.okno.geometry("676x380")
        self.okno.configure(bg="#f0f0f0")

        #tohle je pro nacteni obrazku
        self.obrazek = Image.open("minglepozadi.png")
        self.foto = ImageTk.PhotoImage(self.obrazek)
        #tohle je pro to pozadi
        self.pozadi = Label(self.okno, image=self.foto)         #Label = je to widget, který zobrazuje text či obrázek, image=self.foto = načtení obrázku PIL
        self.pozadi.place(x=0, y=0, relwidth=1, relheight=1)    # ty rel veci nam rikaji aby se obrazek rozprostrel pres cele okno

hra=MingleHra()
hra.okno.mainloop()