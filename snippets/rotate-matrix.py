mat = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

''' Rotate a matrix by 90 degree '''
def rotate_matrix(mat_in):
    row_len = len(mat_in)
    col_len = len(mat_in[0])

    mat_out = [[0] * row_len for _ in range(col_len)]
    for r in range(row_len):
        for c in range(col_len):
            mat_out[c][row_len - 1 - r] = mat_in[r][c]

    return mat_out

print(rotate_matrix(mat))
