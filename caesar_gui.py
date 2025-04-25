import caesar as cc
import tkinter as tk
result_text=""
def encrypt_text():
    global result_text
    text = entry_text.get()
    key = int(entry_key.get())
    result_text = cc.encrypt(text,key)
    result_label.config(text="Encrypted Text: "+result_text)
def decrypt_text():
    global result_text
    text = entry_text.get()
    key = int(entry_key.get())
    result_text = cc.decrypt(text,key)
    result_label.config(text="Decrypted Text: "+result_text)
def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(result_text)
    root.update()
    result_label.config(text="Copied!!!")
    root.after(1500, lambda: result_label.config(text="Result: "+result_text))
root = tk.Tk()
root.title("Caesar Cipher")
root.geometry("400x400")
label1 = tk.Label(root, text="Enter text: ")
label1.pack(pady=5)
entry_text = tk.Entry(root, width=40)
entry_text.pack()
label2 = tk.Label(root, text="Enter key: ")
label2.pack()
entry_key = tk.Entry(root, width=10)
entry_key.pack()
button_frame = tk.Frame(root)
button_frame.pack()
encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_text)
encrypt_button.pack(side="left",padx=10)
decrypt_button = tk.Button(root, text="Decrypt", command=decrypt_text)
decrypt_button.pack(side="left",padx=10)
copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(side="left",padx=10)
result_label = tk.Label(root, text="")
result_label.pack()
root.mainloop()