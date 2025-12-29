import random

rock = '''
                                  88         
                                  88         
                                  88         
8b,dPPYba,  ,adPPYba,   ,adPPYba, 88   ,d8   
88P'   "Y8 a8"     "8a a8"     "" 88 ,a8"    
88         8b       d8 8b         8888[      
88         "8a,   ,a8" "8a,   ,aa 88`"Yba,   
88          `"YbbdP"'   `"Ybbd8"' 88   `Y8a  
'''

papers = '''
 _ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_| 
'''

scissors='''
   _       ,/'
  (_).  ,/'
   _  ::
  (_)'  `\.
           `\.
'''
print("Welcome to the Rock Paper Scissors Game!")

list_r_p_s = ["Rock", "Paper", "Scissors"]
user_choice = int(input("Rock (0), Paper (1) or Scissors(2)?\n"))


comp_choice = random.randint(0,2)

print("Your choice: ",list_r_p_s[user_choice] )

print("Computer choice: ",list_r_p_s[comp_choice])

if user_choice == 0:
    if comp_choice == "0":
        print ("Draw, play again!")
    elif comp_choice == "1":
        print ("Computer Wins!")
    else:
        print ("You Win!")

elif user_choice == 1:
    if comp_choice == "0":
        print ("You Win!")
    elif comp_choice == "1":
        print ("Draw, play again!")
    else:
        print ("Computer Wins!")
        
elif user_choice == 2:
    if comp_choice == "0":
        print ("Computer Wins!")
    elif comp_choice == "1":
        print ("You Win!")
    else:
        print ("Draw, play again!")