from data import data
import os
import random


def clear():
    os.system("cls")


logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/    
  __ _  __ _ _ __ ___   ___  
 / _` |/ _` | '_ ` _ \ / _ \\
| (_| | (_| | | | | | |  __/
 \__, |\__,_|_| |_| |_|\___|
  __/ |                          
 |___/ 
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""


def max_count(a, b):
    if a > b:
        return "A"
    return "B"


def higher_lower_game(user_A, score):
    count_of_A = user_A["follower_count"]
    print(
        f"\nCompare A : {user_A['name']}, {user_A['description']}, {user_A['country']}"
    )
    print(f"\n{vs}\n")
    user_B = random.choice(data)
    while user_A == user_B:
        user_B = random.choice(data)
    count_of_B = user_B["follower_count"]
    print(
        f"\nAgainst B : {user_B['name']}, {user_B['description']}, {user_B['country']}"
    )

    answer = max_count(count_of_A, count_of_B)
    user_choice = input("Who has more follower? 'A' or 'B' : ").upper()
    if user_choice == answer:
        score += 1
        clear()
        print(f"\n{logo}\n")
        print(f"You are Right!! Current Score : {score}")
        return higher_lower_game(user_B, score)
    else:
        return score


while True:
    clear()
    print("Welcome to Higher Lower Game")
    print(f"\n{logo}\n")
    print(f"Your final score : {higher_lower_game(random.choice(data), 0)}\n")
    choice = input("Do you want to play again? Type 'yes' or 'no'\n").lower()
    if choice == "no":
        break
