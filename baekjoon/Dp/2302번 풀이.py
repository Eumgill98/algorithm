import sys

input= sys.stdin.readline

dp = [0]*41
dp[0] = 1
dp[1] = 1

for i in range(2, 41):
    dp[i] = dp[i-1] + dp[i-2]

n = int(input())
m = int(input())
array = [0]*(n+1)

for _ in range(m):
    key = int(input())
    array[key] = 1

result = 1
tmp = 0
for idx in range(1, n+1):
    if not array[idx]:
        tmp += 1
    elif array[idx]:
        result *= dp[tmp]
        tmp = 0

if tmp:
    result *= dp[tmp]

print(result)
