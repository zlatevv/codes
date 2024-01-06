row_col = int(input())
matrix = []
for row in range(row_col):
    a = list(map(int, input().split(", ")))
    matrix.append(a)
sum = sum(matrix[i][row_col - i - 1] for i in range(row_col))
print(sum)