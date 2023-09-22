import sys
sys.setrecursionlimit(10**6)

array = []
while True:
    try:
        n = int(input())
        array.append(n)
    except:
        break

def postorder(f, e):
    if f > e:
        return
    
    m = e + 1

    for i in range(f+1, e+1):
        if array[f] < array[i]:
            m = i
            break

    postorder(f+1, m-1)
    postorder(m, e)
    print(array[f])

postorder(0, len(array)-1)