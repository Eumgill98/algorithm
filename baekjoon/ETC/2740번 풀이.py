import sys
input = sys.stdin.readline

a_n, a_m = map(int, input().split())
a = []
for _ in range(a_n):
    a.append(list(map(int, input().rstrip().split())))

b_n, b_m = map(int, input().split())
b = []
for _ in range(b_n):
    b.append(list(map(int, input().rstrip().split())))

c = [[0 for _ in range(b_m)] for _ in range(a_n)]

for n in range(a_n):
    for k in range(b_m):
        for m in range(b_n):
            c[n][k] += a[n][m] * b[m][k]

for i in c:
    for j in i:
        print(j, end = ' ')
    print()