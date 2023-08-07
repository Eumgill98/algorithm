import sys
from itertools import combinations
from collections import deque, defaultdict

input = sys.stdin.readline

def bfs(zone):
    start = zone[0]
    q = deque([start])
    visited = set([start])
    total = 0

    while q:
        now = q.popleft()
        total += people[now]
        for _next in maps[now]:
            if _next not in visited and _next in zone:
                q.append(_next)
                visited.add(_next)
    return total, len(visited)


n = int(input())
people = list(map(int, input().rstrip().split()))
maps= defaultdict(list)
for i in range(n):
    connect = list(map(int, input().rstrip().split()))
    for j in range(1, connect[0] + 1):
        maps[i].append(connect[j]-1)

result = int(1e9)

#combinations로 랜덤으로 a,b 선거구나누기
for i in range(1, n//2 + 1):
    for com in combinations(range(n), i):
        group1, v1= bfs(com)
        group2, v2= bfs([i for i in range(n) if i not in com])
        if v1 + v2 == n:
            result = min(result, abs(group1 - group2))

if result == int(1e9):
    print(-1)
else:
    print(result)
