num = int(input("Please give me a number: "))
check = int(input("Please give me a number to divide by: "))

rem = num % check

if rem == 0:
    print(check,"divides evenly into", num)
else:
    print(check,"does not divide evenly into", num)
