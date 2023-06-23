n = int(input())
array = list(set(list(map(int, input().split()))))
array.sort()

print(*array)

