row_col = int(input())
matrix = []
for row in range(row_col):
    matrix.append([])
    for col in range(row_col):
        matrix[row].append(col + 1 + row * row_col)
sum = 0
for i in range(row_col):
    for j in range(i+1):
        sum += matrix[i][j]
print(sum)
print(*matrix, sep="\n")
