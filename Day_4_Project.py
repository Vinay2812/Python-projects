import random
import os


def clear():
    os.system("cls")


# random.seed(int(input("Enter seed : ")))


choice = [
    """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
    """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
""",
    """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""",
]

while True:
    continue_game = input("Do you want to play the game? Type 'yes' or 'no' \n").lower()
    if continue_game == "no":
        break
    clear()
    computer_choice = random.randrange(3)

    user_choice = int(input('Enter "0" for stone "1" for paper "2" scissor\n'))
    print(f"Your Choice is \n {choice[user_choice]}\n")
    print(f"Computer Choice is \n {choice[computer_choice]}\n")

    if user_choice == computer_choice:
        print("It's a Tie. You both choose same.")
    elif user_choice == 2 and computer_choice == 0:
        print("You Loose!!")
    elif user_choice == 0 and computer_choice == 2:
        print("You win!!")
    elif computer_choice < user_choice:
        print("You Win!!")
    else:
        print("You Loose!!")
