n, w, l = map(int, input().split())
car = list(map(int, input().split()))

dp = [0] * w
c = 0
while True:
    if not car and sum(dp) == 0:
        break
    
    c += 1
    dp.pop(0)
    dp.append(0)

    if car and (sum(dp) + car[0]) <= l:
        dp[-1] = car.pop(0)


print(c)
        