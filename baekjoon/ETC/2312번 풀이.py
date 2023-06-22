from collections import defaultdict
import sys

input = sys.stdin.readline

n = int(input())

def factor(x, defa):
    d = 2
    while d <= x:
        if x % d == 0:
            defa[d] += 1
            x = x//d
        else:
            d = d + 1

for _ in range(n):
    de = defaultdict(int)
    num = int(input())
    factor(num, de)

    for key in de.keys():
        print(key, de[key])

