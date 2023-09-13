import sys
from collections import Counter
input = sys.stdin.readline

result = {0:'invalid', 1:'valid'}

def check(list, string):
    if list[0] == list[1] == list[2] == string:
        return 1
    if list[0] == list[3] == list[6] == string:
        return 1
    if list[0] == list[4] == list[8] == string:
        return 1
    if list[1] == list[4] == list[7] == string:
        return 1
    if list[2] == list[5] == list[8] == string:
        return 1
    if list[3] == list[4] == list[5] == string:
        return 1
    if list[6] == list[7] == list[8] == string:
        return 1
    if list[2] == list[4] == list[6] == string:
        return 1
    return 0

while True:
    tictack = list(input().strip())

    if "".join(tictack) == 'end':
        break
    C = Counter(tictack)

    X = C['X']
    O = C['O']

    if X>O + 1 or O>X:
        print(result[0])
        continue

    if O==X:
        if check(tictack, 'O') and not check(tictack, 'X'):
            print(result[1])
            continue

    if O+1==X:
        if check(tictack, 'X') and not check(tictack, 'O'):
            print(result[1])
            continue
    
    if X==5 and O == 4:
        if not check(tictack, 'O'):
            print(result[1])
            continue

    print(result[0])