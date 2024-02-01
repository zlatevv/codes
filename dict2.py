products = input().split()
wanted = input().split()
data = {}
for i in range(0, len(products), 2):
    name = products[i]
    amount = int(products[i + 1])
    if name not in data:
        data[name] = 0
    data[name] += amount
for product in wanted:
    if product in data:
        print(f"We have {data[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")