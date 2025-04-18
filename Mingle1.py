from tkinter import *
from PIL import Image, ImageTk   # pro nacteni obrazku na pozadi, PIL= python imaginary library--> museli jsme nainstalovat pillow 
import random                    # na generovani cisel

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

        self.tlacitko = Button(self.okno, text="Start", font=("Arial", 14), command=self.zobraz_cislo)
        self.tlacitko.place(relx=0.5, rely=0.8, anchor="center")                 # relx, rely = umístí tlačítko na 80 % výšky a doprostřed šířky okna (0.5 je střed) ---> basically umistuji tlacitko

        self.text = Label(self.okno, text="", font=("Arial", 30), bg="white")    # anchor = říká, že střed tlačítka bude umístěn do toho bodu
        self.text.place(relx=0.5, rely=0.4, anchor="center")
                                                              
    def zobraz_cislo(self):
        cislo = random.randint(100, 100000)  # náhodné číslo
        self.text.config(text=str(cislo))    # self.text.config(text=str(cislo)) = zmeni text label na dalsi nahodne cislo 
                                             # config = metoda, která mění funkce widgetu poté co už byl vytvořen (funguje i na barvy a tak)



hra=MingleHra()
hra.okno.mainloop()