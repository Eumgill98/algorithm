n = int(input())
store = list(map(int, input().split()))

now = -1
c = 0
for milk in store:
    if (now == -1 or now ==2) and milk == 0:
        c += 1
        now = milk
    elif now == 0 and milk == 1:
        c += 1
        now = milk
    elif now == 1 and milk == 2:
        c += 1
        now = milk


print(c)