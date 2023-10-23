import sys
from collections import Counter

input = sys.stdin.readline

n,m,b = map(int, input().split())
maps = list(list(map(int, input().split())) for _ in range(n))

idx, values = 0, sys.maxsize

for floor in range(257):
    max_t, min_t = 0, 0

    for i in range(n):
        for j in range(m):

            if maps[i][j] >= floor:
                max_t += maps[i][j] - floor

            else:
                min_t += floor - maps[i][j]

    if max_t + b >= min_t:
        if min_t + (max_t * 2) <= values:
            values = min_t+(max_t * 2)
            idx = floor
        
print(values, idx)

#python 시간 초과 -> pypy 제출 -> 브르투포스의 경우 시간초가 많이남
