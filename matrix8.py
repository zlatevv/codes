n, m = input().split(", ")
n = int(n)
m = int(m)
matrix = []
for row in range(n):
    row = input()
    elements = row.split(", ")[:m]
print(*matrix, sep = "\n")
max_sum = 0
max_square = []
for i in range(n - 1):
    for j in range(len(matrix[i]) - 1):
        current_sum = int(matrix[i][j]) + int(matrix[i][j + 1]) + int(matrix[i + 1][j]) + int(matrix[i + 1][j + 1])
        current_sum = int(current_sum)
        if current_sum > max_sum:
            max_sum = current_sum
            max_square = [[matrix[i][j], matrix[i][j + 1]], [matrix[i + 1][j], matrix[i + 1][j + 1]]]
for row in max_square:
    print(row[0], row[1])
print(max_sum)
