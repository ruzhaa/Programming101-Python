def check_matrix(matrix, cord):
    if cord[0] < 0 or cord[0] >= len(matrix):
        return False
    if cord[1] < 0 or cord[1] >= len(matrix):
        return False
    return True


def change_matrix(matrix, cord):
    start_matrix = copy.deepcopy(matrix)
    if check_matrix(matrix, cord):
        print(cord)
        bomb = matrix[cord[0]][cord[1]]
        print(bomb)
        if cord[0] - 1 < 0 and cord[1] - 1 < 0:
            matrix[cord[0]][cord[1] + 1] -= bomb
            matrix[cord[0] + 1][cord[1]] -= bomb
            matrix[cord[0] + 1][cord[1] + 1] -= bomb
            if matrix[cord[0]][cord[1]] <= 0:
                matrix[cord[0]][cord[1]] = 0
        if cord[0] - 1 < 0 and cord[1] - 1 == 0:
            matrix[cord[0]][cord[1] - 1] -= bomb
            matrix[cord[0]][cord[1] + 1] -= bomb
            matrix[cord[0] + 1][cord[1]] -= bomb
            matrix[cord[0] + 1][cord[1] - 1] -= bomb
            matrix[cord[0] + 1][cord[1] + 1] -= bomb
            if matrix[cord[0]][cord[1]] <= 0:
                matrix[cord[0]][cord[1]] = 0
        if cord[0] - 1 < 0 and cord[1] == len(matrix):
            matrix[cord[0]][cord[1] - 1] -= bomb
            matrix[cord[0] + 1][cord[1]] -= bomb
            matrix[cord[0] + 1][cord[1] - 1] -= bomb
            if matrix[cord[0]][cord[1]] <= 0:
                matrix[cord[0]][cord[1]] = 0
        if matrix[cord[0]][cord[1]] <= 0:
            matrix[cord[0]][cord[1]] = 0
# matrix[cord[0]][cord[1] - 1] -= bomb
# matrix[cord[0] - 1][cord[1]] -= bomb
# matrix[cord[0] - 1][cord[1] + 1] -= bomb
# matrix[cord[0] - 1][cord[1] - 1] -= bomb
# matrix[cord[0] + 1][cord[1] - 1] -= bomb
    return matrix


def matrix_bombing(matrix):
# result = dict()
    start_matrix = copy.deepcopy(matrix)
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            cord = [i, j]
            change_matrix(matrix, cord)
            print(matrix)
            matrix = start_matrix
# print(start_matrix)
    return matrix

print(matrix_bombing([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))