# Cipher App

A Python GUI-based application for encrypting and decrypting text using Caesar and Vigenère ciphers.

## Features
- Supports Caesar and Vigenère ciphers
- Encrypt and decrypt messages
- Copy output to clipboard
- Simple GUI using Tkinter
- Select which cipher you want to use from the main window

## Files
- `caesar.py` – Caesar cipher logic
- `vigenere.py` – Vigenère cipher logic
- `caesar_gui.py` – GUI for Caesar cipher
- `vigenere_gui.py` – GUI for Vigenère cipher
- `main_gui.py` – Starting point: lets you choose which cipher to use

## Future Features (Planned)
- QR code generation for encrypted messages
- Brute-force Caesar decryption
- Save/load encrypted messages
- Dark mode GUI

## How to Run
```bash
python main_gui.py