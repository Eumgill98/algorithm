import sys
input = sys.stdin.readline

a, b = map(int, input().split())

array = []
for _ in range(a):
    array.append(list(f for f in input().strip()))

total = []
for i in range(a):
    temp = []
    flag = 0
    for j in range(b):
        if array[i][j] == 'c':
            temp.append(0)
            flag = 1
        elif array[i][j] == '.' and flag:
            temp.append(flag)
            flag += 1
        elif array[i][j] == '.' and not flag:
            temp.append(-1)

    total.append(temp)

for ar in total:
    print(*ar)