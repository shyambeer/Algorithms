class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


def maxDepth(root: 'Node') -> int:
    def dfs(root):
        if not root:
            return 0
        res = 0
        for child in root.children:
            res = max(dfs(child), res)
        return res + 1

    return dfs(root)


root = Node
root = [1, "null", 3, 2, 4, "null", 5, 6]
print(maxDepth(root))
