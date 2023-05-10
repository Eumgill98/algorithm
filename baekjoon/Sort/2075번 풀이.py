import heapq

heap = []
n = int(input())

for _ in range(n):
    num = map(int, input().split())
    for ns in num:
        if len(heap)<n:
            heapq.heappush(heap, ns)
        else:
            if heap[0] < ns:
                heapq.heappop(heap)
                heapq.heappush(heap, ns)
print(heap[0])
