n = int(input())
array = sorted(list(map(int,input().split())))
total = 0

while len(array) > 1:
    a = array.pop()
    b = array.pop()
    c = a+b 

    array.append(c)
    total += (a * b)

print(total)

