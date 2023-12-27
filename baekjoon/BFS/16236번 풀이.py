import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
graph = []
for i in range(N):
    tmp = list(map(int, input().split()))

    #check shark
    for j in range(N):
        if tmp[j] == 9:
            x, y = i, j

    graph.append(tmp)


dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

shark_size = 2

def bfs(x,y,shark_size):
    distance = [[0] * N for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    q = deque([(x,y)])
    visited[x][y] = 1

    tmp_result = []
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0<= ny <N and visited[nx][ny] == 0:
                # 작거나 같은 경우만 지나갈 수 있음
                if graph[nx][ny] <= shark_size:
                    visited[nx][ny] = 1
                    distance[nx][ny] = distance[x][y] + 1
                    
                    q.append((nx, ny))
                    #eat 할 수 있는 경우
                    if graph[nx][ny] < shark_size and graph[nx][ny] != 0:
                        tmp_result.append((nx, ny, distance[nx][ny])) # 위 기준, 왼쪽 기준, 거리 기준

    if not len(tmp_result):
        return None
    else:
        return sorted(tmp_result, key=lambda x : (-x[2], -x[0], -x[1]))[-1]

result = 0
cnt = 0
while True:

    x_y = bfs(x, y, shark_size)


    if x_y is None:
        print(result)
        break

    nx, ny, dist = x_y

    #update
    result += dist
    graph[x][y], graph[nx][ny] = 0, 0

    x,y = nx, ny
    cnt += 1
    if cnt == shark_size:
        shark_size += 1
        cnt = 0
