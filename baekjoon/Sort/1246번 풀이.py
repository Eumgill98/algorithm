import sys

n, m = map(int, input().split())
array = list()
for _ in range(m):
    array.append(int(input()))

array.sort(reverse=True)

money = 0

for i in range(m):
    temp_c = 0
    temp_money = 0
    for j in range(m):
        if array[j] >= array[i]:
            temp_money += array[i]
            temp_c += 1
        
        if temp_c == n:
            break
    
    if money <= temp_money:
        money = temp_money
        per = array[i]

print(per, money)