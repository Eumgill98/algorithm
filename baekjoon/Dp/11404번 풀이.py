import sys
input = sys.stdin.readline

n = int(input()) #num of city
m = int(input()) #num of bus

INF = int(1e9)

graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0


for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for g in range(1, n+1):
    g = map(lambda x: 0 if x==INF else x, graph[g][1:])
    print(*g)


