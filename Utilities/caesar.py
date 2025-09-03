import sys

def encrypt(message, key):
    cipher = ""
    for char in message:
        if char.isalpha():
            if char.isupper():
                caseBase = ord('A') #65
            elif char.islower():
                caseBase = ord('a') #97
            shiftedPosition = ((ord(char) - caseBase) + key) % 26
            shiftedChar = chr(shiftedPosition + caseBase)
            cipher += shiftedChar
        else:
            cipher += char
    return cipher

def decrypt(message, key):
    return encrypt(message, -key)

print("____ CAESAR CIPHER APP ____")
print("1: Encrypt\n2: Decrypt")
try:
    choice = int(input("Choice: [1 or 2]: "))
    while choice != 1 and choice != 2:
        choice = int(input("Please enter valid choice: [1 or 2]: "))

    if choice == 1:
        msg = input("Enter message to Encrypt: ")
        try:
            key = int(input("Enter Key: "))
            print(f"Encrypted message: {encrypt(msg, key)}")
        except ValueError:
            print("Key must be a number !")
    if choice == 2:
        msg = input("Enter message to Decrypt: ")
        try:
            key = int(input("Enter Key: "))
            print(f"Decrypted message: {decrypt(msg, key)}")
        except ValueError:
            print("Key must be a number !")    
except ValueError as e:
    print("Invalid Choice !!!")