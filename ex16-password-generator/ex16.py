import random, string

def generatePassword(length):
    pw = ""
    for i in range(length):
        a = random.randint(1,4)
        if a == 1:
            pw += random.choice(string.ascii_lowercase)
        elif a == 2:
            pw += random.choice(string.ascii_uppercase)
        elif a == 3:
            pw += random.choice(string.digits)
        elif a == 4:
            pw += random.choice(string.punctuation)

    return pw


password = generatePassword(10)
print(password)
