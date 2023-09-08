from collections import deque
import sys

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    global max_times
    q = deque([(x,y)])
    visted[x][y] = 1
    while q:
        x,y = q.popleft()

        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]
            if 0<=nx<a and 0<=ny<b and not visted[nx][ny] and maps[nx][ny] != 'W':
                visted[nx][ny] = visted[x][y] + 1
                max_times = max(max_times, visted[nx][ny])

                q.append((nx,ny))


a, b = map(int, input().split())
maps = []
max_times = -1

for _ in range(a):
    maps.append(list(input().rstrip()))
    

for i in range(a):
    for j in range(b):
        if maps[i][j] == 'L':
            visted = [[0]*b for _ in range(a)]
            bfs(i, j)
    
print(max_times-1)