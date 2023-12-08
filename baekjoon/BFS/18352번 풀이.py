import sys
from collections import deque

input = sys.stdin.readline

n, m, k, x = map(int, input().split())

road = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    road[a].append(b)


def bfs(x):
    q = deque([x])
    distance = [-1] * (n+1)
    distance[x] = 0

    while q:
        x = q.popleft()

        for i in road[x]:
            if distance[i]== -1:
                distance[i] = distance[x] + 1

                q.append(i)
    
    if k not in distance:
        print(-1)
    else:
        for i in range(len(distance)):
            if distance[i] == k:
                print(i)

bfs(x)


