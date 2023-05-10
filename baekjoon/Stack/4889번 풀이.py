import sys
input = sys.stdin.readline
answer = []
while True:
    stack = []
    c = 0
    array = input().strip()
    if '-' in array:
        break
    for i in range(len(array)):
        if not stack and array[i] == '}':
            c += 1
            stack.append('{')
        elif stack and array[i] == '}':
            stack.pop()
        else:
            stack.append(array[i])

    c += len(stack) // 2
    answer.append(c)

for i in range(len(answer)):
    print(i+1, '. ', answer[i], sep='')






