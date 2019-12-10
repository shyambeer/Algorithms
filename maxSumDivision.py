def maxSumDivThree(nums):
    seen = [0, 0, 0]
    for a in nums:
        for i in seen[:]:
            seen[(i + a) % 3] = max(seen[(i + a) % 3], i + a)
    return seen[0]


nums = [3, 6, 5, 1, 8]
print(maxSumDivThree(nums))
