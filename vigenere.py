def vigenere(text,key,direction=1):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    key_index=0
    char_index=0
    encrypted_text=""
    for char in text:
        flag=char.isupper()
        base_char=char.lower()
        if not char.isalpha():
            encrypted_text+=char
        else:
            key_char=key[key_index%len(key)]
            key_index+=1
            char_index=alphabet.find(base_char)
            offset=alphabet.find(key_char)
            new_index=char_index+offset*direction
            if flag:
                encrypted_text+=alphabet[new_index%len(alphabet)].upper()
            else:
                encrypted_text+=alphabet[new_index%len(alphabet)]
    return encrypted_text
def encrypt(text,key):
    return vigenere(text,key,1)
def decrypt(text,key):
    return vigenere(text,key,-1)