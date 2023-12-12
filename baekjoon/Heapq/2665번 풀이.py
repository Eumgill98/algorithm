import heapq
import sys

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0 ,-1, 1]

INF = 1e9

n = int(input())
cost = [[INF]*n for _ in range(n)]
graph = [[int(f) for f in input().strip()] for _ in range(n)]
cost[0][0] = 0

q = []
heapq.heappush(q, (0, (0,0)))
while q:
    n_cost, (x,y) = heapq.heappop(q)
    
    for idx in range(4):
        nx = dx[idx] + x
        ny = dy[idx] + y
        
        if 0<=nx<n and 0<=ny<n:
            if graph[nx][ny] == 0:
                sum_cost = n_cost + 1
            else:
                sum_cost = n_cost

            if sum_cost >= cost[nx][ny]:
                continue
            cost[nx][ny] = sum_cost
            heapq.heappush(q, (sum_cost, (nx,ny)))

print(cost[-1][-1])