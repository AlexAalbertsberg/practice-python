def fibonacci(a,b):
    return b, a+b

a = 1
b = 1
amt = int(input("How many numbers should I generate? (min. 2): "))

fib_list = []
fib_list.append(a)
fib_list.append(b)

while len(fib_list) < amt:
    a,b = fibonacci(a,b)
    fib_list.append(b)

print(fib_list)
