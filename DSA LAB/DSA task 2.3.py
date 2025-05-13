def rotate_matrix(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n): 
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()

    return matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotated_matrix = rotate_matrix(matrix)

print("Rotated Matrix (90° Clockwise):")
for row in rotated_matrix:
    print(row)
