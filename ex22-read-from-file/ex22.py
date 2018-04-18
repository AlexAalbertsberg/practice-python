name_occurrences = {}

with open('nameslist.txt', 'r') as open_file:
    line = open_file.readline()
    while line:
        line = line.strip()
        if line not in name_occurrences:
            name_occurrences[line] = 1
        else:
            name_occurrences[line] += 1
        line = open_file.readline()

print(name_occurrences)
