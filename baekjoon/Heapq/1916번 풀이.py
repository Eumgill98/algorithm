import heapq
import sys

input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    s, e, c = map(int, input().split())
    graph[s].append([e, c])

start, end = map(int, input().split())
costs = [1e9 for _ in range(N+1)]

heap = []
costs[start] = 0
heapq.heappush(heap, [0, start])

while heap:
    
    cur_cost, cur_v = heapq.heappop(heap)

    if costs[cur_v] < cur_cost:
        continue
    for next_v, next_cost in graph[cur_v]:
        sum_cost = cur_cost + next_cost

        if sum_cost >= costs[next_v]:
            continue

        costs[next_v] = sum_cost
        heapq.heappush(heap, [sum_cost, next_v])

print(costs[end])
