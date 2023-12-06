row_col = int(input("Enter the number of collumns and rows:"))
matrix = []
for row in range(row_col):
    matrix.append([])
    for col in range(row_col):
        matrix[row].append(col + 1 + row * row_col)
print(*matrix, sep = "\n")
diagonal_sum = 0
for i in range(row_col):
    for j in range(row_col):
        if i + j >= row_col - 1:
            diagonal_sum += matrix[i][j]
print(diagonal_sum)


