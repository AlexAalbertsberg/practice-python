category_occurrences = {}

with open('Training_01.txt', 'r') as open_file:
    line = open_file.readline()
    while line:
        category = line.split('/')[2]
        if category not in category_occurrences:
            category_occurrences[category] = 1
        else:
            category_occurrences[category] += 1
        line = open_file.readline()

print(category_occurrences)
