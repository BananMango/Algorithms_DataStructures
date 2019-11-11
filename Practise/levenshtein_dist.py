import numpy as np
def leven_dist(str1, str2):
    size_x = len(str1) + 1
    size_y = len(str2) + 1
    matrix = np.zeros ((size_x, size_y))
    for x in range(size_x):
        matrix [x, 0] = x
    for y in range(size_y):
        matrix [0, y] = y
    for i in range(1, size_x):
        for j in range(1, size_y):
            diff = 1 if str1[i - 1] != str2[j - 1] else 0
            matrix[i, j] = min(matrix[i - 1, j] + 1, matrix[i, j - 1] + 1, matrix[i - 1, j - 1] + diff)
    return int(matrix[size_x - 1, size_y - 1])

str1 = input()
str2 = input()
dist = leven_dist(str1, str2)
print(dist)