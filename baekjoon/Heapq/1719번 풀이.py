import sys
import heapq

input = sys.stdin.readline

def dijkstra(start, n):
    global dists, res

    q = []
    for i in range(n):
        if i == start:
            continue
        heapq.heappush(q, (dists[start][i], i))

    while q:
        dist, node = heapq.heappop(q)

        if dists[start][node] < dist:
            continue
        for n_p in range(n):
            if node == n_p or start == n_p:
                continue
            sum_node = dist + dists[node][n_p]

            if sum_node < dists[start][n_p]:
                dists[start][n_p] = sum_node
                heapq.heappush(q, (sum_node, n_p))
                # node로 가는 첫 번째 집하장을 neighbor 경로에 저장
                res[start][n_p] = res[start][node]

n, m = map(int, input().split())

INF = 1e9
dists = list(([INF] * (n)) for _ in range(n))
res = [['-'] * (n) for _ in range(n)]


for _ in range(m):
    a, b, c = map(int, input().split())
    dists[a-1][b-1] = dists[b-1][a-1] = c
    res[a-1][b-1] = str(b)
    res[b-1][a-1] = str(a)

for i in range(n):
    dijkstra(i, n)

for r in res:
    print(*r)