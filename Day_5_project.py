import random

print("Welcome To Password Generator!")
letters_num = int(input("How many letters woud you like in your password?\n"))
symbol_num = int(input("How may symbols would you like?\n"))
num = int(input("How many numbers would you like?\n"))

letters = []

for i in range(26):
    letters.append(chr(i + 65))
for i in range(26):
    letters.append(chr(i + 97))

symbols = ["(", ")", "@", "!", "#", "%", "*", "+"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


random_string = []

for i in range(letters_num):
    random_string.append(random.choice(letters))

for i in range(symbol_num):
    random_string.append(random.choice(symbols))

for i in range(num):
    random_string.append(random.choice(numbers))

random.shuffle(random_string)
password = ""

for c in random_string:
    password += c

print(f"Your Password can be {password}")
