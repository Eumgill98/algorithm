import sys

input = sys.stdin.readline

N, B = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

def mul(U, V):
    n = len(U)
    z_m = [[0]*n for _ in range(n)]

    for row in range(n):
        for col in range(n):
            e = 0
            for i in range(n):
                e += U[row][i] * V[i][col]
            z_m[row][col] = e %  1000

    return z_m

def sol(A, B):
    if B == 1:
        for x in range(len(A)):
            for y in range(len(A)):
                A[x][y] %= 1000
        return A

    tmp = sol(A, B//2)
    
    if B % 2:
        return mul(mul(tmp, tmp), A)
    else:
        return mul(tmp, tmp)
    
result = sol(A, B)

for r in result:
    print(*r)