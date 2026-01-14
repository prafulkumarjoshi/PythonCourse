import random

persons =[{"Name":"A", "value":11}, {"Name":"B", "value":441},{"Name":"C", "value":2},{"Name":"D", "value":121}]
correct_guess = True
score = 0

def check_answer(guess, count1, count2):
    '''Takes user's guess, A and B followers count and returns the result'''
    if count1 > count2:
        return guess == "a"
    else:
        return guess == "b"
    
while correct_guess:
    print("Welcome to the Game Higher or Lower !")

    person_A_B = random.sample(persons,2)

    print("Compare A: " , person_A_B[0]["Name"])
    print("Vs")
    print("Compare B: " , person_A_B[1]["Name"])

    guess = input("Guess who has more followers? Type 'A' or 'B'\n").lower()
    
    correct_guess = check_answer(guess, person_A_B[0]["value"], person_A_B[1]["value"])
    
    if correct_guess:
        score += 1
        print("Correct!")
    else:
        print("Wrong!")    

print("Your score: ", score)    
