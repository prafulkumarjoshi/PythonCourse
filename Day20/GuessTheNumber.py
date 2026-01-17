import random

print("Welcome to the Number Guessing Game!")

play_again = "y"

while play_again == "y":
    print("I am thinking of a number between 1 and 100!")
    computer_number = random.randint(1,100) 
    level = input("Chose a difficulty. Type 'easy' or 'hard': ").lower()
    attempts = 0
    if level == "easy":
        attempts = 10
    elif level == "hard":
        attempts = 5 
           
    guessed_correct = False
    
    while attempts > 0 and not guessed_correct:
        print(f"You have {attempts} attempts remaining to guess the number")
        guess = int(input("Make a guess: \n"))
        if guess < computer_number:
            print("Too low\nGuess again")
            attempts -= 1
        elif guess > computer_number:
            print("Too high\nGuess again")
            attempts -= 1
        elif guess == computer_number:
            print("You guessed correct!")
            guessed_correct = True
    if attempts == 0:
        print("You did not guess correct. The number was: ", computer_number)
    play_again = input("Do you want to guess again? Type Y or N: \n").lower()
