import sys
from collections import deque

n,m = map(int, input().split())
count = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = []
maps = []


for i in range(n):
    values = list(f for f in input().strip())
    temp = []
    for j, key in enumerate(values):
        if key == 'X':
            temp.append(1)
        else:
            if key == 'I':
                start = (i, j)
            temp.append(0)
    maps.append(values)
    visited.append(temp)


q = deque([start])

visited[start[0]][start[1]] = 1

while q:
    x, y = q.popleft()
    for idx in range(4):
        nx = x + dx[idx]
        ny = y + dy[idx]
        if 0<=nx<n and 0<=ny<m and visited[nx][ny]==0:
            q.append((nx, ny))
            visited[nx][ny] = 1

            if maps[nx][ny] == 'P':
                count += 1
    
if count == 0:
    print('TT')
else:
    print(count)
