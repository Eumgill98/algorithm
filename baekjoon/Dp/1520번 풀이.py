import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]


visited = [[-1]*n for _ in range(m)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    global c

    if x == m-1 and y == n-1:
        return 1
    
    if visited[x][y] != -1:
        return visited[x][y]

    visited[x][y] = 0

    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<= nx < m and 0<= ny <n and graph[nx][ny] < graph[x][y]:
            visited[x][y] += dfs(nx, ny)

    return visited[x][y]

print(dfs(0,0))