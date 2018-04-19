import random

def read_words():
    words = []
    with open('sowpods.txt') as open_file:
        line = open_file.readline()
        while line:
            words.append(line.strip())
            line = open_file.readline()
    return words

def pick_random_word(words):
    r = random.randint(0, len(words) - 1)
    return words[r]

list_of_words = read_words()
print(pick_random_word(list_of_words))
