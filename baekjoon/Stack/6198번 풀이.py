import sys

input = sys.stdin.readline 

n = int(input())
stack = []
result = 0

for _ in range(n):
    b = int(input())
    while stack and stack[-1] <= b:
        stack.pop()
    stack.append(b)

    result += len(stack) - 1

print(result)

