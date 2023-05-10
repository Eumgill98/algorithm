import sys
input = sys.stdin.readline

n = int(input())
li = []
for _ in range(n):
	li.append(int(input()))
max_n = max(li)
dp = [0, 1, 2, 4] + [0] * (max_n-3)
for i in range(4, max_n+1):
	dp[i] = (dp[i-3] + dp[i-2] + dp[i-1])%1000000009
for num in li:
	print(dp[num])


##메모리는 더 먹어도 조금 더 빠른
dp = [1,2,4,7]
for i in range(int(input())):
    n = int(input())
    for j in range(len(dp), n):
        dp.append((dp[-3]+dp[-2]+dp[-1])%1000000009)
    print(dp[n-1])