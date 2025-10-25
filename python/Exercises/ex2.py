import random

secretNumber = random.randint(1,10)
guess = None
attempts = 0

print("# GUESS THE NUMBER GAME [1-10] #")

# Guess number game loop
while (guess != secretNumber):

    attempts += 1

    guess = int(input("\nYour guess: "))
    if guess < secretNumber:
        print("\nToo low!")
    elif guess > secretNumber:
        print("\nToo high!")
    else:
        print(f"\nBro got it right after {attempts} attempts! :)\n")