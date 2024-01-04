n = int(input())
max_intersection = []
for _ in range(n):
    range1_start, range1_end, range2_start, range2_end = map(int, input().replace('-', ',').split(','))
    intersection_start = max(range1_start, range2_start)
    intersection_end = min(range1_end, range2_end)
    if intersection_start <= intersection_end:
        current_intersection = list(range(intersection_start, intersection_end + 1))
        if len(current_intersection) > len(max_intersection):
            max_intersection = current_intersection

print(f"The longest intersection is {max_intersection} with length {len(max_intersection)}")