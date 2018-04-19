import random

def read_words():
    words = []
    with open('sowpods.txt') as open_file:
        line = open_file.readline()
        while line:
            words.append(line.strip())
            line = open_file.readline()
    return words

def pick_random_word():
    list_of_words = read_words()
    r = random.randint(0, len(list_of_words) - 1)
    return list_of_words[r]

def main():
    word = pick_random_word()
    guessedLetters = []
    guessedWord = "_" * len(word)
    guessesRemaining = 6

    while guessedWord != word:
        print(guessedWord)
        print("Guesses remaining:", guessesRemaining)

        userChar = input("Please input a letter: ")

        found = False
        if userChar not in guessedLetters:
            guessedLetters.append(userChar)
            for i in range(len(word)):
                if word[i] == userChar:
                    found = True
                    gwList = list(guessedWord)
                    gwList[i] = userChar
                    guessedWord = ''.join(gwList)
            if not found:
                guessesRemaining -= 1
                if guessesRemaining == 0:
                    break
        else:
            print ("You already guessed this letter once.")

    if guessedWord == word:
        print(word)
        print("You guessed the word! Congratulations!")
        playAgain = input("Press y to play again, or anything else to stop: ")
        if playAgain == "y":
            main()
    else:
        print("You lost! The word was", word)

main()
