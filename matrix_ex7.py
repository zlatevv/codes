row_col = int(input("Enter the number of collumns and rows:"))
matrix = []
for row in range(row_col):
    matrix.append([])
    for col in range(row_col):
        matrix[row].append(col + 1 + row * row_col)
print(*matrix, sep = "\n")
diagonal_sum = 0
for i in range(len(matrix)):
       for j in range(i, len(matrix)):
            diagonal_sum += matrix[i][j]
print(f"Sum of the diagonal: {diagonal_sum}")
