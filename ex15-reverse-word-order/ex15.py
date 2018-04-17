inStr = input("Please give me a long string, containing multiple words: ")

str_list = inStr.split()
str_list.reverse()

print(" ".join(str_list))
