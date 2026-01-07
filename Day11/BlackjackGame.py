import random

print("Welcome to the Blackjack game!")

cards=[1,2,3,4,5,6,7,8,9,10,11]

def calculate(cards):
    return sum(cards)

def check_winner(your_cards, computer_cards):
    your_score=calculate(your_cards)
    computer_score=calculate(computer_cards)
    print("Your final cards: ",your_cards,", final score:",your_score)
    print("Computer's final cards: ",computer_cards,", final score:",computer_score)
    if your_score <= 21:
        if your_score == computer_score:
            print("Draw!")
        elif your_score > computer_score:
            print("You win!")
        elif computer_score > 21:
            print("Computer score > 21. You win!")
        elif your_score < computer_score:
            print("Computer Wins!")
    elif your_score > 21:
        print("Your score greater than 21, Play again")
    else:
        "Play again"
        
play_again = "y"

while play_again == "y":
    your_cards=random.choices(cards,k=2)
    computer_cards=random.choices(cards,k=2)
    print("\n"*20)
    print("Your cards: ",your_cards,", current score:",calculate(your_cards)) 
    print("Computer's first card: ", computer_cards[0])
    while calculate(computer_cards) < 17:
        print("Computer total is less than 17, it will chose one more hand")
        computer_cards.append(random.choice(cards))
        
    sgo="y"
    while sgo=="y":
        sgo = input("Type y for another card or n to pass\n").lower()
        if sgo == "y":
            your_cards.append(random.choice(cards))
            print("Your cards: ",your_cards,", current score:",calculate(your_cards))
    check_winner(your_cards, computer_cards)
    play_again = input("Do you want to play again? Type y for Yes and n for No\n").lower()       
