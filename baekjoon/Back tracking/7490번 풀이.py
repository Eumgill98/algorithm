import sys
input = sys.stdin.readline


def backtracking(a, s, c):
    global array
    global n
    global result
    if c == n:
        if sum(a) == 0:
            result.append(s)
            
        return 

    #+
    a.append(array[c])
    backtracking(a, s+'+'+str(array[c]) ,c+1)
    a.pop()

    #-
    a.append(-array[c])
    backtracking(a, s+'-'+str(array[c]), c+1)
    a.pop()

    #' '
    a.append(int(str(a.pop())+str(array[c])))
    backtracking(a, s+' '+str(array[c]), c+1)

    


c = int(input())
for _ in range(c):
    n = int(input())

    result = []
    array = list(f for f in range(1, n+1))
    num =[array[0]]
    backtracking(num, str(array[0]), 1)

    for i in sorted(result):
        print(i)
    print('')