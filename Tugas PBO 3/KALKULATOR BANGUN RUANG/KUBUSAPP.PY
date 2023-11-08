import tkinter as tk
from tkinter import Frame,Label,Entry,Button,END, W

def hitung_luas():
    R = float(txtrusuk.get())

    L = round(6 *(R**2), 1)

    txtLuas.delete(0,END)
    txtLuas.insert(END,L)

def hitung_volume():
    R = float(txtrusuk.get())

    V = (round(R**3), 2)

    txtVolume.delete(0,END)
    txtVolume.insert(END,V)

def hitung():
    hitung_luas()
    hitung_volume()

# Create tkinter object
app = tk.Tk()

# Tambahkan judul
app.title("kalkulator luas dan volume Kubus")

app.geometry("450x450")

# Windows
frame = Frame(app)
frame.pack(padx=20, pady=20)

# Label Rusuk
rusuk= Label(frame, text="rusuk:")
rusuk.grid(row=0, column=0, sticky=W, padx=5, pady=5)

# Textbox Rusuk
txtrusuk = Entry(frame)
txtrusuk.grid(row=0, column=1)

# Button
hitung_button = Button(frame, text="Hitung", command=hitung)
hitung_button.grid(row=2, column=1, sticky=W, padx=5, pady=5)

# Label Volume
volume= Label(frame, text="volume:")
volume.grid(row=3, column=1, sticky=W, padx=5, pady=5)

# Output Label Luas
luas = Label(frame, text="Luas: ")
luas.grid(row=3, column=0, sticky=W, padx=5, pady=5)

# Output Label Volume
volume = Label(frame, text="volume: ")
volume.grid(row=4, column=0, sticky=W, padx=5, pady=5)

# Output Textbox Luas
txtLuas = Entry(frame)
txtLuas.grid(row=3, column=1, sticky=W, padx=5, pady=5)

# Output Textbox Volume
txtVolume = Entry(frame)
txtVolume.grid(row=4, column=1, sticky=W, padx=5, pady=5)

app.mainloop()



