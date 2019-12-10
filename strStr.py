def strStr(haystack, needle):
    index = 0

    if needle == "":
        return 0

    if needle in haystack:
        c = needle[0]
        for ch in haystack:
            if ch == c:
                if haystack[index: index + len(needle)] == needle:
                    return index
            index += 1

    return -1



haystack = "hello"
needle = "ll"

print(strStr(haystack, needle))