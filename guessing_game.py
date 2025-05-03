import random

while True:
    number = random.randint(1, 50)
    print("Guess a number between 1 and 10")
    guess = int(input())

    
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")

    
    if guess == number:
        print("You win!")
    else:
        print(f"Wrong! The number was {number}")

    print("Play again? (y/n)")
    if input().lower() != 'y':
        break
