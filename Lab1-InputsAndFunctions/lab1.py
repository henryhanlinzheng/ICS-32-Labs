# lab1.py

# Starter code for lab 1 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.
# Please see the README in this repository for the requirements of this lab exercise

# HENRY HANLIN ZHENG
# HHZHENG1@UCI.EDU
# 19204536

def calculator(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"

def run():
    run_again = "y"

    while run_again.lower() == 'y':
        print("Welcome to ICS 32 PyCalc!\n")
        num1 = float(input("Enter your first operand: "))
        num2 = float(input("Enter your second operand: "))
        operation = input("Enter your operation (+, -, *, /): ")

        print("The result of your calculation is:", calculator(num1, num2, operation), "\n")

        run_again = input("Run another calculation (y/n)?: \n")

if __name__ == '__main__':
    run()