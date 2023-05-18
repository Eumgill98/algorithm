import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

n, m = map(int, input().split())
dp = []
q = deque()

for x in range(n):
    temp = list(map(int, input().split()))
    for y in range(m):
        if temp[y] == 1:
            q.append((x, y))
    dp.append(temp)

def bfs():
    while q:
        x, y = q.popleft()
        for idx in range(8):
            nx = x + dx[idx]
            ny = y + dy[idx]

            if 0 <= nx < n and 0<= ny <m and dp[nx][ny] == 0:
                q.append((nx, ny))
                dp[nx][ny] = dp[x][y] + 1

bfs()
print(max(map(max, dp)) - 1)



