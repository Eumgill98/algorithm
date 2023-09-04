import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n+1)]

while True:
    a, b = map(int, input().split())
    
    if a == -1 :
        break

    graph[a].append(b)
    graph[b].append(a)


def bfs(x):
    q = deque([x])
    vis[x] = True
    while q:
        point = q.popleft()
        for i in graph[point]:
            if not vis[i]:
                vis[i] = True
                dp[i] = dp[point] + 1
                q.append(i)

president = 51 
result = []
for i in range(1, n+1):
    dp = [0]*(n+1)
    vis = [False]*(n+1)

    bfs(i)

    if max(dp) < president:
        result = [i]
        president = max(dp)
    elif max(dp) == president:
        result.append(i)


print(president, len(result))
print(*result)

