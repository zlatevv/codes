from collections import deque

children = input().split()
n = int(input())
circle = deque(children)

while len(circle) > 1:
    for _ in range(n - 1):
        # Преместваме детето с горещ картоф напред в кръга
        circle.append(circle.popleft())
    
    # Изгонваме детето с горещ картоф
    removed_child = circle.popleft()
    print(f"Removed {removed_child}")

winner = circle[0]
print(f"Winner is {winner}")

