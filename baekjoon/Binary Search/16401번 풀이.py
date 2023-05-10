import sys
input = sys.stdin.readline

n, m = map(int,input().split())
cookies = list(map(int, input().split()))

start = 1
end = int(1e9)
result = 0
while start <= end:
    mid = (start + end) // 2

    temp = 0
    for cookie in cookies:
        temp += cookie // mid

    if temp >= n:
        start = mid + 1
        result = mid
    else:
        end = mid - 1


print(result)