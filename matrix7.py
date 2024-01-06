n, m = input().split(", ")
n = int(n)
m = int(m)
matrix = []
for i in range(n):
    row = input()
    row_elements = row.split(', ')[:m]
    matrix.append(row_elements)

searched_symbol = input()
found = False
for r in range(n):
    for c in range(m):
        if matrix[r][c] == searched_symbol:
            print(f"{r}, {c}")
            found = True
            break
    if found:
        continue
if not found:
    print(f"{searched_symbol} does not occur in the matrix")
        
