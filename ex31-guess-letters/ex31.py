word = "EVAPORATE"
guessedWord = "_________"

guessedLetters = []

while guessedWord != word:
    print(guessedWord)
    userChar = input("Please input a letter: ")

    if userChar not in guessedLetters:
        guessedLetters.append(userChar)
        for i in range(len(word)):
            if word[i] == userChar:
                gwList = list(guessedWord)
                gwList[i] = userChar
                guessedWord = ''.join(gwList)
    else:
        print("You have already guessed that letter, try again.")

print(guessedWord)
print("Congratulations, you guessed the word!")
