#Tip calculator
print("Welcome to the tip calculator.\n")
# Get the total bill
bill = float(input("What was the total bill?\n"))
# Find out what percentage of total bill they are giving as tip
tip = int(input("What percentage tip would you like to give? 10, 12, or 15?\n"))
# Number of people splitting the bill
n_people = int(input("How many people to split the bill?\n"))
# How much each is paying
amount = round((bill/n_people)*(1+tip/100),2)
print(f"Each person should pay ${amount}")