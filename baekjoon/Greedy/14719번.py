h, w = map(int, input().split())
array = list(map(int, input().split()))
c = 0

for i in range(1, w-1):
    left = max(array[:i])
    right = max(array[i+1:])

    verse = min(left, right)

    if array[i] < verse:
        c += verse - array[i]

print(c)