import sys
input = sys.stdin.readline

n = int(input())

before = dict()
c = 0

for idx in range(n):
    car = input().strip()
    before[car] = idx

for idx in range(n):
    out_car = input().strip()
    if idx != before[out_car]:
        for car in before:
            if (idx <= before[car] <= before[out_car]) and car != out_car:
                before[car] += 1
        before[out_car] = idx
        c += 1

print(c)
