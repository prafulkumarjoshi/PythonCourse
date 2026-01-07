logo = """
,adPPYba, ,adPPYYba, ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,
a8" "8a I8[ "" I8[ "" a8" "8a I8[ "" 88P' "Y8
88 88 `"Y8ba, `"Y8ba, 88 88 `"Y8ba, 88
88 88 aa ]8I aa ]8I 88 88 aa ]8I 88
"8a, ,d88 `"YbbdP"' `"YbbdP"' "8a, ,d88 `"YbbdP"' 88
`"8bbdP"Y8
"""

print(logo)
print("Welcome to the secret bid program!")

bids={}
go = "y"
while go == "y":
    print("\n"*100)
    name = input("What's your name?\n").lower()
    bid_amount = int(input("What's your bid amount?\n"))
    bids[name]=bid_amount
    go = input("Type Y to run the program again or Type N to exit\n").lower()
    
def find_highest_bid(bids):
    max = 0
    winner=""
    for item in bids:
        if bids[item] > max:
            max = bids[item]
            winner = item
    print("Highest Bid: ",winner, bids[winner] )
    
find_highest_bid(bids)
