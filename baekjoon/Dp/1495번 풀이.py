import sys
input = sys.stdin.readline

#n : 곡의 갯수, s : 시작 볼륨, m : 최대 볼륨

## 문제 조건1. 볼륨은 0 보다 작아 질 수 없고 m을 넘을 수 없다
## 문제 조건2. 음악 시작전 그 음악의 볼륨은 P(현재 볼륨) + V[i] or P - V[i]여야한다 -> 이때 i은 현재 음악의 순서
## 이때 마지막 곡이 될 수 있는 최대 볼륨은?

n, s, m = map(int, input().split())

V = list(map(int, input().split()))
dp = [[0]* (m+1) for _ in range(n+1)]

dp[0][s] = 1

for i in range(n):
    for j in range(m+1):
        if dp[i][j] == 1:
            if j + V[i] <=m:
                dp[i+1][j+V[i]] = 1
            
            if j - V[i] >=0:
                dp[i+1][j-V[i]] = 1

for idx in range(m, -1 , -1):
    if dp[n][idx] == 1:
        print(idx)
        break
else:
    print(-1)
    
