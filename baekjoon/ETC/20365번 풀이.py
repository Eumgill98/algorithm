n = int(input())
array = input()

result = {'R':0, 'B':0}
result[array[0]] += 1

for idx in range(1, n):
    if array[idx-1] != array[idx]:
       
        result[array[idx]] += 1

print(min(result['R'], result['B']) + 1)