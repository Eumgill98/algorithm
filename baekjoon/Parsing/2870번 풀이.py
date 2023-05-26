import sys
input = sys.stdin.readline

n = int(input())
total = []
for _ in range(n):
    s = input().rstrip()
    stack=''
    for i in s:
        if i.isalpha() and stack != '':
            total.append(int(stack))
            stack=''
        elif not i.isalpha():
            stack += i

    if stack:
        total.append(int(stack))
print(*sorted(total), sep='\n')