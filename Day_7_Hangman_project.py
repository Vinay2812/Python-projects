import random

list_of_words = [
    "hello",
    "welcome",
    "complete",
    "challange",
    "hardwork",
    "butterfly",
    "fantastic",
    "awesome",
    "random",
]

word = random.choice(list_of_words)

hangman = [
    """      
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \\
     |
 ____|___""",
    """      
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / 
     |
 ____|___""",
    """      
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |       
     |
 ____|___""",
    """      
      _______
     |/      |
     |      (_)
     |      \|/
     |       
     |       
     |
 ____|___""",
    """     
      _______
     |/      |
     |      (_)
     |      \|
     |       
     |      
     |
 ____|___""",
    """     
      _______
     |/      |
     |      (_)
     |       |
     |       
     |       
     |
 ____|___""",
    """      
      _______
     |/      |
     |      (_)
     |      
     |       
     |       
     |
 ____|___""",
    """     
      _______
     |/      
     |     
     |      
     |      
     |      
     |
 ____|___""",
]

chars = []

for i in range(len(word)):
    chars.append("_")

lives = 7
# print(word)
while lives > 0:
    print(f"No. of lives remaining : {lives}")
    print(hangman[lives])
    for c in chars:
        print(c, end=" ")
    letter = input("\n\nGuess the letter : ")
    if (letter not in word) or (letter in chars):
        lives -= 1
    else:
        for i in range(len(word)):
            if word[i] == letter:
                chars[i] = letter
        if "_" not in chars:
            break

if lives == 0:
    print(hangman[0])
    print("\nGame Over!!You were out of moves.")
else:
    print("\nCongratulations!!You Saved the man.")
