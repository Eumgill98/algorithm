n = int(input())

array = sorted(list(map(int, input().split())))

if n % 2 == 0:
    print(array[n//2 - 1])
else:
    print(array[n//2])