import random

a = random.randint(1,9)

num = int(input("Guess a number between 1 and 9: "))

if num > a:
    print("Too high!")
elif num < a:
    print("Too low!")
elif num == a:
    print("Exactly right!")
