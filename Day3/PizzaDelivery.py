print("Welcome to Pizza Delivery")

size = input("What size pizza do you want? S, M or L\n") #S 15 M 20 L 25

veggies = input("Do you want extra veggies? Type Y for Yes and N for No\n") #2 for S and 3 for M/L

cheese = input("Do you want extra cheese? Type Y for Yes and N for No\n") #1

bill = 0

if size=="S":
    bill += 15
elif size=="M":
    bill += 20
else:
    bill += 25

if veggies=="Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
        

if cheese=="Y":
    bill += 1


print("Bill:" , bill)
