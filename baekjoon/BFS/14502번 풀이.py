import sys
from collections import deque
from itertools import combinations
from copy import deepcopy

input = sys.stdin.readline

def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = 1

    while q:
        x, y = q.popleft()

        for idx in range(4):
            
            nx = x + dx[idx]
            ny = y + dy[idx]
            
            if 0 <= nx <n and 0<= ny < m and new_graph[nx][ny] == 0 and not visited[nx][ny]:
                new_graph[nx][ny] = 2
                visited[nx][ny] = 1

                q.append((nx, ny))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n, m = map(int, input().split())
max_count = 0

graph = []
zero_point = []

for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(m):
        if tmp[j] == 0:
            zero_point.append((i, j))

    graph.append(tmp)


for select in combinations(zero_point, 3):
    new_graph = deepcopy(graph)
    for i, j in select:
        new_graph[i][j] = 1
    
    visited = [[0]*m for _ in range(n)]

    for x in range(n):
        for y in range(m):
            
            if new_graph[x][y] == 2 and not visited[x][y]:

                bfs(x, y)

    #check 0 구역
    c = 0
    for g in new_graph:
        c += g.count(0)
    max_count = max(max_count, c)

print(max_count)  
    


