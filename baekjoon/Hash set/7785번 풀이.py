from collections import defaultdict
import sys

input = sys.stdin.readline

n = int(input())
office = defaultdict()

for _ in range(n):
    human, what = map(str, input().rstrip().split())
    office[human] = what

offices = sorted(office, reverse=True)

for key in offices:
    if office[key] == 'enter':
        print(key)