a = [1,1,2,3,5,8,13,21,23,55,89]
b = [1,2,3,4,5,6,7,8,9,10,11,12,13]

def dedupe_set(l1,l2):
    return list(set(a).intersection(b))

print(dedupe_set(a,b))
