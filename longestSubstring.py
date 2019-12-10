import collections


def longestSubstring(my_str):
    max_len = 0
    queue = collections.deque()
    for ch in my_str:
        if ch in queue:
            max_len = max(max_len, len(queue))
            while queue:
                ch1 = queue.popleft()
                if ch1 == ch:
                    break
        queue.append(ch)
    max_len = max(max_len, len(queue))
    return max_len


my_str = "greeksforgreeks"
print(longestSubstring(my_str))
