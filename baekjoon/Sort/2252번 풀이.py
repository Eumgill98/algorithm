from collections import deque
import sys

input = sys.stdin.readline
n, m = map(int, input().split())

maps = [[] for _ in range(n+1)]
degree = [0 for _ in range(n+1)]
q = deque()

result = []

for i in range(m):
    a, b = map(int, input().split())
    maps[a].append(b)
    degree[b] += 1

for i in range(1, n+1):
    if degree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    result.append(now)
    for i in maps[now]:
        degree[i] -= 1
        if degree[i] == 0:
            q.append(i)

print(*result)