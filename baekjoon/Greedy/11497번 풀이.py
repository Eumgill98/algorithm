import sys

input = sys.stdin.readline

t = int(input())

for i in range(t):

    n = int(input())
    trees = list(map(int, input().split()))
    trees.sort()
    result= 0
    for j in range(2, n):
        result = max(result, abs(trees[j] - trees[j-2]))
    print(result)