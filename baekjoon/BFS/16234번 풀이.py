from collections import deque
import sys
import copy

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, l, r = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))


def bfs(x, y):
    temp = [(x,y)]
    q = deque([(x, y)])

    vis[x][y] = 1
    people = graph[x][y]

    while q:
        x, y = q.popleft()
        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]
            if 0 <= nx < n and 0 <= ny < n and vis[nx][ny]==0:
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    vis[nx][ny] = 1
                    temp.append((nx, ny))
                    people += graph[nx][ny]
                    q.append((nx,ny))

    for x,y in temp:
        graph[x][y] = people // len(temp)

    return len(temp)

day = 0

while True:
    vis = [([0] * n) for f in range(n)]
    flag = 0
    for i in range(n):
        for j in range(n):
            if not vis[i][j]:
                if bfs(i, j) > 1:
                    flag=True

    if not flag:
        break
    else:
        day+=1


print(day)

