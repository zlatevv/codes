def absolute(num1):
    ml = []
    for i in num1:
        absoulte_number = abs(float(i))
        ml.append(absoulte_number)
    return ml
a = input().split(" ")
print(absolute(a))

