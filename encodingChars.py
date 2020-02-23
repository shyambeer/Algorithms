# Python program to move every character
# K times ahead in a given string

# Function to move string character
def encode(s, k):
    # changed string
    newS = ""

    # iterate for every characters
    for i in range(len(s)):

        # ASCII value
        val = ord(s[i])

        # store the duplicate
        dup = k

        # if k-th ahead character exceed 'z'

        if val + k > 122:
            k -= (122 - val)
            k = k % 26
            newS += chr(96 + k)

        else:
            if val == 32:
                newS += chr(32)
            if val == 56:
                newS += chr(56)
            newS += chr(val + k)

        k = dup

    # print the new string
    print(newS)


# driver code
str = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
k = 2

encode(str, k)
