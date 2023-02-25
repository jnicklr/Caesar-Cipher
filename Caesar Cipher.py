alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

def caesar_cipher (string, number, result):
    cipher_text = []
    n = 0
    for letter in string:
        cipher_text.append(letter)
    for i in range (0, len(string)):
        for letter in alphabet:
            if cipher_text[i] == ' ':
                continue
            elif letter == cipher_text[i]:
                if result == 'decode':
                    cipher_text[i] = alphabet[n-shift]
                    n = 0
                    break
                else:
                    cipher_text[i] = alphabet[n+shift]
                    n = 0
                    break
            else:
                n += 1
    new_string = ''.join(cipher_text)
    if result == 'decode':
        print(f"Here\'s the decoded result: {new_string}")
    else:
        print(f"Here\'s the encoded result: {new_string}")

op = ''
print(logo)
while True:
    if op == 'no':
        break
    else:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
        text = input("Type your message: ")
        shift = int(input("Type the shift number: "))
        if direction == 'encode' or direction == 'decode':
            caesar_cipher(string = text, number = shift, result = direction)
            op = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
        else:
            print("The type selected is invalid.")
            break