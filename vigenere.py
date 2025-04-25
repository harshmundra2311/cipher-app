def vigenere(text, key, direction = 1):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    key_index = 0
    final_message = ''
    for ch in text.lower():
        if not ch.isalpha():
            final_message+=ch
        else:
            key_char = key[key_index % len(key)]
            key_index+=1
            offset = alphabet.index(key_char)
            index = alphabet.index(ch)
            new_index = (index + offset*direction)%len(alphabet)
            final_message+=alphabet[new_index]
    return final_message

def encrypt(text, key):
    return vigenere(text,key)

def decrypt(text,key):
    return vigenere(text, key, -1)