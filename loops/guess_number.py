import random

secret = random.randint(1, 10)

while True:

    guess = int(input("Guess the number: "))

    if guess == secret:
        print("Correct!")
        print("")
        secret = random.randint(1, 10)
    elif guess < secret:
        print("Too low")
    else:
        print("Too high")
