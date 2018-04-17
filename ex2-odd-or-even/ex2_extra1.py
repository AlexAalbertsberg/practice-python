number = int(input("Please give me a number: "))
rem4 = number % 4
remainder = number % 2

if rem4 == 0:
    print("The number you gave is divisible by 4.")
elif remainder == 0:
    print("The number you gave is even.")
else:
    print("The number you gave is odd.")
