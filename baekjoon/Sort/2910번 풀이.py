from collections import Counter
n, c = map(int, input().split())
array = list(map(int, input().split()))

c = sorted(Counter(array).items(), key=lambda x: x[1], reverse=True)
for k, l in c:
    for _ in range(l):
        print(k, end=' ')