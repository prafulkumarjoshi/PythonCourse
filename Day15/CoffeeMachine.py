print("Welcome to the Coffee Machine!")
inventory={"Milk":500, "Coffee":300, "Water":1000, "Money":0}

ESPRESSO = {"Milk":200, "Coffee":24, "Water":200, "Money":15}
LATTE = {"Milk":150, "Coffee":12, "Water":100, "Money":25}
CAPPUCCINO = {"Milk":100, "Coffee":12, "Water":150, "Money":30}

def sum_of_coins(coins):
    return coins[0] + (2*coins[1]) + (5 * coins[2]) + (10 * coins[3])

# 5. If enough money is inserted return the change, print to inform user to enjoy coffee and update the inventory
def serve_order(choice,coins):
    print("Serving your order")
    sum_money = sum_of_coins(coins)
    if choice == "espresso":
        inventory["Milk"] -= ESPRESSO["Milk"]
        inventory["Coffee"] -= ESPRESSO["Coffee"]
        inventory["Water"] -= ESPRESSO["Water"]
        inventory["Money"] += ESPRESSO["Money"]
        if sum_money > ESPRESSO["Money"]:
            print("Your extra change: ", sum_money - ESPRESSO["Money"])
    elif choice == "latte":
        inventory["Milk"] -= LATTE["Milk"]
        inventory["Coffee"] -= LATTE["Milk"]
        inventory["Water"] -= LATTE["Milk"]
        inventory["Money"] += LATTE["Milk"]
        if sum_money > LATTE["Money"]:
            print("Your extra change: ", sum_money - LATTE["Money"])
    elif choice == "cappuccino":
        inventory["Milk"] -= CAPPUCCINO["Milk"]
        inventory["Coffee"] -= CAPPUCCINO["Coffee"]
        inventory["Water"] -= CAPPUCCINO["Water"]
        inventory["Money"] += CAPPUCCINO["Money"]
        if sum_money > CAPPUCCINO["Money"]:
            print("Your extra change: ", sum_money - CAPPUCCINO["Money"])
    print(f"Your {choice} is ready. Enjoy!")

# 3. Check if existing inventory is enough to fullfil the order, 
# if not print message of not enough resources
def check_inventory(choice):
    print("Checking inventory:")
    
    if choice == "espresso":
        return (inventory["Milk"] > ESPRESSO["Milk"]) and (inventory["Coffee"] > ESPRESSO["Coffee"]) and (inventory["Water"] > ESPRESSO["Water"])
    elif choice == "latte":
        return (inventory["Milk"] > LATTE["Milk"]) and (inventory["Coffee"] > LATTE["Coffee"]) and (inventory["Water"] > LATTE["Water"])
    elif choice == "cappuccino":
        return (inventory["Milk"] > CAPPUCCINO["Milk"]) and (inventory["Coffee"] > CAPPUCCINO["Coffee"]) and (inventory["Water"] > CAPPUCCINO["Water"])

# 4. If enough money not inserted, print message and return money
def check_money(choice, coins):
    #print("Checking money:", choice)
    sum_money = sum_of_coins(coins)
    if choice == "espresso" and sum_money < 15:
        return False
    elif choice == "latte" and sum_money < 25:
        return False
    elif choice == "cappuccino" and sum_money < 35:
        return False
    else:
        return True
turn_off = False
while not turn_off:
    # 1. What would you like? Espresso, Latte, Cappuccino or Inventory or Off to stop the program
    choice = input("What would you like? Espresso, Latte, Cappuccino or Inventory or Off to stop the program \n").lower()
    if choice == "report":
        print(inventory)
    elif choice == "off":
        print("Turning off the coffee machine")
        turn_off = True
    else:
        # 2. Please insert coins, 1 rupee, 2, 5 , 10

        is_inv_enough = check_inventory(choice)
        

        if not is_inv_enough:
            print("Inventory is not enough")
        else:
            print("Insert coins")
            ones = int(input("1s: "))
            twos = int(input("2s: "))
            fives = int(input("5s: "))
            tens = int(input("10s: "))
            coins=[ones, twos, fives, tens]
            is_money_enough = check_money(choice, coins)
            if not is_money_enough:
                print("Insert enough money")
                print("Your change: ", sum_of_coins(coins))
            elif is_inv_enough and is_money_enough:
                serve_order(choice,coins)
            
