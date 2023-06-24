import sys
input = sys.stdin.readline

dp = [[0]*31 for _ in range(31)]

#h만 있는 경우, 경우의 수는 1가지 밖에 없음
for h in range(1, 31):
    dp[0][h] = 1

for w in range(1, 31):
    for h in range(30):
        if h == 0:
            dp[w][h] = dp[w-1][h+1]

        else:
            dp[w][h] = dp[w-1][h+1] + dp[w][h-1]

while True:
    n = int(input())
    if n == 0:
        break

    print(dp[n][0])




