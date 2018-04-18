prime_numbers = []
happy_numbers = []

with open('primenumbers.txt', 'r') as open_file:
    line = open_file.readline()
    while line:
        line = line.strip()
        prime_numbers.append(line)
        line = open_file.readline()

with open('happynumbers.txt', 'r') as open_file:
    line = open_file.readline()
    while line:
        line = line.strip()
        happy_numbers.append(line)
        line = open_file.readline()

for i in prime_numbers:
    if i in happy_numbers:
        print(i)
