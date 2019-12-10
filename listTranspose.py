def listTranspose(my_list):
    count = len(my_list)
    result = []
    for i in range(count):
        current = []
        result.append(current)
        for j in range(count):
            if j < count and i < len(my_list[j]):
                current.append(my_list[j][i])

    return result


my_list = [[2, 3, 15], [6, 12], [13, 7, 9, 5], [11, 8, 1]]
print(listTranspose(my_list))
