import sys

input = sys.stdin.readline

n, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
distance = [i for i in range(d + 1)]


for i in range(d+1):
    if i > 0:
        distance[i] = min(distance[i], distance[i-1]+1)

    for s, e, c in graph:
        if i == s and e <= d and distance[i] + c < distance[e]:
            distance[e] = distance[i] + c

print(distance[d])
print(distance)