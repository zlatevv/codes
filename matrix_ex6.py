row_col = int(input("Enter the number of collumns and rows:"))
matrix = []
for row in range(row_col):
    matrix.append([])
    for col in range(row_col):
        matrix[row].append(col + 1 + row * row_col)
print(*matrix, sep = "\n")
sum = 0
for i in range(row_col):
    for j in range(i, row_col):
        sum += matrix[j][i]
print(sum)
