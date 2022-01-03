MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
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
    },
}

resources = {"water": 300, "milk": 200, "coffee": 100, "money": 0}

penny = 0.01
dime = 0.1
nickel = 0.05
quarter = 0.25


def enough_resources(choice):
    if MENU[choice]["ingredients"]["water"] > resources["water"]:
        return "water"
    if MENU[choice]["ingredients"]["milk"] > resources["milk"]:
        return "milk"
    if MENU[choice]["ingredients"]["coffee"] > resources["coffee"]:
        return "coffee"
    return "yes"


def enough_money(amount, choice):
    if amount < MENU[choice]["cost"]:
        return False
    else:
        return True


while True:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        break
    elif choice == "report":
        print(
            f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}gm\nMoney: {resources['money']}$"
        )
    else:
        is_enough_resources = enough_resources(choice)
        # print(is_enough_resources)
        if is_enough_resources == "yes":
            print("Please insert coins.")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))
            amount = (
                quarters * quarter + dimes * dime + nickles * nickel + pennies * penny
            )
            is_enough_money = enough_money(amount, choice)
            change = 0.0
            if is_enough_money == True:
                resources["money"] += MENU[choice]["cost"]
                change = amount - MENU[choice]["cost"]
                resources["water"] -= MENU[choice]["ingredients"]["water"]
                resources["milk"] -= MENU[choice]["ingredients"]["milk"]
                resources["coffee"] -= MENU[choice]["ingredients"]["coffee"]
                print(f"Here is ${round(change,2)} in change.")
                print(f"Your {choice}☕ is ready. Enjoy.")
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print(f"Sorry, There is not enough {is_enough_resources}")
