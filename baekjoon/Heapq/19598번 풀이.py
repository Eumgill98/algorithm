import heapq
import sys

input = sys.stdin.readline

n = int(input())
array  = []
for _ in range(n):
    array.append(tuple(map(int, input().split())))
array.sort()

heap = []
for time in array:
    if not heap:
        heapq.heappush(heap, time[1])

    else:
        if time[0] < heap[0]:
            heapq.heappush(heap, time[1])
        else:
            heapq.heappop(heap)
            heapq.heappush(heap, time[1])

print(len(heap))