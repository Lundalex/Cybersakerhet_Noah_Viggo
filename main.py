import random
import string
import threading

def alphabet_encryption(message:str):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    encryption = ""
    for character in message:
        a = alphabet
        encryption += a.replace(character.upper(),"")
    return encryption

def generate_passcode(length=30): # Generate 30 random uppercase letters
    passcode = ""
    for _ in range(length):
        passcode += random.choice(string.ascii_uppercase)
    return passcode

def update_the_passcode():
    global passcode
    passcode = generate_passcode()
    encrypted_message = alphabet_encryption(passcode)

    for _ in range(2):
        encrypted_message = alphabet_encryption(encrypted_message)
    with open("message.txt", "w") as encrypted:
        encrypted.write(encrypted_message)

    threading.Timer(180, update_the_passcode).start() # update every 3 minutes

passcode_update = threading.Thread(target=update_the_passcode)
passcode_update.daemon = True  # Quit with main thread
passcode_update.start()

def main():
    guess = None
    while guess != passcode:
        print("ALPHA83T D3CRYPT10N")

        guess = input("ENTER THE PASSCODE > ")

        if guess == passcode:
            print("That's correct!")
            print("Flag: CTF220S{akskakdls}")
            quit()
        else:
            print("INCORRECT!")

main()