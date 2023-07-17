arr = []
for i in range(1,9):
    arr.append((int(input()),i))
arr.sort(reverse = True)

total = 0; rank = []
for score,n in arr[:5]:
    total+= score
    rank.append(n)
print(total)
print(*sorted(rank))