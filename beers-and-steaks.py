a = input("Enter the name of the friend:")
b = float(input("Enter the budget:"))
c = int(input("Enter amount of beers: "))
d = int(input("Enter amount of steaks:"))
beer = 3.20
beer_cost = c * beer
steak_price = beer_cost * 0.35
steak_price = round(steak_price)
total_steak_cost = d * steak_price
total_cost = total_steak_cost + beer_cost

if b >= total_cost:
    left = b - total_cost
    print(f"{a} bought everything and has {left:.2f} leva left")
else:
    needed = total_cost - b
    print(f"{a} needs {needed:.2f} more leva")
     