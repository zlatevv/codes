n = int(input())
odd_set, even_set = set(), set()
for i in range(1, n+1):
    name = input()
    total_value = sum(ord(char) for char in name) // i
    (even_set if total_value % 2 == 0 else odd_set).add(total_value)
if sum(odd_set) == sum(even_set):
    print(', '.join(map(str, odd_set.union(even_set))))
elif sum(odd_set) > sum(even_set):
    print(', '.join(map(str, odd_set.difference(even_set))))
else:
    print(', '.join(map(str, odd_set.symmetric_difference(even_set))))