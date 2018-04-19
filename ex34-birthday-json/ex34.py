import json

def show_known_birthdays():
    with open('birthdays.json') as json_data:
        birthdays = json.load(json_data)

    print("Welcome to the birthday dictionary. We know the birthdays of: ")

    for i in birthdays.keys():
        print(i)
        
    return birthdays

def main():
    birthdays = show_known_birthdays()

    name = input("Whose birthday would you like to look up? ")

    if(name in birthdays.keys()):
        print(name + "'s birthday is " + birthdays[name] + ".")
    else:
        print("We do not have a birthday on record for " + name + ".")

main()
