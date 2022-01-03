import os


def clear():
    os.system("cls")


secret_list = {}
print("Welcome to the secret auction")

choice = "yes"
while choice == "yes":
    name = input("Enter your name : ")
    bid = int(input("Enter your bid amount $"))
    secret_list[name] = bid
    choice = input("Is there any other bidder. Type 'yes' or 'no' : ")
    clear()

max_amount = 0
winner = ""

for bidder in secret_list:
    if secret_list[bidder] > max_amount:
        max_amount = secret_list[bidder]
        winner = bidder

print(f"The winner is {winner} with maximum bid of ${max_amount}")
