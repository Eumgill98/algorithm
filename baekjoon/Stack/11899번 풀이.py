import sys

input = sys.stdin.readline

stack = []

c = 0

for i in input():
    if not stack and i==')':
        c += 1
    elif stack and i == ')':
        stack.pop()

    elif i == '(':
        stack.append('(')
    
print(c + len(stack))