from collections import deque
import sys

input = sys.stdin.readline

n,m = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

maps = []
for _ in range(n):
    maps.append(list(map(int, input().rstrip().split())))

cheese = True
c = 0

while cheese:
    vistied = [[0]*m for _ in range(n)]
    q = deque([(0,0)])
    vistied[0][0] = 1
    while q:
        x,y = q.popleft()
        
        for idx in range(4):
            nx = dx[idx] + x
            ny = dy[idx] + y

            if 0<=nx<n and 0<=ny<m:
                if maps[nx][ny] == 0 and not vistied[nx][ny]:
                    vistied[nx][ny] = 1
                    q.append((nx,ny))

                elif maps[nx][ny] == 1 and maps[x][y] == 0:
                    vistied[nx][ny] += vistied[x][y]

    for i in range(n):
        for j in range(m):
            if vistied[i][j] >= 2:
                maps[i][j] = 0
        
    tmp = 0
    for i in range(n):
        tmp += sum(maps[i])

    cheese = tmp
    c+=1
    
print(c)