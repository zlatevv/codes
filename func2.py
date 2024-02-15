import math

def square_root(num1):
    numbers = []
    for num in num1:
        result = math.sqrt(num)
        numbers.append((num, result))
    return numbers
a = list(map(int, input().split()))
for num, i in square_root(a):
    print(f"Square of {num} is {i:.2f}")
