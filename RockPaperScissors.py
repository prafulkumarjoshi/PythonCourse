import random as rd
computer_choice=rd.choice(["Rock","Paper", "Scissors"])
user_input = input("Do you want Rock Paper or Scissors?\n")
print("computer_choice is: "+computer_choice)
if computer_choice == user_input:
    print("TIE")
elif computer_choice=="Scissors" and user_input == "Rock":
    print("You win!")
elif computer_choice=="Rock" and user_input == "Paper":
    print("You win!")
elif computer_choice=="Paper" and user_input == "Scissors":
    print("You win!")
else:
    print("Computer wins!")

acronyms=["LOL", "BFF"]
word = "BFN"
if word in acronyms:
    print ("Yes")
else:
    print("No")
t=""
for w in acronyms:
    t+=w    
print(t)

#print(sum(acronyms))
sum=0
for i in range(7):
    e=int(input("Do you want Rock Paper or Scissors?\n"))
    sum+=e
print(sum)
