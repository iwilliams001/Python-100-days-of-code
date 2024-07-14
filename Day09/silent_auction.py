import os
cls = lambda: os.system('cls')
#cls()
print("Welcome to the secret auction program")

tie = True

while tie == True:
    bidders = []
    another = "y"

    while another == "y":
        name = input("What is your name?: ")
        bid = float(input("What is your bid?: $"))
        another = input("Are there any other bidders? Type 'yes' or 'no'. ")[0].lower()
        cls()
        contestant = {}
        contestant["name"] = name
        contestant["bid"] = bid
        bidders.append(contestant)


    bids = []
    for x in range(len(bidders)):
        bid = bidders[x]["bid"]
        bids.append(bid)
        highest = max(bids)
    names = []
    for i in range(len(bids)):
        if bids[i] == highest:
            name = bidders[i]["name"]
            names.append(name)
    
    if len(names) == 1:
        name = names[0]
        print(f"The winner is {name} with a bid of ${highest}.")
        tie = False
    else:
        print(f"There is a tie bid of ${highest}. The following people should bid again.\n{names}")
        tie = True


