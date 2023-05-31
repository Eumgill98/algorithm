import sys
input = sys.stdin.readline

n = int(input())
dp_a = [0]* (n+1)
dp_b = [0]* (n+1)

dp_a[0] = 1

for idx in range(1, n+1):
    dp_a[idx] = dp_b[idx-1]
    dp_b[idx] = dp_a[idx-1] + dp_b[idx-1]

print(dp_a[n], dp_b[n])