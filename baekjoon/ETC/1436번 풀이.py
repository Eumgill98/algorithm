N = int(input())
first = 666
while True:
    if '666' in str(first):
        N = N-1
    if N == 0:
        break
    first = first + 1
print(first)