a = int(input("Enter number of locations:"))
for i in range(a):
    b = int(input("Enter expected number of sandwiches:"))
    c = int(input("Enter amount of days:"))
    eaten = 0
    for j in range(c):
        d = int(input("Sandwiches eaten per day:"))
        eaten += d
    if eaten <= b:
        remaining = b - eaten
        print(f"Good job! {remaining:.2f} sandwiches are left")
    else:
        needed = eaten - b
        print(f"You need {needed:.2f} more sandwiches")
