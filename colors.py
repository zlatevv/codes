n = int(input("Enter the times for spinning:"))
colors = []
red = 0
orange = 0
yellow = 0
white = 0
other = 0
black = 0
for _ in range(n):
    color = input("Enter a color:")
    colors.append(color)
total_points = 0
for color in colors:
    if color == "red":
        total_points += 5
        red += 1
    elif color == "orange":
        total_points += 10
        orange += 1
    elif color == "yellow":
        total_points += 15
        yellow += 1
    elif color == "white":
        total_points += 20
        white += 1
    elif color == "black":
        total_points //= 2
        black += 1
    else:
        other += 1

# Извеждане на резултатите
print(f"Total points: {total_points}")
print(f"Red sector: {red}")
print(f"Orange sector: {orange}")
print(f"Yellow sector: {yellow}")
print(f"White sector: {white}")
print(f"Other colors picked: {other}")
print(f"Divides from black sector: {black}")