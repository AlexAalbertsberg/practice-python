def maximum(arg1,arg2,arg3):
    if arg1 >= arg2 and arg1 >= arg3:
        return arg1
    elif arg2 >= arg1 and arg2 >= arg3:
        return arg2
    elif arg3 >= arg1 and arg3 >= arg2:
        return arg3

print(maximum(1,6,9))
print(maximum('a', 'c', 'z'))
print(maximum(0,True, -1))
