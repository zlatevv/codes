N = int(input("Enter the number of rows and columns: "))

matrix = []
for i in range(N):
    row_input = input(f"Enter row {i + 1}: ")
    matrix.append(row_input)

search_symbol = input("Enter the symbol to search for: ")

found = False
for row in range(N):
    for col in range(len(matrix[row])):
        if matrix[row][col] == search_symbol:
            print(f"({row}, {col})")
            found = True
            break
    if found:
        break

if not found:
    print(f"{search_symbol} does not exist in matrix!")