import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, k = map(int, input().split()) 
graph = [list(map(int, input().split())) for _ in range(n)]

s, r, z = map(int, input().split())


v = []
for i in range(n):
    for j in range(n):
        if graph[i][j]:
            v.append((graph[i][j], 0, i,j))


v.sort()
q = deque(v)

while q:
    v_n, t_s, x, y = q.popleft()

    if s == t_s:
        break

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if 0<=nx<n and 0<=ny<n:
            if not graph[nx][ny]:
                graph[nx][ny] = v_n
                q.append((v_n, t_s+1, nx, ny))

print(graph[r-1][z-1])