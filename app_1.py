# Напишите функцию для транспонирования матрицы
# Пример: [[1, 2, 3], [4, 5, 6]] -> [[1,4], [2,5], [3, 6]]

def transpose_matrix(matrix):
    """Function transposes the matrix"""
    rows = len(matrix)
    cols = len(matrix[0])

    transposed = []
    for j in range(cols):
        transposed_row = []
        for i in range(rows):
            transposed_row.append(matrix[i][j])
        transposed.append(transposed_row)

    return transposed


original_matrix = [[1, 2, 3], [4, 5, 6]]
transposed_matrix = transpose_matrix(original_matrix)
print(transposed_matrix)
