import random

options=("rock", "paper", "scissor")


running = True

while running:
    player = None
    computer=random.choice(options)


    while player not in options:
        player = input("Enter rock, paper, or scissor: ").lower()
    print(f"Player: {player}")
    print(f"Computer: {computer}")



    if player==computer:
        print("It is a tie!")
    elif player == "rock" and computer =="scissor":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissor" and computer == "paper":
        print("You win!")
    else:
        print("You lose!")

    if not input("Do you want to play again? (yes/no): ").lower() == "y":
        running = False
print("Thanks for playing!")