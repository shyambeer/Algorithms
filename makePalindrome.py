def isPalindrome(x):
    if x == "":
        return False

    r = ""
    r = str(x)
    r = r[::-1]

    return True if x == r else False

def makePalindrome(my_str):

    pref = ""
    i = len(my_str) - 1

    while isPalindrome(pref + my_str) == False:
        pref = pref + my_str[i]
        i -= 1

    return pref + my_str







my_str = "abcd"
print(makePalindrome(my_str))
