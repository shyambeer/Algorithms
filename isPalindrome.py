def isPalindrome(x):
    if x < 0:
        return False

    r = ""
    r = str(x)
    r = r[::-1]

    return True if x == int(r) else False



print(isPalindrome(-121))