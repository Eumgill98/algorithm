import sys
input = sys.stdin.readline

N = int(input())

def moo(acc, cur, N): # n번째 전체길이, 가운데 부분 길이, N
    pre = (acc-cur) // 2

    if N <= pre:
        return moo(pre, cur-1, N)
    elif N > pre+cur:
        return moo(pre, cur-1, N-pre-cur)
    else:
        return "o" if N-pre-1 else "m"

acc, n = 3, 0 

while N > acc:
    n += 1
    acc = acc * 2 + n + 3

print(moo(acc, n+3, N))