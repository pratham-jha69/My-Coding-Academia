import random

lowest = 1
highest = 100

answer=random.randint(lowest, highest)
guesses = 0
is_running = True

print(f"Welcome to the Number Guessing Game!\n")
print(f"Guess a number between {lowest} and {highest}.\n")

while is_running:

    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses+=1
        if guess < lowest or guess > highest:
            print("The number is out of range.")
            print(f"Please enter a number between {lowest} and {highest}")
        elif guess < answer:
            print("Too low!")
        elif guess > answer:
            print("Too high!")
        else:
            print(f"Congratulations! Correct answer.")
            print(f"Number of guesse: {guesses}")
            is_running = False
    else:
        print("Invalid input. Please enter a number.")
        print(f"Please enter a number between {lowest} and {highest}")