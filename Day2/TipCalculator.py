print("Welcome to the Tip Calculator!")

total_bill = int(input("What was the total bill?\n"))

tip_amount = int(input("How much tip would you like to give? 10, 12 or 15?\n"))

num_people = int(input("how man people to split the bill?\n"))
each_person_share = (total_bill + (total_bill*(tip_amount/100)))/num_people
print(f"Each person should pay: {each_person_share}")


