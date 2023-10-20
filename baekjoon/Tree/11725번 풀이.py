import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [[] for i in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)

queue = deque()
queue.append(1)

result = [0] * (n+1)

def bfs():
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not (visited[i]):
                visited[i] = True
                queue.append(i)
                result[i] = v

bfs()

for j in range(2, n+1):
    print(result[j])

