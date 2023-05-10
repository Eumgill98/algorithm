import sys
input = sys.stdin.readline

n = int(input())
citys = []
for _ in range(n):
    citys.append(list(map(int, input().split())))

min_cost = sys.maxsize

def dfs(start, deth, target, cost):
    global  min_cost
    if deth == n:
        if citys[target][start]:
            cost += citys[target][start]
            min_cost = min(min_cost, cost)
        return

    if cost > min_cost:
        return

    for i in range(n):
        if not visited[i] and citys[target][i]:
            visited[i] = 1
            dfs(start, deth+1, i, cost+citys[target][i])
            visited[i] = 0

visited = [0] * n
for t in range(n):
    visited[t] = 1
    dfs(t, 1, t, 0)
    visited[t] = 0

print(min_cost)