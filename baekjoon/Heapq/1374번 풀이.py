import sys
import heapq

input = sys.stdin.readline

q = []

n = int(input())
array = list(list(map(int, input().split())) for _ in range(n))
array.sort(key = lambda x:x[1])

#end time
heapq.heappush(q, array[0][2])

for i in range(1, n):
    if array[i][1] < q[0]:
        heapq.heappush(q, array[i][2])
    else:
        heapq.heappop(q)
        heapq.heappush(q, array[i][2])

print(len(q))


