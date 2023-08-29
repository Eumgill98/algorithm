import sys
input = sys.stdin.readline

S = list(input().rstrip())
T = list(input().rstrip())

flag = 0 
while T:
    if T[-1] == 'A':
        T.pop()
    elif T[-1] == 'B':
        T.pop()
        T = T[::-1]
    
    if T == S:
        flag = 1
        break


print(flag)