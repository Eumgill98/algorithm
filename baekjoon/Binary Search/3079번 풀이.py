import sys
input = sys.stdin.readline

n,m =map(int, input().split())
T = list(int(input()) for _ in range(n))

start = min(T)
end = max(T) * m
result = end + 1

while start <= end:
    mid = (start + end)  // 2

    peoples = 0 

    for i in range(n):
        peoples += mid // T[i]

    if peoples >= m :
        end = mid - 1
        result = min(result, mid)

    else:
        start = mid + 1
print(result)
