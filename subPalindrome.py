def subPalindrome(s):
    s = s.lower()
    results = []

    if s == "":
        return ""
    if len(s) == 1:
        return s
    if len(s) == 2:
        if s == s[::-1]:
            return s
        else:
            return s[0]

    for i in range(len(s)):
        for j in range(0, i):
            chunk = s[j:i + 1]

            if chunk == chunk[::-1]:
                results.append(chunk)

    # return s.index(max(results, key=len)), results
    if results:
        return max(results, key=len)
    else:
        return s




my_str = "abcda"
print(subPalindrome(my_str))
