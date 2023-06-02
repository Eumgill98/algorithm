import sys
input = sys.stdin.readline
#
# array = []
# m_t = 0
# for _ in range(int(input())):
#     x, y = tuple(map(int, input().split()))
#     array.append((x,y))
#     m_t = max(m_t, y)
#
# array = sorted(array)
# dp = [[0]*(m_t+1)]
#
# for idx in array:
#     flag = 0
#     x,y = idx
#     for room in dp:
#         if room[x+1] == 0 and room[y-1] == 0:
#             for i in range(x, y+1):
#                 room[i] = 1
#             flag = 1
#             break
#     if flag == 1:
#         pass
#     else:
#         temp = [0]*(m_t+1)
#         for i in range(x, y+1):
#             temp[i] = 1
#         dp.append(temp)
#
# print(len(dp))
"""
메모리 초과
"""


import heapq

n = int(input())

q = []

for i in range(n):
    start, end = map(int, input().split())
    q.append([start, end])

q.sort()

room = []
heapq.heappush(room, q[0][1])

for i in range(1, n):
    if q[i][0] < room[0]: # 현재 회의실 끝나는 시간보다 다음 회의 시작시간이 빠르면
        heapq.heappush(room, q[i][1]) # 새로운 회의실 개설

    else: # 현재 회의실에 이어서 회의 개최 가능
        heapq.heappop(room) # 새로운 회의로 시간 변경을 위해 pop후 새 시간 push
        heapq.heappush(room, q[i][1])


print(len(room))

