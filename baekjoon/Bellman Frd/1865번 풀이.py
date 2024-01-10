import sys

input = sys.stdin.readline
INF = 1e9

def bf(start):
    distance = [INF] * (N+1)
    distance[start] = 0

    for i in range(N):
        for edge in edges:
            cur = edge[0]
            next_node = edge[1]
            cost = edge[2]

            if distance[next_node] > cost + distance[cur]:
                distance[next_node] = cost+distance[cur]

                if i == N - 1:
                    return True 
    return False

T  = int(input())

for _ in range(T):
    N, M, W = map(int, input().split())

    edges = []

    for _ in range(M):
        s, e, t = map(int, input().split())
        edges.append((s, e, t))
        edges.append((e, s, t))

    for _ in range(W):
        s, e, t = map(int, input().split())
        edges.append((s, e, -t))


    if bf(1):
        print("YES")
        break
    else:
        print("NO")