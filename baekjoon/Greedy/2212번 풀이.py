import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

if k >= n:
    print(0)
    exit()

sense = sorted(list(map(int, input().split())))

dist = []
for idx in range(1, n):
    dist.append(sense[idx] - sense[idx-1])

dist.sort(reverse=True)
for _ in range(k-1):
    dist.pop(0)

print(sum(dist))