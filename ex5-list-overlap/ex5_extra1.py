import random
a = random.sample(range(10),3)
b = random.sample(range(10),5)

newList = list()

for i in a:
    if i in b and i not in newList:
        newList.append(i)

print("a: ",a)
print("b: ",b)
print(newList)
