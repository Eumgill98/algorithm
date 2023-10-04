import sys

input = sys.stdin.readline

array = list(map(str, input().strip()))

stack = []
cnt = 0
repeat = 0

for a in array:
    if a == '(':
        stack.append([cnt-1, repeat])
        cnt = 0
    elif a == ')':
        tmp = stack.pop()
        cnt = cnt*tmp[1]+tmp[0]
    else:
        cnt += 1
        repeat= int(a)

print(cnt)