name = input("Please enter your name: ")
age = int(input("Please enter your age: "))

years_to_100 = 100 - age

amount = int(input("How many repetitions?: "))

toPrint = "Dear " + name + ", you will turn 100 in the year " + str(2018+years_to_100)

print(toPrint * amount)
