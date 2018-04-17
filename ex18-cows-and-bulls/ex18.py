import random

def show_cows_and_bulls(number_to_guess, user_number):
    cows = 0
    bulls = 0
    for i in range(4):
        if str(user_number)[i] == str(number_to_guess)[i]:
            cows += 1
        elif str(user_number)[i] in str(number_to_guess)[i]:
            bulls += 1
    print(cows, "cows,", bulls, "bulls")


if __name__=="__main__":
    number = random.randint(1000,9999)
    guesses = 0

    while True:
        user_num = int(input("Give me a number: "))
        guesses += 1
        if user_num == number:
            print("You win!",number,"is the correct number. It took you",guesses, "guesses!")
            break
        else:
            show_cows_and_bulls(number,user_num)
