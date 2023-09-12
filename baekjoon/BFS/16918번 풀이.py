import sys
from collections import deque

input = sys.stdin.readline


dx = [-1, 0, 1, 0]
dy = [0, 1, 0 ,-1]

q = deque()

R, C, N = map(int, input().split())

graph = [list(input().rstrip()) for _ in range(R)]

def bfs(q, graph):
    while q:
        x,y = q.popleft()
        graph[x][y] = '.'
        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]

            if 0<= nx < R and 0<= ny < C and graph[nx][ny] == 'O':
                graph[nx][ny] = '.'


def solution(t):
    global q, graph

    if t == 1:
        for i in range(R):
            for j in range(C):
                if graph[i][j] == 'O':
                    q.append((i, j))

    elif t%2 == 1:
        bfs(q, graph)
        for i in range(R):
            for j in range(C):
                if graph[i][j] == 'O':
                    q.append((i, j))

    else:
        graph = [ ['O']*C for _ in range(R)]

for i in range(1, N+1):
    solution(i)
    
for g in graph:
    print(''.join(g))