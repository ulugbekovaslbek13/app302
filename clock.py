# Fayl nomi: clock.py
from tkinter import *
from time import strftime

# Oynani yaratish
root = Tk()
root.title("Aslbek | Digital Clock")

# Soat ko'rinishini sozlash
def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

# Dizayn qismi
label = Label(root, font=("ds-digital", 80), background="black", foreground="cyan")
label.pack(anchor='center')

# Soatni ishga tushirish
time()

print("Soat oynasi ochildi! Uni yopish uchun oynani o'zini yoping.")
root.mainloop()