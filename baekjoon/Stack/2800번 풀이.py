import sys
from itertools import combinations
from copy import deepcopy

input = sys.stdin.readline

array = list(input().strip())
result = set()
stack = []
c = []

for idx, v in enumerate(array):
    if v == '(':
        stack.append(idx)
    
    elif v == ')':
        x_y = (stack.pop(), idx)
        c.append(x_y)


for i in range(1, len(c)+1):
    com = combinations(c, i)
        
    for j in com:
        
        target = deepcopy(array)
        for k in j:
            target[k[0]] = ""
            target[k[1]] = ""

        result.add(''.join(target))


for r in sorted(list(result)):
    print(r)