stack = []
for _ in range(5):
    stack.append(int(input()))

stack = sorted(stack)
print(sum(stack)//5)
print(stack[2])