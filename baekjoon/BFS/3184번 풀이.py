import sys
from collections import deque
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

R, C = map(int, input().split())
f = []

for _ in range(R):
    f.append(list(f for f in input().strip()))

sheep, wolf = 0, 0
for i in range(R):
    for j in range(C):
        if f[i][j] != '#':
            q = deque([(i, j)])

            temp_wolf = 0
            temp_sheep = 0
            if f[i][j] == 'v':
                temp_wolf += 1
            elif f[i][j] == 'o':
                temp_sheep += 1
            f[i][j] = '#'

            while q:
                x, y = q.popleft()
                for idx in range(4):
                    nx = x + dx[idx]
                    ny = y + dy[idx]
                    if (0 <= nx <R) and (0 <= ny <C) and f[nx][ny] != '#':
                        if f[nx][ny] == 'v':
                            temp_wolf += 1
                        elif f[nx][ny] == 'o':
                            temp_sheep += 1
                        f[nx][ny] = '#'
                        q.append((nx, ny))

            if temp_sheep > temp_wolf:
                sheep += temp_sheep
            else:
                wolf += temp_wolf

print(sheep, wolf)


