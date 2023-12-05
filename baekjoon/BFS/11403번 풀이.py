import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]

def bfs(x):
    q = deque()
    q.append(x)
    check = [0 for _ in range(n)]

    while q:
        i = q.popleft()

        for j in range(n):
            if check[j] == 0 and graph[i][j] == 1:
                q.append(j)
                check[j] = 1
                visited[x][j] = 1

for i in range(0, n):
    bfs(i)

for i in visited:
    print(*i)