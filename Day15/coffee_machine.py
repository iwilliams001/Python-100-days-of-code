# Cost of each type of coffee
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}


# Resources at the beginning of the day.
# It can reduce and also be refilled with any quantity not exceeding the limit the machine can hold
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0

# Function to refill the coffee machine with resources


def refill():
    global resources
    water = float(input("How much water in millilitres do you want to add? "))     
    if water + resources["water"] > 300:
        print(f"You could only add {300 - resources["water"]}ml")
        resources["water"] = 300
    else:
        resources["water"] += water

    milk = float(input("How much milk in millilitres do you want to add? "))
    if milk + resources["milk"] > 200:
        print(f"You could only add {200 - resources["milk"]}ml")
        resources["milk"] = 200
    else:
        resources["milk"] += milk

    coffee = float(input("How much coffee in grams do you want to add? "))
    if coffee + resources["coffee"] > 100:
        print(f"You could only add {100 - resources["coffee"]}g")
        resources["coffee"] = 100
    else:
        resources["coffee"] += coffee

# update resources


def update(coffee_type):
    global resources, money
    resources["water"] -= MENU[coffee_type]["ingredients"]["water"]
    resources["milk"] -= MENU[coffee_type]["ingredients"]["milk"]
    resources["coffee"] -= MENU[coffee_type]["ingredients"]["coffee"]
    money += MENU[coffee_type]["cost"]

# Check resources necessary to make coffee


def materials(coffee_type):
    if resources['water'] < MENU[coffee_type]["ingredients"]["water"]:
        print("Sorry there is not enough water.")
        return False, MENU[coffee_type]["cost"]
    elif resources['coffee'] < MENU[coffee_type]["ingredients"]["coffee"]:
        print("Sorry there is not enough coffee.")
        return False, MENU[coffee_type]["cost"]
    elif resources['milk'] < MENU[coffee_type]["ingredients"]["milk"]:
        print("Sorry there is not enough milk.")
        return False, MENU[coffee_type]["cost"]
    else:
        return True, MENU[coffee_type]["cost"]

# Take coins from the customer, check if it sufficient for the item they want, and give change if needed.


def coins(cost):
    print("Please insert coins.")
    quarter = int(input("How many quarters?: "))
    dime = int(input("How many dimes?: "))
    nickle = int(input("How many nickles?: "))
    penny = int(input("How many pennies?: "))
    amount = 0.25*quarter + 0.1*dime + 0.05*nickle + 0.01*penny
    if amount < cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        change = amount - cost
        if change > 0:
            print(f"Here is ${change} in change.")
            return True
        else:
            return True


# Put on the machine. Use "off" to turn it off. Use "report" to find out the resources and money in the machine.
# Use "refill" to top up the resources


power = True
while power:
    make1 = False
    make2 = False
    want = input("What would you like? (espresso/latte/cappuccino): ")
    if want == "off":
        power = False

    if want == "report":
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\n"
              f"Money: ${money}")

    if want == "refill":
        refill()

    if want in ["espresso", "latte", "cappuccino"]:
        make1, cost = materials(want)
        if make1:            
            print(f"{want} costs ${cost}.")
            make2 = coins(cost)

    if make2:
        print(f"Here is your {want} ☕ Enjoy!")
        update(want)
