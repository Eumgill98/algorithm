n = int(input())
c = 0

while True:
    if n % 5 == 0:
        c += n//5
        break
    else:
        n -= 2
        c += 1

    if n <0:
        break

if n<0:
    print(-1)
else:
    print(c)