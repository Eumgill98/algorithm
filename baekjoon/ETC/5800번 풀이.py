n = int(input())

for i in range(n):
    array = list(map(int, input().split()))
    num = array.pop(0)

    array.sort(reverse=True)
    max_gap = -1
    for j in range(num-1):
        temp_gap = array[j] - array[j+1]
        max_gap = max(max_gap, temp_gap)

    print(f'Class {i+1}')
    print(f'Max {max(array)}, Min {min(array)}, Largest gap {max_gap}')