import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

def dfs(s):
    q = deque([dictionary[s]])
    while q:
        nt = q.popleft()
        if not visited[nt]:
            visited[nt] =1
            q.append(dictionary[nt])


for _ in range(n):
    s = int(input())
    dictionary = {k:0 for k in range(1, s+1)}
    array = list(map(int, input().split()))
    for i in range(1, s+1):
        dictionary[i] = array[i-1]

    visited = [0] * (s+1)
    c = 0

    for k in dictionary.keys():
        if not visited[k]:
            c +=1
            dfs(k)
    print(c)

