import heapq
import sys

input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

i = 1
INF =  1e9
while True:
    n = int(input())
    if n == 0:
        break
    
    maps = [list(map(int, input().split())) for _ in range(n)]
    cost_map = [[INF]*n for _ in range(n)]
    q = []
    heapq.heappush(q, (maps[0][0], (0,0))) # (cost, next_xy)
    cost_map[0][0] = maps[0][0]

    while q:
        cost, (x, y) = heapq.heappop(q)
        if cost_map[x][y] < cost:
            continue

        for idx in range(4):
            nx = dx[idx] + x
            ny = dy[idx] + y

            if 0<= nx < n and 0<= ny < n:
                sum_cost = cost + maps[nx][ny]

                if sum_cost >= cost_map[nx][ny]:
                    continue
                
                cost_map[nx][ny] = sum_cost
                heapq.heappush(q, (sum_cost, (nx,ny)))

    result = cost_map[-1][-1]
    print(f'Problem {i}: {result}')
    i += 1