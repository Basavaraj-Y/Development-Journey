#Number Guessing game
import random

secret_number = random.randint(1,10)

while True:
    guess = int(input("Guess an number between 1 to 10 : "))

    if guess == secret_number:
        print("Congragulations, You guessed correctly...")
        break
    elif guess < secret_number:
        print("Too Low, Try again")
    else:
        print("Too High, Try again")