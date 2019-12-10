import numpy as np


def shiftGrid(grid, k):
    np_arr = np.array(grid)
    arr = list(np.roll(np_arr.flatten(), k))

    f_grid = []
    r_size = len(grid[0])
    for i in range(0, len(arr), r_size):
        f_grid.append(arr[i:i + r_size])

    return f_grid


grid = [[3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10], [12, 0, 21, 13]]
k = 2
print(shiftGrid(grid, k))
