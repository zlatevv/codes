food = int(input("Enter amount of food for the dog in kg: "))
cost = 5.50
food_gram = 0
while True:
    for_a_day = input("Enter amount of food in grams for the dog or stop: ")
    if for_a_day == "stop":
        break
    grams = int(for_a_day)
    food_gram += grams

remaining = abs(food_gram - (food * 1000))
price = (food_gram / 1000) * cost
if food_gram <= food * 1000:
    print(f"Food is enough. Leftovers: {remaining} grams.")
else:
    print(f"Food is not enough. You need {remaining} grams more.")
print(f"So you spent {price:.2f} leva for food")
