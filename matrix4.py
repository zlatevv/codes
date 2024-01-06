row_col = int(input())
matrix = []
total_sum = 0
for row in range(row_col):
    current_row = list(map(int, input().split(", ")))
    matrix.append(current_row)
for r in matrix:
    total_sum += sum(r)
print(total_sum)