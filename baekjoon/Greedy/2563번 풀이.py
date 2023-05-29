n = int(input())
dp = [[0]*100 for f in range(100)]
c = 0
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x-1, x+9):
        for j in range(y-1, y+9):
            if dp[i][j] == 0:
                dp[i][j] =1
                c+=1


print(c)