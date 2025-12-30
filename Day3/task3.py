print("Welcome to rollercoaster")

height = int(input("What is your height in cms?\n"))
bill = 0

if height > 120:
    print("You can ride a rollercoaster")
    age = int(input("What is your age?\n"))
    if age <5:
        print("Free ticket")
        bill=0
    elif age>=5 and age<12:
        print("5 Rs")
        bill=5
    elif age>=45 and age<=55:
        print("0 Rs")
        bill=0
    else:
        print("12 Rs")
        bill=12
    wants_photo = input("Do you want a photo? Type Y for Yes and N for No\n")
    
    if wants_photo == "Y":
        bill += 3
    print("Bill: ", bill)
else:
    print("You cannot ride a rollercoaster")

#num = int(input("Input a number:\n"))

#if num % 2 != 0:
#    print("Odd")
#else:
#    print("Even")

