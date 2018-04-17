import random

a = random.sample(range(1,100),10)
b = random.sample(range(1,100),12)

c = []
[c.append(i) for i in a for j in b if i == j and i not in c]

print(a)
print(b)
print(c)
