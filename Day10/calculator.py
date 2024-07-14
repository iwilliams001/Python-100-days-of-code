import os
cls = lambda: os.system('cls')
#cls()
## Calculator
#Add
def add(n1,n2):
    return n1+n2

#Subtract
def minus(n1,n2):
    return n1-n2

#Multiply
def times(n1,n2):
    return n1*n2

#Divide
def divide(n1,n2):
    return n1/n2

operations = {
    "+": add,
    "-": minus,
    "*": times,
    "/": divide,
}

def calculator():
    num1 = float(input("What is the first number?: "))

    for key in operations:
        print(key)

    should_continue = True
    while should_continue == True:
        symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))
        if num2 == 0.0 and symbol == "/":
            print("You cannot divide by zero")
            should_continue = False
        else:
            answer = operations[symbol](n1=num1,n2=num2)
            print(f"{num1} {symbol} {num2} = {answer}")
            if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ") == "y":
                num1 = answer
            else:
                should_continue = False
                cls()
                calculator()

calculator()
