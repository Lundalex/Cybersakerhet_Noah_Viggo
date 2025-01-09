import random
import string
import threading
import os

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

def remove_the_file():
    if os.path.exists("message.txt") and remove_the_file.shouldDelete:
        os.remove("message.txt")  # Remove the file if it exists
        print("You weren't fast enough!")
        quit()
    else:
        remove_the_file.shouldDelete=True
    threading.Timer(180, remove_the_file).start() # update every 3 minutes

remove_the_file.shouldDelete = False

def update_the_passcode():
    global passcode
    passcode = generate_passcode()
    encrypted_message = alphabet_encryption(passcode)

    for _ in range(2):
        encrypted_message = alphabet_encryption(encrypted_message)
    with open("message.txt", "w") as encrypted:
        encrypted.write(encrypted_message)

update_the_passcode()

file_removal = threading.Thread(target=remove_the_file)
file_removal.daemon = True  # Quit with main thread
file_removal.start()

print(r"""
 ________  ___       ________  ___  ___  ________  ___  ___  _________  ___  ___     
|\   __  \|\  \     |\   __  \|\  \|\  \|\   __  \|\  \|\  \|\___   ___\\  \|\  \    
\ \  \|\  \ \  \    \ \  \|\  \ \  \\\  \ \  \|\  \ \  \\\  \|___ \  \_\ \  \\\  \   
 \ \   __  \ \  \    \ \   ____\ \   __  \ \   __  \ \  \\\  \   \ \  \ \ \   __  \  
  \ \  \ \  \ \  \____\ \  \___|\ \  \ \  \ \  \ \  \ \  \\\  \   \ \  \ \ \  \ \  \ 
   \ \__\ \__\ \_______\ \__\    \ \__\ \__\ \__\ \__\ \_______\   \ \__\ \ \__\ \__\
    \|__|\|__|\|_______|\|__|     \|__|\|__|\|__|\|__|\|_______|    \|__|  \|__|\|__|
""")

def main():
    guess = None
    while guess != passcode:

        guess = input("ENTER THE PASSCODE > ")

        if guess == passcode:
            print("That's correct!")
            print("Flag: CTF220S{AlPh4b3t1c4l_aUth3nT1C4t1oN_N04h--oC4--V1gg0}")
            quit()
        else:
            print("INCORRECT!")

main()