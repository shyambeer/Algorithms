def pascalsTriangle(rows):
    my_list = []

    def pascalValue(i, j):
        if j == 1 or i == j:
            return 1
        return pascalValue(i - 1, j - 1) + pascalValue(i - 1, j)

    for num in range(rows):
        my_list.append(pascalValue(rows, num+1))

    return my_list


rows = 23
print(pascalsTriangle(rows))
