import sys

input = sys.stdin.readline

def solve(x):
    global result

    if len(array) == 2:
        result = max(result, x)
        return

    for i in range(1, len(array)-1):
        t = array[i-1] * array[i+1]

        temp = array.pop(i)
        solve(x+t)
        array.insert(i, temp)

n = int(input())
array = list(map(int, input().split()))
result = 0

solve(0)
print(result)
