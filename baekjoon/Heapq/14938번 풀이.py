import sys
import heapq

input = sys.stdin.readline


result = 0
n, m, r = map(int, input().split())
item_num = list(map(int, input().split()))
graph = [[] for _ in range(n)]

for _ in range(r):
    a, b, c = map(int, input().split())
    graph[a-1].append((b-1, c))
    graph[b-1].append((a-1, c))


for start in range(n):
    visted = [0]*n
    visted[start] = item_num[start]

    q = []
    heapq.heappush(q, (0, start))

    while q:
        n_cost, n_p = heapq.heappop(q)
        if n_cost > m:
            continue

        for nx in graph[n_p]:
            sum_cost = n_cost + nx[1]

            if sum_cost > m:
                continue

            if not visted[nx[0]]:
                visted[nx[0]] = item_num[nx[0]]
            heapq.heappush(q, (sum_cost, nx[0]))

    result = max(sum(visted), result)
print(result)