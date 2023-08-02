import math
n = int(input())
array = [0 if math.sqrt(i) != int(math.sqrt(i)) else 1 for i in range(n + 1)]

result = 4
for i in range(int(math.sqrt(n)), 0, -1):
    if array[n] :
        result = 1
        break
    elif array[n-(i**2)]:
        result = 2
        break
    else:
        for j in range(int(math.sqrt((n-(i**2)))), 0, -1):
            if array[(n-(i**2)-(j**2))]:
                result = 3


print(result)