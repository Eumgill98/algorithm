n = int(input())
array = list(map(str, input().split()))

visited = [0]*10
max_num = ''
min_num = ''

def check(i, j, k):
    if k == '<':
        return i < j
    else:
        return  i > j

def dfs(depth, temp):
    global  max_num, min_num
    if depth == n+1:
        if len(min_num) == 0:
            min_num = temp
        else:
            max_num = temp
        return

    for i in range(10):
        if not visited[i]:
            if depth==0 or check(temp[-1], str(i), array[depth-1]):
                visited[i] = True
                dfs(depth+1, temp+str(i))
                visited[i] = False
dfs(0, '')
print(max_num)
print(min_num)