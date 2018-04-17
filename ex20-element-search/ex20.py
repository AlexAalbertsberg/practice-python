def find_number(haystack, needle):
    found = False
    for num in haystack:
        if num == needle:
            found = True
            break
    return found

a = [1,1,3,5,8,9,10]
print(find_number(a,3))
print(find_number(a,7))
