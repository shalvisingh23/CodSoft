
# Task 4 - Rock Paper Scissors Game
import random

options = ["rock", "paper", "scissors"]

while True:
    user = input("Choose rock/paper/scissors or 'exit': ").lower()
    if user == "exit":
        break
    if user not in options:
        print("Invalid choice!")
        continue

    comp = random.choice(options)
    print(f"You: {user} | Computer: {comp}")

    if user == comp:
        print("It's a tie!")
    elif (user == "rock" and comp == "scissors") or \
         (user == "scissors" and comp == "paper") or \
         (user == "paper" and comp == "rock"):
        print("You win!")
    else:
        print("Computer wins!")
