inStr = str(input("Please give me a string: "))

isPalindrome = True
strl = len(inStr)

for i in range(0, int(strl/2)):
    front = inStr[i]
    back = inStr[strl-(1+i)]
    if(front != back):
        isPalindrome = False
print(isPalindrome)
