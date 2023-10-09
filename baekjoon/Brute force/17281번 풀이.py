import sys
from collections import deque
from itertools import permutations

input = sys.stdin.readline

n = int(input())
inning = list(list(map(int, input().split())) for _ in range(n))

max_score = 0

def play(lineup):
    hitter = 0
    score = 0

    for inn in inning:
        out = 0
        b1, b2, b3 = 0, 0, 0
        while out < 3:
            if inn[lineup[hitter]] == 0:
                out += 1

            elif inn[lineup[hitter]] == 1:
                score += b3
                b1, b2, b3 = 1, b1, b2
            elif inn[lineup[hitter]] == 2:
                score += (b2 + b3)
                b1, b2, b3 = 0, 1, b1
            elif inn[lineup[hitter]] == 3:
                score += (b2 + b3 + b1)
                b1, b2, b3 = 0, 0, 1
            elif inn[lineup[hitter]] == 4:
                score += (1 + b1 + b2 + b3)
                b1, b2, b3 =0, 0, 0

            hitter = (hitter + 1) % 9
    return score

for lineup in permutations(range(1,9), 8):
    lineup = list(lineup[:3]) + [0] + list(lineup[3:])
    max_score = max(max_score, play(lineup))

print(max_score)