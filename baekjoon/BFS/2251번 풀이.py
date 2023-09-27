from collections import deque

def visit(x, y):
    if not visited[x][y]:
        visited[x][y] = 1
        q.append((x,y))


def bfs():
    q.append((0,0))
    visited[0][0] = 1

    while q:
        x, y = q.popleft()
        z = c - x - y

        if x == 0:
            result.append(z)


        #a -> b
        if x > 0 and y < b:
            w = min(x, b - y)
            visit(x - w, y + w)
        
        #a -> c
        if x > 0 and z < c:
            w = min(x, c - z)
            visit(x - w, y)

        #b -> a
        if y > 0 and x < a:
            w = min(y, a - x)
            visit(x + w, y - w)
        
        #b -> c
        if y > 0 and z < c:
            w = min(y, c - z)
            visit(x, y - w)

        # c -> a
        if z > 0 and x < a:
            w = min(z, a - x)
            visit(x + w, y)

        # c -> b
        if z > 0 and y < b:
            w = min(z, b - y)
            visit(x, y + w)


a,b,c = map(int, input().split())

result= []

visited = [[0]*(b+1) for _ in range(a+1)]

q = deque()
bfs()

result.sort()
print(*result)

