import random
choices = ["rock", "paper", "scissors"]
user_choice=input("Make your choice (rock, paper, scissors):").lower()
if user_choice not in choices:
    print("Invalid selection!")
else:
    computer_choice = random.choice(choices)
    print(f"Selection of computer: {computer_choice}")
if user_choice == computer_choice:
    print("Draw!")
elif(user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
    print("You won!")
else:
    print("You lost!")