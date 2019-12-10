def reverseString(my_str):
    if my_str == " ":
        return

    return ' '.join(reversed(my_str.split(' ')))



my_str = "Today is Wednesday"
print(reverseString(my_str))
