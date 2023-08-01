import sys

input = sys.stdin.readline

n, k = map(int, input().split())

levels = list(int(input()) for _ in range(n))

start = min(levels)
end = start + k

result = 0
while start <= end:
    mid = (start + end) // 2

    res = 0
    for level in levels:
        if mid > level:
            res += (mid - level)
    
    if res <= k:
        start = mid + 1
        result = max(result, mid)

    else:
        end = mid - 1 

print(result)