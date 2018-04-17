import random

a = random.randint(1,9)

while True:
    num = input("Guess a number between 1 and 9: ")

    if num == "exit":
        break

    num = int(num)

    if num > a:
        print("Too high!")
    elif num < a:
        print("Too low!")
    elif num == a:
        print("Exactly right! Generating a new random number...")
        a = random.randint(1,9)
