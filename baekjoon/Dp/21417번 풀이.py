import sys
input = sys.stdin.readline

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
result= dp[-1]

for i in range(3, n):
    t, d1, d2 = dp[i-3]+k, 1e9, 1e9
    for j in range(i, n-1):

        if i+1 <= n:
            d1 = min(d1, t + values[j][0])
        if i+2 <= n:
            d2 = min(d2, t + values[j][1])

        t, d1, d2 = d1, d2, 1e9

    result = min(result, t)

print(result)