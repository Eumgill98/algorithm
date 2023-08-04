import heapq

n, m = map(int, input().split())
heap = list(map(int, input().split()))

heapq.heapify(heap)

for _ in range(m):
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)

    tmp = a+b
    for _ in range(2):
        heapq.heappush(heap, tmp)


print(sum(heap))