
from tkinter import *
from PIL import Image, ImageTk   # pro nacteni obrazku na pozadi, pillow
import random                    # na generovani cisel

class MingleHra:
    def __init__(self):
        self.okno = Tk()
        self.okno.title("Mingle")
        self.okno.geometry("676x380")
        self.okno.configure(bg="#f0f0f0")

         # tohle je pro nacteni obrazku pozadi
        self.obrazek = Image.open("minglepozadi.png")
        self.foto = ImageTk.PhotoImage(self.obrazek)
        # tohle je pro to pozadi
        self.pozadi = Label(self.okno, image=self.foto)         # Label = widget zobrazujici obrazek
        self.pozadi.place(x=0, y=0, relwidth=1, relheight=1)    # rel veci jsou na umístění do okna jejich poloha

        # Panáček - načtení a zobrazení
        self.panacek_img = Image.open("vojaksq.png")  # cesta k panáčkovi
        self.panacek_img = self.panacek_img.resize((100, 200))  # uprava velikosti
        self.panacek_photo = ImageTk.PhotoImage(self.panacek_img)
        self.panacek_label = Label(self.okno, image=self.panacek_photo, bg="#f0f0f0")
        self.panacek_label.place(x=10, y=200)  # umisteni do leva dolu

        # Text panáčka
        self.text_info = Label(self.okno, text="Vítejte ve hře Mingle! Zapamatujte si číslo, které se objeví na obrazovce.",
                               font=("Arial", 14), bg="#f0f0f0", wraplength=400, justify="center")
        self.text_info.place(relx=0.5, rely=0.4, anchor="center")

        # Tlačítko "Rozumím"
        self.tlacitko_rozumim = Button(self.okno, text="Jsem připraven!", font=("Arial", 14), command=self.zacni_hru)
        self.tlacitko_rozumim.place(relx=0.5, rely=0.6, anchor="center")

        # Label pro číslo, bude skryt až do startu
        self.text_cislo = Label(self.okno, text="", font=("Arial", 30), bg="white")
        self.text_cislo.place(relx=0.5, rely=0.2, anchor="center")

        # Životy
        self.zivoty = 3  # pocet zivotu
        self.label_zivoty = Label(self.okno, text="Životy:3", font=("Arial", 14), bg="white")
        self.label_zivoty.place(relx=0.05, rely=0.05)

        # Nastaveni casovace
        self.zpozdeni = 6000  # ms, jak dlouho je cislo videt
        self.casovac = None    # uchovava id timeoutu
        self.odpocet = None    # uchovava odpočet sek

        # Odpovedni tlacitka (zatim disabled)
        self.tlacitko1 = Button(self.okno, text="", font=("Arial", 12), command=lambda: self.zkontroluj_odpoved(0), state="disabled")
        self.tlacitko2 = Button(self.okno, text="", font=("Arial", 12), command=lambda: self.zkontroluj_odpoved(1), state="disabled")
        self.tlacitko3 = Button(self.okno, text="", font=("Arial", 12), command=lambda: self.zkontroluj_odpoved(2), state="disabled")
        self.tlacitko4 = Button(self.okno, text="", font=("Arial", 12), command=lambda: self.zkontroluj_odpoved(3), state="disabled")
        # lambda = malá funkce, která nám pomáhá vytvorit funkci bez def 
        # Po kliknutí na tlačítko se zavolá metoda zkontroluj_odpoved(0)
        # Číslo v závorce určuje, které tlačítko bylo zmáčknuto (0 = první tlačítko, 1 = druhé, atd.)

        # umisteni tlacitek
        self.tlacitko1.place(relx=0.2, rely=0.7, anchor="center")
        self.tlacitko2.place(relx=0.4, rely=0.7, anchor="center")
        self.tlacitko3.place(relx=0.6, rely=0.7, anchor="center")
        self.tlacitko4.place(relx=0.8, rely=0.7, anchor="center")

        self.spravne_cislo = None  # promenna pro spravne cislo

    def zacni_hru(self):
        # skryti uvodni bubliny a tlacitka
        self.text_info.place_forget()
        self.tlacitko_rozumim.place_forget()
        # aktivace tlacitek
        for b in (self.tlacitko1, self.tlacitko2, self.tlacitko3, self.tlacitko4):
            b.config(state="normal")
        # start hry
        self.zobraz_cislo()

    def zobraz_cislo(self):
        # generovani a zobrazeni cisla
        self.spravne_cislo = random.randint(100, 100000) # self.text.config(text=str(cislo)) = zmeni text label na dalsi nahodne cislo 
                                                          # config = metoda, která mění funkce widgetu poté co už byl vytvořen (funguje i na barvy a tak)
        self.text_cislo.config(text=str(self.spravne_cislo))
        # priprava moznosti
        moznosti = [self.spravne_cislo]
        while len(moznosti) < 4:
            n = random.randint(100, 100000)
            if n not in moznosti:
                moznosti.append(n)
        random.shuffle(moznosti)  # shuffle - nahodne vybrani ...
        # nastaveni tlacitek
        self.tlacitko1.config(text=str(moznosti[0]))
        self.tlacitko2.config(text=str(moznosti[1]))
        self.tlacitko3.config(text=str(moznosti[2]))
        self.tlacitko4.config(text=str(moznosti[3]))
        # odpocet a casovac
        self.odpocet = self.zpozdeni // 1000  #Dělením // 1000 získáme celé sekundy (6 000 // 1 000 = 6). #příprava proměnné self odpočet
        self.update_odpocet()          # zacni odpocet sekund  # ---> metoda, která jednou za sekundu sníží self.odpocet o 1 a přepíše číslo v labelu.
        if self.casovac:               # zrus stary casovac
            self.okno.after_cancel(self.casovac)
        self.casovac = self.okno.after(self.zpozdeni, lambda: self.konec_hry("Čas vypršel!"))  # nějak se v okně nezobrazuje zjistit proč

    def update_odpocet(self): 
        # zobrazeni odpocet sekund
        self.label_zivoty.config(text=f"Životy:{self.zivoty}  Čas:{self.odpocet}s")
        if self.odpocet > 0:
            self.odpocet -= 1
            self.okno.after(1000, self.update_odpocet)

    def zkontroluj_odpoved(self, index):
        # kontrola odpovedi
        vybrane = int([self.tlacitko1["text"], self.tlacitko2["text"],
                       self.tlacitko3["text"], self.tlacitko4["text"]][index])
        # zrus casovac
        if self.casovac:
            self.okno.after_cancel(self.casovac)
        if vybrane == self.spravne_cislo:
            self.zobraz_cislo()
        else:
            self.zivoty -= 1
            if self.zivoty <= 0:
                self.konec_hry("Špatně! Hra končí.") # taky nezobrazuje zjistit proč ig 
            else:
                self.zobraz_cislo()

    def konec_hry(self, zprava):
        # konec hry, deaktivace tlacitek a zobrazeni zpravy
        self.text_cislo.config(text="")  # vymazání čísla z obrazovky 
        self.text_info.config(text=zprava)
        for b in (self.tlacitko1, self.tlacitko2, self.tlacitko3, self.tlacitko4): # cyklus prochází každou odpověď tlačítek
            b.config(state="disabled") #U každého z těchto tlačítek voláme metodu config, která nastaví state="disabled" → tlačítko je šedivé a nedá se na něj kliknout.
        # Tlacitko restart hry
        self.restart_btn = Button(self.okno, text="Hrát znovu", font=("Arial", 14), command=self.restartuj)
        self.restart_btn.place(relx=0.5, rely=0.8, anchor="center")

    def restartuj(self):  # NOVÉ
        # odstraneni restart tlacitka
        self.restart_btn.destroy()  #tlačítko „Hrát znovu“, které se objevilo po skončení hry.
        # obnoveni zivota       # destroy ---> úplné odstraběbí z okna
        self.zivoty = 3
        self.text_info.place_forget()  #self.text_info je label s mluvící bublinou panáčka (nebo úvodní text).

                    #Metoda place_forget() ho skryje (nezruší úplně, ale stáhne ho z viditelné plochy), aby byl čistý štít pro novou hru.
        # spustit novou hru
        self.zacni_hru()

# spust hru
hra = MingleHra()
hra.okno.mainloop()