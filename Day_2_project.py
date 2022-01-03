print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
num_people = int(input("How many people to split the bill? "))

tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))

split_bill = round((bill + bill*(tip/100))/num_people, 2)

print(f"Each person should pay : ${split_bill}")
