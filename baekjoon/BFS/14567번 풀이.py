import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split()) #n : 과목수, m : 선수 과목 조건 수

dp = [-1] * (n+1)
visited = [0]*(n+1)
classes = {f:[] for f in range(1, n+1)}
for _ in range(m):
    a, b = map(int, input().split())
    classes[b].append(a)

def bfs(st):
    if not classes[st]:
        dp[st] = 1
        visited[st] = 1
    else:
        for key in classes[st]:
            if not visited[key]:
                bfs(key)
            else:
                dp[st] = max(dp[st], dp[key] + 1)
                visited[st] = 1

for i in range(1, n+1):
    if not visited[i]:
        bfs(i)

for i in range(1, n+1):
    print(dp[i], end=' ')
