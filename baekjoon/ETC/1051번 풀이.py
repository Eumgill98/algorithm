import sys

input= sys.stdin.readline

n,m = map(int, input().split())
size = min(n, m) 

board = [list(map(int, input().rstrip(3))) for _ in range(n)]


def check(k):
    for i in range(n-k+1):
        for j in range(m-k+1):
            if board[i][j] == board[i][j+k-1] == board[i+k-1][j] == board[i+k-1][j+k-1]:
                return True
    return False

for num in range(size, 0, -1):
    if check(num):
        print(num**2)
        break