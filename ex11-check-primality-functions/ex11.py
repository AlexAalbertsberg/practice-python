num = int(input("Please give me a number: "))

def isPrime(number):
    if number==1:
        prime = False
    elif number==2:
        prime = True
    else:
        prime = True
        for i in range(2, number):
            if(number % i == 0):
                prime = False
                break
    return prime

if(isPrime(num)):
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")
