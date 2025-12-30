import random

print("Welcome to the Password Generator!")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols = ['!','#','$','%','&','*','(',')','+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

input_letters = int(input("How many letters do you want?\n"))
input_symbols = int(input("How many symbols do you want?\n"))
input_numbers = int(input("How many numbers do you want?\n"))

password_list = []
for c in range(0,input_letters):
    password_list.append(random.choice(letters))

for s in range(0,input_symbols):
    password_list.append(random.choice(symbols))

for n in range(0,input_numbers):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char
    
print(password)
