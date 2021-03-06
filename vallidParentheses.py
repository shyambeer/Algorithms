def validParentheses(s):
    stack = []
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        elif stack and s[stack[-1]] == '(':
            stack.pop()
        else:
            stack.append(i)
    stack = [-1] + stack + [len(s)]
    ans = 0
    for i in range(len(stack) - 1):
        ans = max(ans, stack[i + 1] - stack[i] - 1)
    return ans


s = "(()"
print(validParentheses(s))
