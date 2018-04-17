num = int(input("Please give me a number: "))

divisorList = []

for i in range(1, int(num/2+1)):
    if num % i == 0:
        divisorList.append(i)

print(divisorList)
