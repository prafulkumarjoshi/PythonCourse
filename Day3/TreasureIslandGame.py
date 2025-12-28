

print('''
.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
.            _.,.__       .                                   .
.           ((o\\o\))     .                                   .
.     .-.    `  \\``      .    A tropical island              .
.  __(   )___.o"^^".,___  .                                   .
.     ===    ~~~~~~~~     .                                   .
.      ==             ldb .                                   .
.       =                 .                                   .
.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.
''')
print("Welcome to the Treasure Island!")
print("your mission is to find treasure island!")


left_or_right = input("Do you want to go left or right?\n") #S 15 M 20 L 25

if left_or_right.lower() == "left":
    wait_or_swim = input("Do you ant to wait or swim?\n")
    if wait_or_swim.lower() == "wait":
        colour = input("Which colour? Red, Blue or Yellow\n")
        if colour.lower() == "red":
            print("Fire! Game Over!")
        elif colour.lower() == "blue":
            print("Beasts! Game Over!")
        elif colour.lower() == "yellow":
            print("You win!")
        else:
            print("Game Over!")
    else:
        print("Trouts! Game Over!") 
else:
    print("Fall into a hole.Game Over!")
