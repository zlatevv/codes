from collections import deque
queue = deque()
while True:
    command = input()
    if command == "END":
        print(f"{len(queue)} people remaining")
        break
    elif command == "PAID":
        while queue:
            print(queue.popleft())
    else:
        queue.append(command)