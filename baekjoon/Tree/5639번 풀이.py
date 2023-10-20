# https://bottlenose-oak-2e3.notion.site/5639-02f6bb58755d43e7a85137af84d4753b?pvs=4
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



