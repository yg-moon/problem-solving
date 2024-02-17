def rotate(mat):
    r = len(mat)
    c = len(mat[0])
    result = [[0] * r for _ in range(c)]
    for i in range(r):
        for j in range(c):
            result[j][r - i - 1] = mat[i][j]
    return result


def rotate_anti(mat):
    r = len(mat)
    c = len(mat[0])
    result = [[0] * r for _ in range(c)]
    for i in range(r):
        for j in range(c):
            result[c - j - 1][i] = mat[i][j]
    return result


def rotate_map(mat):
    return list(map(list, zip(*mat[::-1])))


def rotate_list(mat):
    return [list(row) for row in zip(*mat[::-1])]


def rotate_list_anti(mat):
    return [list(row) for row in zip(*mat)][::-1]


sample_mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

for row in sample_mat:
    print(row)
print()

for row in rotate_list(sample_mat):
    print(row)
print()
