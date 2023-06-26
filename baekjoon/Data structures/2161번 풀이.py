from collections import deque
n = int(input())
stack = deque([f for f in range(1, n+1)])
total = []
while True:
    total.append(stack.popleft())
    if len(stack) == 0:
        break
    stack.append(stack.popleft())

print(*total)
