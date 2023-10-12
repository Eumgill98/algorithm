import sys

input = sys.stdin.readline

result = 0
n, m = map(int, input().split())
if n == 1:
    result = 1

elif n == 2:
    if 1 <= m <= 6:
        result = (m+1) // 2
    else:
        result = 4

else:
    if m <= 6:
        result = min(m, 4)
    else:
        result = m - 2

print(result)
