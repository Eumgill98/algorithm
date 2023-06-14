from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

visited = [0] * (n+1)
graph = [[] for f in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(x):
    q = deque()
    visited[x] = 1
    q.append(x)
    while q:
        next = q.popleft()
        for i in graph[next]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = visited[next]+1

bfs(1)
c = 0
for idx in range(2, n+1):
    if 1 < visited[idx] < 4:
        c+=1

print(c)