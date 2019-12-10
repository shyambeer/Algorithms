def reverseWord(my_str):
    if len(my_str) == 0:
        return my_str
    else:
        return reverseWord(my_str[1:]) + my_str[0]


my_str = "Monday"
print(reverseWord(my_str))
