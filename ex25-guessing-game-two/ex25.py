guess = 50
guesses = 0

high_divisor = 100
low_divisor = 0

while True:
    guesses += 1
    response = input("I'm guessing your number is " + str(guess) + ", is that correct? (yes/high/low)")

    if response == "yes":
        print("I guessed the number in", guesses, "guesses!")
        break
    elif response == "high":
        high_divisor = guess
        guess = int((guess + low_divisor) / 2)
    elif response == "low":
        low_divisor = guess
        guess = int((guess + high_divisor) / 2)
    else:
        break

print("Game over.")
