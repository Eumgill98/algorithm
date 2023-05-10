import sys
input = sys.stdin.readline

n, m = map(int , input().split())

a = []
b = []
c = 0

for _ in range(n):
    a.append(list(input().strip()))

for _ in range(n):
    b.append(list(input().strip()))

for i in range(n):
    for j in range(m):
        if a[i][j] != b[i][j]:
            try:
                for k in range(3):
                    for f in range(3):
                        if a[i+k][j+f] == '0':
                            a[i+k][j+f] ='1'
                        else:
                            a[i+k][j+f] = '0'
            except:
                print(-1)
                exit()
            c += 1

print(c)