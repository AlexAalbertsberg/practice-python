a = [1,1,3,4,5,5,6,7,8,8]

def remove_duplicates_via_list(l):
    new_list = []
    for i in l:
        if i not in new_list:
            new_list.append(i)

    return new_list

print(remove_duplicates_via_list(a))
