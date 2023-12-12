import sys
import heapq

input = sys.stdin.readline

v,e = map(int, input().split()) # point num, #nood num
k = int(input()) # start point

INF = 1e9
dist = [INF]*v
graph = [[] for _ in range(v)]

for _ in range(e):
    a,b,w = map(int, input().split())

    graph[a-1].append((b-1, w))


q = []
heapq.heappush(q, (0, k-1)) #cost, start_point
dist[k-1] = 0

while q:
    cost, n_p = heapq.heappop(q)

    if dist[n_p] < cost:
        continue

    for new_p, weight in graph[n_p]:
        sum_cost = cost + weight

        if sum_cost < dist[new_p]:
            dist[new_p] = sum_cost
            heapq.heappush(q, (sum_cost, new_p))

for value in dist:
    if value == INF:
        print('INF')
    else:
        print(value)