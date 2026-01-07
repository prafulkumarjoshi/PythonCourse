import random

logo = """
,adPPYba, ,adPPYYba, ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,
a8" "8a I8[ "" I8[ "" a8" "8a I8[ "" 88P' "Y8
88 88 `"Y8ba, `"Y8ba, 88 88 `"Y8ba, 88
88 88 aa ]8I aa ]8I 88 88 aa ]8I 88
"8a, ,d88 `"YbbdP"' `"YbbdP"' "8a, ,d88 `"YbbdP"' 88
`"8bbdP"Y8
"""

print(logo)

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def cipher(original_text, shift_amount, encode_or_decode):
    cipher_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for char in original_text:
        if char in alphabets:
            new_position = alphabets.index(char) + shift_amount
            new_position %= len(alphabets)
            cipher_text += alphabets[new_position]
        else:
            cipher_text += char
        
    print("Encoded: ",cipher_text )

to_proceed = "y"

while to_proceed=="y":
    direction = input("Type Encode to encrypt and Decode to decrypt\n").lower()
    text = input("Type the message?\n").lower()
    shift = int(input("Type the shift number?\n"))  
    cipher(original_text=text, shift_amount=shift, encode_or_decode=direction)
    to_proceed = input("Type Y to runt the program again or Type N to exit\n").lower()
    