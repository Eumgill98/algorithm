import sys
input = sys.stdin.readline

n = int(input())
want = int(input())


board = [[0]*n for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

x, y = n//2, n//2
num = 1
move = 0

save = (n//2 + 1, n//2 + 1)

board[x][y] = num

while True:

    for i in range(4):
        for _ in range(move):
            x += dx[i]
            y += dy[i]

            num += 1
            board[x][y] = num
            if num == want:
                save = (x+1, y+1)

    if x == y == 0:
        break

    x -= 1
    y -= 1
    move += 2


for b in board:
    print(*b)
print(*save)