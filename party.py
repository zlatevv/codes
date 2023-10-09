adults = 0
kids = 0

while True:
    a = input("Enter age of members or Party: ")
    if a == "Party":
        break
    a = int(a)
    if a > 16:
        adults += 1
        liquior = adults * 15
    elif a <= 16:
        kids += 1
        candy = kids * 5
print(f"Number of adults is: {adults}")
print(f"Number of kids is: {kids}")
print(f"Money for sweets: {candy}")
print(f"Money for bottles: {liquior}")        