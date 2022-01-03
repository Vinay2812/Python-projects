import os


def clear():
    os.system("cls")
    print(logo)


logo = """
 _____________________
|  _________________  |
| |Vinay Calc     0.| |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
 """


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


basic_operations = {"+": add, "-": sub, "*": multiply, "/": divide}


def calculator(first_number):
    operation = input("Enter the operation \n+\n-\n*\n/\n")
    next_number = float(input("Enter the next number : "))
    function = basic_operations[operation]
    answer = function(first_number, next_number)
    next_choice = input("Do you want to do further calculations? Type 'yes' or 'no'\n")
    if next_choice == "yes":
        clear()
        print(f"Previous answer : {answer}")
        return calculator(answer)
    else:
        return answer


choice = "yes"
while choice == "yes":
    clear()
    first_number = float(input("Enter first number : "))
    answer = calculator(first_number)
    print(f"Your final answer is : {answer}")
    choice = input("Do you want to perform new calculations? Type 'yes' or 'no' \n")
