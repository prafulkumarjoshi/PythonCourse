import random

print("Welcome to the Word Guessing Game!")

string_art = ['''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
''','''
  +---+
  |   |
  O   |
 /|\\  |
 / \\   |
      |
=========
''']
placeholder=""
display=""

words_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(words_list)

placeholder = placeholder+ "_"*len(chosen_word)
print(placeholder)
placeholder_as_list=list(placeholder)
result = False

count = 0
while not result:
    guess_letter = input("Guess a letter?\n").lower()
    guess=False
    #replace chose letters instead of '_' in the placeholder
    for i in range(0,len(chosen_word)):
        if guess_letter == chosen_word[i]:
            guess = True
            placeholder_as_list[i]=guess_letter
    if not guess and count <6:
        print("***************************Count left: ", 6-(count+1))
        print(string_art[count])
        count +=1
    curr_word="".join(placeholder_as_list)
    print(curr_word)
    if curr_word==chosen_word:
        result = True
        print("You Win!")
    if count == 6:
        print("You Did not Win!")
        print("Correct word is: ", chosen_word)
        result=True
