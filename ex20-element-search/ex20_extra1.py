def find_number_binary_search(haystack, needle):
    left = 0
    right = len(haystack)-1

    while True:
        if left > right:
            return False

        m = int((left+right)/2)

        if(haystack[m] < needle):
            left = m + 1
        elif(haystack[m] > needle):
            right = m - 1
        else:
            return True

a = [1,1,3,5,8,9,10]
print(find_number_binary_search(a,9))
print(find_number_binary_search(a,15))
