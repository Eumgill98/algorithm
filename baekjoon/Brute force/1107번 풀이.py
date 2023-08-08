n = int(input())
m = int(input())
if m :
    not_working = list(map(str, input().split()))
else:
    not_working = list()

min_c = abs(100 - n)

for num in range(1000001):

    for t_s in str(num):
        if t_s in not_working:
            break
    else:
        min_c = min(min_c, abs(num - n) + len(str(num)))

print(min_c)
