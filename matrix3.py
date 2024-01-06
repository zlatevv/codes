row_col = int(input())
matrix = []
for row in range(row_col):
    a = input().split()
    matrix.append(a)
for row in matrix:
    print(*row, sep = " ")