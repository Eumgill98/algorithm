import sys

input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))

min_moeny = array[0]
result = 0

for i in range(1, n):
    if min_money < array[i]:
        result = max(result, array[i]-min_money)
    else:
        min_money = array[i]
print(result)
  
    