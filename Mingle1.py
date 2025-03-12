#hra pocatek
import tkinter as tk

# Vytvoření hlavního okna
root = tk.Tk()
root.title("Moje první GUI")

# Přidání tlačítka
button = tk.Button(root, text="Klikni mě!", command=lambda: print("Tlačítko stisknuto!"))
button.pack(pady=20)

# Spuštění aplikace
root.mainloop()