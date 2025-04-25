alphabet= 'abcdefghijklmnopqrstuvwxyz'
def caesar(message, key, direction=1):
    encrypted = ''
    for ch in message.lower():
        if not ch.isalpha():
            encrypted+=ch
        else:
            encrypted+= alphabet[(alphabet.index(ch)+key*direction)%len(alphabet)]
    return encrypted
def encrypt(message,key):
    return caesar(message,key)
def decrypt(message,key):
    return caesar(message, key, -1)