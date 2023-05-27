import sys
input = sys.stdin.readline

for _ in range(int(input())):
    s = (list(map(str, input().rstrip().split())))

    remove = []
    while True:
        s2 = input().rstrip()
        if s2 == 'what does the fox say?':
            break

        _, _, key = s2.split()
        remove.append(key)

    for i in s:
        if i not in remove:
            print(i, end=' ')