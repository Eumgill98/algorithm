import sys

input = sys.stdin.readline

n = int(input())

array = []

for _ in range(n):
    n,d,m,y = input().rstrip().split()
    d,m,y = int(d), int(m), int(y)
    array.append((y,m,d,n))

array.sort()
print(array[-1][3])
print(array[0][3])