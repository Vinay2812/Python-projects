import random
import os


def clear():
    os.system("cls")


user_cards = []
computer_cards = []

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
"""


def get_card():
    deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(deck)
    return card


def game():
    global computer_cards, computer_sum, user_cards, user_sum
    while computer_sum < 16:
        computer_cards.append(get_card())
        computer_sum = sum(computer_cards)

    while True:
        print(f"Your cards are {user_cards} and your card sum is : {user_sum}")
        print(f"Computer first card is : {computer_cards[0]}")
        user_choice = input(
            "Do you want to pick up new card? Type 'yes' or 'no'\n"
        ).lower()
        if user_choice == "yes":
            card = get_card()
            if card == 11:
                card = int(
                    input("You got an ace card.What number do you want? '1' or '11'\n")
                )
            user_cards.append(card)
            user_sum = sum(user_cards)
            if user_sum > 21:
                print(f"\nYour cards are {user_cards}")
                return "Game Over!! Your sum is over 21."
        else:
            break
    print(f"Your cards are {user_cards} and your cards sum is : {user_sum}")
    print(
        f"Computer cards are {computer_cards} and computer cards sum is : {computer_sum}"
    )

    if user_sum == computer_sum:
        return "\nIt's a draw!! both have equal sum."
    elif user_sum > computer_sum or computer_sum > 21:
        return "\nCongratulation!! You win, your total was greater."
    else:
        return "\nSorry!! You loose, your total was less."


while True:
    clear()
    user_cards = []
    computer_cards = []
    print("Welcome To The Black-Jack Game\n")
    print(logo)

    for _ in range(2):
        card = get_card()
        if card == 11:
            card = int(
                input("You got an ace card.What number do you want? '1' or '11'\n")
            )
        user_cards.append(card)
        computer_cards.append(get_card())

    user_sum = sum(user_cards)
    computer_sum = sum(computer_cards)

    print(game())
    choice = input("\nDo you want to play the Game? Type 'yes' or 'no'\n")
    if choice == "no":
        break
