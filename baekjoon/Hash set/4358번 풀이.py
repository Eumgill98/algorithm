import sys
input = sys.stdin.readline

trees = {}
c = 0
while True:
    tree = input().strip()
    if not tree:
        break
    if tree in trees:
        trees[tree] += 1
    else:
        trees[tree] = 1
    c += 1

for key in sorted(trees):
    print('%s %.4f' %(key, trees[key]/c*100))

## defaultdict를 쓴다면
from collections import defaultdict
import sys
input = sys.stdin.readline

trees = defaultdict(int)
c = 0

while True:
    tree = input().strip()
    if not tree:
        break
    trees[tree] += 1
    c += 1

for key in sorted(trees):
    print('%s %.4f' %(key, trees[key]/c*100))
