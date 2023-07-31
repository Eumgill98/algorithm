from collections import deque

n = int(input())

r1, c1, r2, c2 = map(int, input().split())

visited = [[-1]*n for f in range(n)] 


dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]

q = deque([(r1, c1)])
visited[r1][c1] = 0 

while q:
    x, y= q.popleft()
    
    for idx in range(6):
        nx = x + dx[idx]
        ny = y + dy[idx]
        
        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1:

            visited[nx][ny] = visited[x][y] + 1
            q.append((nx, ny))


print(visited[r2][c2])

