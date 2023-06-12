from collections import deque
import sys

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

m, n = map(int, input().split())
world = []
for _ in range(n):
    world.append(list(f for f in input().rstrip()))

visited = [[0]*m for f in range(n)]
w_score, b_score = 0, 0

def bfs(a,b):
    q = deque([(a,b)])

    visited[a][b] = 1
    c = 1
    key = world[a][b]
    while q:
        x,y = q.popleft()
        for idx in range(4):
            nx = dx[idx] + x
            ny = dy[idx] + y
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and world[nx][ny] == key:
                c += 1
                visited[nx][ny] = 1
                q.append([nx, ny])
    return c ** 2

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            temp = bfs(i,j)
            if world[i][j] == 'B':
                b_score += temp
            else:
                w_score += temp

print(w_score, b_score)


