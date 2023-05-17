from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
result = []

def bfs(graph, start):
    num = [0] * (n+1)
    visited = [start]
    q = deque([start])

    while q:
        a = q.popleft()
        for i in graph[a]:
            if i not in visited:
                num[i] = num[a] + 1
                visited.append(i)
                q.append(i)
    return sum(num)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    result.append(bfs(graph, i))

print(result.index(min(result))+1)


