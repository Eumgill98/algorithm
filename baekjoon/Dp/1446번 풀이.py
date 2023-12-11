# import sys

# input = sys.stdin.readline

# n, d = map(int, input().split())
# graph = [list(map(int, input().split())) for _ in range(n)]
# distance = [i for i in range(d + 1)]


# for i in range(d+1):
#     if i > 0:
#         distance[i] = min(distance[i], distance[i-1]+1)

#     for s, e, c in graph:
#         if i == s and e <= d and distance[i] + c < distance[e]:
#             distance[e] = distance[i] + c

# print(distance[d])

import sys
import heapq

input = sys.stdin.readline

INF = int(1e9)

def dijkstra():
    q = []
    heapq.heappush(q, (0, 0))
    distance[0] = 0

    while q:
       
        dist, now = heapq.heappop(q)

        if dist > distance[now]:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

n , d = map(int,input().split())
graph = [[] for _ in range(d+1)]
distance = [INF] * (d+1)

for i in range(d):
    graph[i].append((i+1, 1))

for _ in range(n):
    s, e, c = map(int, input().split())
    if e> d:
        continue
    graph[s].append((e, c))

dijkstra()
print(distance[d])
