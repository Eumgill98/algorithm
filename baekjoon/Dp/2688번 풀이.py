for _ in range(int(input())):
    n = int(input())
    dp = [1 for _ in range(10)]

    for _ in range(n-1):
        for j in range(10):
            dp[j] = sum(dp[j:])

    print(sum(dp))