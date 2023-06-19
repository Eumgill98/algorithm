from collections import defaultdict
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
group = defaultdict(list)

for _ in range(n):
    team = input().strip()

    len_member = int(input())
    for _ in range(len_member):
        group[team].append(input().strip())

for key in group.keys():
    group[key] = sorted(group[key])

for _ in range(m):
    q = input().strip()
    q_type = int(input())

    if q_type == 0:
        for member in group[q]:
            print(member)
    else:
        for key in group.keys():
            if q in group[key]:
                print(key)
                break
