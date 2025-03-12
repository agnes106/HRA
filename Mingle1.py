import tkinter as tk

# Vytvoření hlavního okna
root = tk.Tk()
root.title("Srdíčko")

# Vytvoření plátna
canvas = tk.Canvas(root, width=300, height=300, bg="white")
canvas.pack()

# Nakreslení srdce pomocí dvou kruhů a trojúhelníku
canvas.create_oval(50, 50, 150, 150, fill="red", outline="red")  # Levý kruh
canvas.create_oval(150, 50, 250, 150, fill="red", outline="red")  # Pravý kruh
canvas.create_polygon(50, 100, 250, 100, 150, 250, fill="red", outline="red")  # Spodní část

# Spuštění aplikace
root.mainloop()