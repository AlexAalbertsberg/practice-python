import json

name = input("Please input a new name: ")
birthday = input("Please provide this person's birthday: ")

with open('birthdays.json', 'r') as json_data:
    d = json.load(json_data)

d[name] = birthday

with open('birthdays.json', 'w') as json_data:
    j = json.dumps(d, indent=4)
    json_data.write(j)
