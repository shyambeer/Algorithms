def climbStairs(n):
    k = n + 1

    def fib(k):
        if k < 2:
            return k
        else:
            return fib(k - 1) + fib(k - 2)

    return fib(k)


n = 35
print(climbStairs(n))
