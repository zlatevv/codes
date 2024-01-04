row_col = int(input())
matrix = []
for row in range(row_col):
    matrix.append([])
    for col in range(row_col):
        matrix[row].append(col + 1 + row * row_col)
sum1 = sum(matrix[i][i] for i in range(row_col))
print(sum1)
sum2 = sum(matrix[i][row_col - i - 1] for i in range(row_col))
print(sum2)

print(*matrix, sep = "\n")
