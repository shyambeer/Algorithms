import numpy as np


def rotateImage(a):
    b =np.rot90(a, 1, axes=(0, 1))
    return b


a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

print(rotateImage(a))
