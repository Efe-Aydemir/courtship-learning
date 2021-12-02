import tkinter as tk
from tkinter import font
import requests
import json
import datetime
from tkinter import messagebox


def göster():
    messagebox.showinfo("!--Kurlar--!","Dolar Alış: "+dolar_alis+"\nEuro Alış: "+euro_alis+"\n\n\nDolar Satış: "+dolar_satis+"\nEuro Satış: "+euro_satis)

api_url = requests.get("https://api.genelpara.com/embed/doviz.json")


yazi = api_url.text
veri = json.loads(yazi)


dolar = veri["USD"]
dolar_alis = dolar["alis"]
dolar_satis = dolar["satis"]


euro = veri["EUR"]
euro_alis = euro["alis"]
euro_satis = euro["satis"]



pencere = tk.Tk()
pencere.title("Kur")
pencere.geometry("300x100")
pencere.resizable(width=False,height=False)
pencere.configure(bg="cornflowerblue")


baslık = tk.Label(text="Kur App"
,fg="red",
bg="cornflowerblue",
font="cursive 25",)
baslık.pack()

btn = tk.Button(text="Popüler Kurları Göster",
bg="aqua",
fg="red",
font="cursive",
activebackground="red",
activeforeground="yellow",
command=göster).pack()

pencere.mainloop()