n = int(input())
matrix = []
for row in range(n):
    a = input().split()
    matrix.append(a)
found_squares = []
for r in range(n - 1):
    for c in range(len(matrix[r]) - 1):
        if matrix[r][c] == matrix[r][c + 1] == matrix[r + 1][c] == matrix[r + 1][c + 1]:
            found_squares.append((r, c))

for r in range(n):
    row_output = ""
    for c in range(len(matrix[r])):
        if any((r, c) in square for square in found_squares):
            row_output += "* "
        else:
            row_output += matrix[r][c] + " "
    print(row_output.strip())
            