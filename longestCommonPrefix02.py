def longestCommonPrefix(strs):
    minL = min(map(len, strs)) if strs else 0
    for i in range(minL):
        for j in range(1, len(strs)):
            if strs[j][i] != strs[0][i]:
                return strs[0][:i]
    return strs[0][:minL] if minL else ""



my_str = ["flower","flow","flight"]
print(longestCommonPrefix(my_str))