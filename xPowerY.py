def xPowerY(a, b):
    if not b:
        return 1
    if b < 0:
        return 1 / xPowerY(a, -b)
    if b % 2:
        return a * xPowerY(a, b - 1)
    return xPowerY(a * a, b / 2)


x = 3
y = 2
print(xPowerY(x, y))
