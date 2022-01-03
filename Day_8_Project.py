import os


def clear():
    os.system("cls")


letters = {}

for i in range(26):
    letters[i] = str(chr(97 + i))

print(letters)


def encryption(text, key):
    cipher = ""
    for c in text:
        for k in letters:
            if letters[k] == c:
                cipher += letters[(k + key) % 26]
    return cipher


def decryption(cipher, key):
    text = ""
    for c in cipher:
        for k in letters:
            if letters[k] == c:
                text += letters[(k - 26 - key) % 26]
    return text


text = input("Enter Text \n")
key = int(input("Enter Key \n"))

cipher = encryption(text, key)

print(f"Cipher text : {cipher}")
text = decryption(cipher, key)
print(f"Plain Text : {text}")
