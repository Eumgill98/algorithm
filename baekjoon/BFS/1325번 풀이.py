import sys
from collections import deque
input = sys.stdin.readline


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

def bfs(x):
    c = 1
    q = deque([x])
    visited[x] = 1
    while q:
        x = q.popleft()
        
        for next in graph[x]:
            if not visited[next]:
                visited[next] = 1
                c += 1
                q.append(next)
    return c

        
max_c = 0
result = []

for point in range(1, n+1):
    visited = [0] * (n+1)
    tmp = bfs(point)

    if tmp > max_c:
        result = [point]
        max_c = tmp

    elif tmp == max_c:
        result.append(point)

print(*result)

    
