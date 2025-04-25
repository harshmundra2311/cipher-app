import tkinter as tk
from tkinter import messagebox
def open_caesar():
    root.destroy()
    import caesar_gui
def open_vigenere():
    root.destroy()
    import vigenere_gui

root = tk.Tk()
root.title("Cipher App")
root.geometry("400x400")
label = tk.Label(root, text="Choose Cipher",font=('Helvetica',16))
label.pack(pady=20)

button_frame = tk.Frame(root)
button_frame.pack()
caesar_button = tk.Button(root, text="Caesar Cipher", width=20, command=open_caesar)
caesar_button.pack(side='left', padx=10)
vigenere_button = tk.Button(root, text="Vigenere Cipher", width=20, command=open_vigenere)
vigenere_button.pack(side='left', padx=10)

root.mainloop()