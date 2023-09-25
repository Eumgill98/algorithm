import sys
from collections import deque

input = sys.stdin.readline

board = [list(input().strip()) for _ in range(12)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

#구현해야할 기능 1 : 위,아래, 양옆에 같은 블록이 도합 4개이면 펑

#구현해야할 기능 2 : 사라진 블록이 있으면 그 위에 있는 블록이 아래에 값이 있을때 까지 내려오게하기


def make_bomb(x, y):
    visited = [[0]*6 for _ in range(12)]
    q = deque([(x,y)])
    visited[x][y] = 1

    bomb_list = [(x,y)]

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0<= nx <12 and 0<= ny <6 and not visited[nx][ny] and board[nx][ny] == board[x][y]:
                visited[nx][ny] = 1
                q.append((nx,ny))
                bomb_list.append((nx,ny))

    if len(bomb_list) >= 4:
        return bomb_list


def bomb(bomb_list):
    for x,y in bomb_list:
        board[x][y] = '.'

def gravity():
    for y in range(6):
        queue = deque()
        for x in range(11, -1, -1):
            if board[x][y] != '.':
                queue.append(board[x][y])
        for x in range(11, -1, -1):
            if queue:
                board[x][y] = queue.popleft()
            else:
                board[x][y] = '.'

result = 0

while True:
    flag = 0
    for i in range(12):
        for j in range(6):
            if board[i][j] != '.':
                bomb_list = make_bomb(i, j)

                if bomb_list:
                    bomb(bomb_list)
                    flag = 1
    if not flag:
        break

    gravity()
    result += 1 


print(result)  