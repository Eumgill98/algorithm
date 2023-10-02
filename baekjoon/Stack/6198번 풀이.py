import sys

input = sys.stdin.readline 

n = int(input())
stack = []
result = 0

buildings = [int(input()) for _ in range(n)]

for b in buildings:
    while stack and stack[-1] <= b:
        stack.pop()
    stack.append(b)

    result += len(stack) - 1

print(result)