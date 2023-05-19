import sys
from collections import deque

input = sys.stdin.readline
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(int(f) for f in input().rstrip()))

def bfs(x, y):
    q = deque([(x, y)])

    graph[x][y] = 2
    while q:
        x, y = q.popleft()
        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]
            if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 0:
                graph[nx][ny] = 2
                q.append((nx, ny))

for t in range(m):
    if graph[0][t] == 0:

        bfs(0, t)

if 2 not in graph[-1]:
    print('NO')
else:
    print('YES')