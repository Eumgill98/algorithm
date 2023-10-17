import sys
input = sys.stdin.readline
from copy import deepcopy

n = int(input())
dp = [0]+ [1e9]*(n-1)
values = []

for i in range(n-1):
    s, l = map(int, input().split())
    values.append((s, l))

    if i + 1 < n:
        dp[i+1] = min(dp[i+1], dp[i]+s)

    
    if i + 2 < n:
        dp[i+2] = min(dp[i+2], dp[i]+l)

k = int(input())

result = dp[-1]
dp2 = deepcopy(dp)

for i in range(0, n-3):
    if dp[i] + k < dp[i+3]:
        dp2[i+3] = dp[i]+k
        for j in range(i+4, n):
            dp2[j] = min(dp[j], dp2[j-1]+values[j-1][0], dp2[j-2]+values[j-2][1])

        result = min(result, dp2[-1])

print(result) 