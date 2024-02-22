add = lambda x, y: x + y
subtract = lambda x, y: x - y
multiply = lambda x, y: x * y
divide = lambda x, y: x / y
num1, num2, operator = input().split()
num1 = int(num1)
num2 = int(num2)
if operator == "+":
    print(add(num1, num2))
elif operator == "-":
    print(subtract(num1, num2))
elif operator == "*":
    print(multiply(num1, num2))
elif operator == "/":
    if num2 == 0:
        print("You can't divide by ZERO")
        exit(0)
    print(divide(num1, num2))