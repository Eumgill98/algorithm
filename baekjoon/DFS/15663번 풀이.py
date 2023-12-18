import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s = []
check = set()

n_list = sorted(list(map(int, input().split())))
indexing = {k:v for k, v in enumerate(n_list)}


def dfs():
    if len(s) == m:
        tmp = ' '.join(map(str,[indexing[x] for x in s]))
        if tmp not in check:
            print(tmp)
            check.add(tmp)
        return

    for idx in range(len(n_list)):
        if idx not in s:        
            s.append(idx)
            dfs()
            s.pop()

dfs()