import sys

n, m = map(int, input().split())
array = list()
for _ in range(m):
    array.append(int(input()))

array.sort()

per = []
money = []

for i in range(m):
    temp = array[i]
    per.append(temp)
    if len(array[i::]) >= n:
        money.append(temp*n)
    else:
        money.append(temp*len(array[i::]))


print(per[money.index(max(money))], max(money))