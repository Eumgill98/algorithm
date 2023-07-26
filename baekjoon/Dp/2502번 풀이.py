from collections import deque
d, k = map(int, input().split())

Daily = deque(0 for f in range(d-2))
one, two = 1, 1
while True:
    Daily = deque(0 for f in range(d-2))
    Daily.appendleft(two)
    Daily.appendleft(one)

    for idx in range(2, d):
        Daily[idx] = Daily[idx-2] + Daily[idx-1]

    if Daily[-1] > k:
        two -= 1
        one += 1
    elif Daily[-1] < k:
        two += 1
    else:
        break
    

print(one)
print(two)

