import sys
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n,m = map(int, input().split())
board = list(list(map(int, input().split())) for _ in range(n))
visited = list([0]*m for _ in range(n))

result = 0

def dfs(i, j, sum_value, cnt):
    global result

    if cnt == 4:
        result = max(result, sum_value)
        return
    
    for idx in range(4):
        nx = i + dx[idx]
        ny = j + dy[idx]

        if 0<= nx < n and 0 <= ny < m and not visited[nx][ny]:
            visited[nx][ny] = 1
            dfs(nx, ny, sum_value+board[nx][ny], cnt+1)
            visited[nx][ny] = 0

def other(i, j):
    global result

    for t in range(4):
        sum_value = board[i][j]
        for k in range(3):
            idx = (t+k)% 4
            nx = i + dx[idx]
            ny = j + dy[idx]

            if not (0 <= nx < n and 0 <= ny < m):
                sum_value = 0
                break

            sum_value += board[nx][ny]

        result = max(result, sum_value)


for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(i, j, board[i][j], 1)
        visited[i][j] = 0

        other(i, j)


print(result)