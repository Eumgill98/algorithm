#최대 증가 수열을 찾아주면 ok
import sys
input = sys.stdin.readline

n = int(input())

array = [0]*501

for _ in range(n):
    a, b = map(int, input().split())
    array[a] = b 
    

#lis
dp = [1 for f in range(501)]

for i in range(501):
    for j in range(i):
        if array[i] > array[j] and array[j] != 0:
            dp[i] = max(dp[j]+1, dp[i])

print(n - max(dp))