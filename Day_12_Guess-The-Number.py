import random
import os


def clear():
    os.system("cls")


attempts_left = int()

logo = """
  ____  __ __  ____   ____   ____     _____  _   _  ____     __  _  __ __  __  __ _____  ____ _____ 
/ (_,`|  |  || ===| (_ (_` (_ (_`   |_   _|| |_| || ===|   |  \| ||  |  ||  \/  || () )| ===|| () )
\____) \___/ |____|.__)__).__)__)     |_|  |_| |_||____|   |_|\__| \___/ |_|\/|_||_()_)|____||_|\_\
                                                                                                                                                                 
"""


def guess_the_number():
    clear()
    print("Welcome to the game.")
    number = random.randint(0, 100)
    print(f"\n{logo}\n")
    level = input("Which level do you want? 'easy' or 'difficult'\n").lower()

    if level == "easy":
        attempts_left = 10
    else:
        attempts_left = 5
    while attempts_left > 0:
        print(f"\nAttempts left : {attempts_left}")
        user_guess = int(input("Guess the number : "))
        if user_guess == number:
            print(f"Congratulation!! You Guessed the number.\n")
            return
        elif user_guess < number:
            print(f"{user_guess} is too low.")
        else:
            print(f"{user_guess} is too high.")
        attempts_left -= 1

    if attempts_left == 0:
        print("You ran out of guesses.Please try again.\n")


while True:
    guess_the_number()
    choice = input("Do you want to play the game again? Type 'yes' or 'no'\n")
    if choice == "yes":
        guess_the_number()
    else:
        break
