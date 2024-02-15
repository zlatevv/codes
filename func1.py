def square(num1, num2):
    result = num1 ** num2
    return result
a, b = map(int, input().split(", "))
print(f"{a} to the power {b} is {square(a, b)}")