# passcode = input("ENTER THE PASSCODE > ")
# if passcode == "mypass":
#     print("Flag: CTF220S{akskakdls}")

def alphabet_encryption(message:str):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    encryption = ""
    for character in message:
        a = alphabet
        encryption += a.replace(character.upper(),"")
    return encryption

myencryption = alphabet_encryption("hello")

for i in range(2):
    myencryption = alphabet_encryption(myencryption)

print(myencryption)

def find_missing_letter(s):
    full_alphabet = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    input_set = set(s)
    missing_letter = full_alphabet - input_set
    return missing_letter.pop() if missing_letter else None

def alphabet_decrypt(encrypted_message:str):
    len()
    