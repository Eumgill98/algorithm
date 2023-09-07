n = int(input())

result = []
x, y = 1, 1

while x+y<= n:
    temp =  (x+y)*(x-y)

    if temp== n:
        result.append(x)
        x += 1
    
    elif temp > n:
        y += 1
    
    else:
        x += 1

if not result:
    print(-1)
else:
    print(*result, sep='\n')
