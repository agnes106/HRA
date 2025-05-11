
from tkinter import *
from PIL import Image, ImageTk   # pro nacteni obrazku na pozadi, PIL= python imaginary library--> museli jsme nainstalovat pillow 
import random                    # na generovani cisel

class MingleHra:
    def __init__(self):
        self.okno = Tk()
        self.okno.title("Mingle")
        self.okno.geometry("676x380")
        self.okno.configure(bg="#f0f0f0")

        # tohle je pro nacteni obrazku
        self.obrazek = Image.open("minglepozadi.png")
        self.foto = ImageTk.PhotoImage(self.obrazek)
        # tohle je pro to pozadi
        self.pozadi = Label(self.okno, image=self.foto)         #Label = je to widget, který zobrazuje text či obrázek, image=self.foto = načtení obrázku PIL
        self.pozadi.place(x=0, y=0, relwidth=1, relheight=1)    # ty rel veci nam rikaji aby se obrazek rozprostrel pres cele okno
        # tvoření tlačítka
        self.tlacitko = Button(self.okno, text="Start", font=("Arial", 14), command=self.zobraz_cislo)
        self.tlacitko.place(relx=0.5, rely=0.8, anchor="center")                 # relx, rely = umístí tlačítko na 80 % výšky a doprostřed šířky okna (0.5 je střed) ---> basically umistuji tlacitko

        self.text = Label(self.okno, text="", font=("Arial", 30), bg="white")    # anchor = říká, že střed tlačítka bude umístěn do toho bodu
        self.text.place(relx=0.5, rely=0.4, anchor="center")
        # tvoření tlačítek pro životy                                                      
        self.zivoty = 3  
        self.label_zivoty = Label(self.okno, text="Životy:3", font=("Arial", 14), bg="white")
        self.label_zivoty.place(relx=0.05, rely=0.05)
        # nastavení časovače
        self.zpozdeni = 6000  # čas v milisekundách (2 sekundy)
        self.cas_vyprsel = False
        self.casovac = None  # proměnná pro časovač

        # Panáček - načítání obrázku
        self.panacek_img = Image.open("squidgamevojak.png")  # cesta k panáčkovi
        self.panacek_img = self.panacek_img.resize((100, 200))  # úprava velikosti, dle potřeby
        self.panacek_photo = ImageTk.PhotoImage(self.panacek_img)
        self.panacek_label = Label(self.okno, image=self.panacek_photo, bg="#f0f0f0")
        self.panacek_label.place(x=10, y=200)  # umístění do levého dolního rohu

        # Text pro úvodní výzvu od panáčka
        self.text = Label(self.okno, text="Vítejte ve hře! Zapamatujte si číslo, které se objeví na obrazovce.", 
                          font=("Arial", 14), bg="#f0f0f0", wraplength=400, justify="center")
        self.text.place(relx=0.5, rely=0.4, anchor="center")

        # Tlačítko pro pokračování
        self.tlacitko_rozumim = Button(self.okno, text="Rozumím", font=("Arial", 14), command=self.zacni_hru)
        self.tlacitko_rozumim.place(relx=0.5, rely=0.6, anchor="center")

        # tlačítka na vyber odpovědi, ted jsou jeste prazdna
        self.tlacitko1 = Button(self.okno, text="", font=("Arial", 12), command=lambda: self.zkontroluj_odpoved(0))
        self.tlacitko2 = Button(self.okno, text="", font=("Arial", 12), command=lambda: self.zkontroluj_odpoved(1))
        self.tlacitko3 = Button(self.okno, text="", font=("Arial", 12), command=lambda: self.zkontroluj_odpoved(2))
        self.tlacitko4 = Button(self.okno, text="", font=("Arial", 12), command=lambda: self.zkontroluj_odpoved(3))
        # lambda = malá funkce, která nám pomáhá vytvorit funkci bez def 
        # Po kliknutí na tlačítko se zavolá metoda zkontroluj_odpoved(0)
        # Číslo v závorce určuje, které tlačítko bylo zmáčknuto (0 = první tlačítko, 1 = druhé, atd.)

        # umístění tlačítek v obraze
        self.tlacitko1.place(relx=0.2, rely=0.6, anchor="center")
        self.tlacitko2.place(relx=0.4, rely=0.6, anchor="center")
        self.tlacitko3.place(relx=0.6, rely=0.6, anchor="center")
        self.tlacitko4.place(relx=0.8, rely=0.6, anchor="center")
        # proměnná, none= je zatim prázdná  (předpřipravení proměnné)
        self.spravne_cislo = None

    def zacni_hru(self):
        self.text.config(text="Začínáme hru! Zapamatujte si číslo.")  # Změní text na úvodní text pro hru
        self.tlacitko_rozumim.place_forget()  # Skrýt tlačítko "Rozumím" po jeho stisknutí
        self.zobraz_cislo()  # Zavolá metodu pro zobrazení čísla


    def zobraz_cislo(self):
        self.spravne_cislo = random.randint(100, 100000)  # self.text.config(text=str(cislo)) = zmeni text label na dalsi nahodne cislo 
                                                          # config = metoda, která mění funkce widgetu poté co už byl vytvořen (funguje i na barvy a tak)
        self.text.config(text=str(self.spravne_cislo))

        # vygenerujeme náhodné odpovědi včetně správné
        moznosti = [self.spravne_cislo]
        while len(moznosti) < 4:
            nahodne = random.randint(100, 100000)
            if nahodne not in moznosti:       # kontroluje, že tam náhodné číslo ještě není
                moznosti.append(nahodne)
        random.shuffle(moznosti)   # náhodné zamíchání prvků = shuffle

        # nastavíme texty tlačítek
        self.tlacitko1.config(text=str(moznosti[0]))
        self.tlacitko2.config(text=str(moznosti[1]))
        self.tlacitko3.config(text=str(moznosti[2]))
        self.tlacitko4.config(text=str(moznosti[3]))

        # startujeme časovač
        self.cas_vyprsel = False
        self.spusti_casovac()

    def spusti_casovac(self):
        if self.casovac:  # Pokud už časovač běží, zrušíme předchozí
            self.okno.after_cancel(self.casovac)

        # Nastaví časovač, který po uplynutí doby zavolá funkci pro konec hry
        self.casovac = self.okno.after(self.zpozdeni, self.konec_hry, "BANG")

    def zkontroluj_odpoved(self, index):   # funkce dostává jako úvodní info index (0-3)       index pak také vybere ten na, který hráč klikl
        vybrane = int([self.tlacitko1["text"], self.tlacitko2["text"],
                       self.tlacitko3["text"], self.tlacitko4["text"]][index])
        
        if vybrane == self.spravne_cislo:
            self.zobraz_cislo()  # správná odpověď, zobrazí nové číslo
            if not self.cas_vyprsel:  # Pokud čas nevypršel, restartujeme časovač
                self.spusti_casovac()
        else:
            self.zivoty -= 1
            self.label_zivoty.config(text=f"Životy: {self.zivoty}")
            if self.zivoty <= 0:
                self.konec_hry("BANG!")
            elif not self.cas_vyprsel:  # Pokud čas nevypršel, restartujeme časovač
                self.spusti_casovac()

    def konec_hry(self, zprava):
        self.text.config(text=zprava)
        self.tlacitko1.config(state="disabled")  #NAPSAT SEM DOVYSVETLENÍ!
        self.tlacitko2.config(state="disabled")
        self.tlacitko3.config(state="disabled")
        self.tlacitko4.config(state="disabled")
        self.tlacitko.config(state="disabled")

hra = MingleHra()
hra.okno.mainloop()