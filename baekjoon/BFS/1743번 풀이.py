import sys
from collections import deque

input = sys.stdin.readline 

n, m, f = map(int, input().split())
dp = list([0] * m for i in range(n)) 

for _ in range(f):
    x, y = map(int, input().split())
    dp[x-1][y-1] = 1

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


total = 0

for i in range(n):
    for j in range(m):
        if dp[i][j]:
            q = deque([(i, j)])
            dp[i][j] = 2
            c= 1

            while q:
                x, y = q.popleft()
                for idx in range(4):
                    nx = x + dx[idx]
                    ny = y + dy[idx]
                    if 0 <= nx <n and 0 <= ny <m and dp[nx][ny] == 1:
                        q.append((nx, ny))
                        dp[nx][ny] = 2
                        c += 1
            total = max(c, total)
                        
        
            
print(total)
        

