def caesar(text,offset,direction=1):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    char_index=0
    encrypted_text=""
    for char in text:
        flag=char.isupper()
        base_char=char.lower()
        if not char.isalpha():
            encrypted_text+=char
        else:
            char_index=alphabet.find(base_char)
            new_index=char_index+offset*direction
            if flag:
                encrypted_text+=alphabet[new_index%len(alphabet)].upper()
            else:
                encrypted_text+=alphabet[new_index%len(alphabet)]
    return encrypted_text
def encrypt(text,offset):
    return caesar(text,offset,1)
def decrypt(text,offset):
    return caesar(text,offset,-1)

