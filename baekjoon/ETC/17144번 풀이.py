import sys
from copy import deepcopy

input = sys.stdin.readline

r, c , t = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(r)]

for i in range(r):
    if graph[i][0] == -1:
        up = i
        down = i + 1
        break

def diffusion():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    tmp = [[0]* c for _ in range(r)]

    for i in range(r):
        for j in range(c):

            if graph[i][j] != 0 and graph[i][j] != -1:
                counts = 0

                for k in range(4):
                    nx = dx[k] + i
                    ny = dy[k] + j

                    if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] != -1:
                        tmp[nx][ny] += graph[i][j] // 5
                        counts += graph[i][j] // 5

                graph[i][j] -= counts
    for i in range(r):
        for j in range(c):
            graph[i][j] += tmp[i][j]

    

def air(opt='up'):
    if opt == 'up':
        dx = [0, -1, 0, 1]
        dy = [1, 0, -1, 0]
        x , y = up, 1
    else:
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        x , y = down, 1

    dir = 0
    before = 0

    while True:
        nx = x + dx[dir]
        ny = y + dy[dir]

        if opt == 'up':
            if x == up and y == 0:
                break
        else:
            if x == down and y == 0:
                break


        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            dir += 1
            continue
        graph[x][y], before = before, graph[x][y]
        x = nx
        y = ny

for _ in range(t):
    diffusion()
    air('up')
    air('down')

result = 0
for i in range(r):
    for j in range(c):
        if graph[i][j] > 0:
            result += graph[i][j]

print(result)


