data = {}
total_products = 0
total_quantities = 0
while True:
    entry = input()
    if entry == "START":
        break
    products, quantity = map(str.strip , entry.split(": "))
    quantity = int(quantity)
    if products in data:
        data[products] += quantity
    else:
        data[products] = quantity
    total_products += 1
    total_quantities += quantity
print("Products in stock:")
for product, quantity in data.items():
    print(f"- {product}: {quantity}")

print(f"Total Products: {total_products}")
print(f"Total Quantity: {total_quantities}")

    