class Trie:
    def __init__(self, val):
        self.children = {}
        self.cnt = 0
        self.character = val

class Solution:
    def longestCommonPrefix(self, strs):
        root = Trie('#')
        for s in strs:
            cur = root
            for c in s:
                if c not in cur.children:
                    cur.children[c] = Trie(c)
                cur = cur.children[c]
                cur.cnt += 1
        res = ''
        cur = root
        pre = None
        while pre != cur:
            pre = cur
            for child in cur.children.values():
                if child.cnt == len(strs):
                    res += child.character
                    cur = child
        return res


my_str = ["flower","flow","flight"]

s = Solution()
print(s.longestCommonPrefix(my_str))