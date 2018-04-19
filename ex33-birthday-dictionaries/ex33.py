birthdays = {
    "Alex Aalbertsberg" : "08/05/1991",
    "Albert Einstein" : "03/14/1879",
    "Henk" : "01/01/2001"
}

def show_known_birthdays():
    print("Welcome to the birthday dictionary. We know the birthdays of: ")
    for i in birthdays.keys():
        print(i)

def main():
    show_known_birthdays()

    name = input("Whose birthday would you like to look up? ")

    if(name in birthdays.keys()):
        print(name + "'s birthday is " + birthdays[name] + ".")
    else:
        print("We do not have a birthday on record for " + name + ".")

main()
