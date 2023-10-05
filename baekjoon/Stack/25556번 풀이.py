import sys

input = sys.stdin.readline

def solution():
    n = int(input())
    array = list(map(int, input().split()))

    stack = [[0] for _ in range(4)]

    for v in array:
        for s in stack:
            if s[-1] < v:
                s.append(v)
                break
        else:
            return 'NO'
    return 'YES'

print(solution())

