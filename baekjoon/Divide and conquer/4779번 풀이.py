def cal(array, start, len):
    t = len // 3
    if t == 0:
        return
    for i in range(start + t, start+t *2):
        array[i] = ' '
    cal(array, start, t)
    cal(array, start + t * 2, t)

while True:
    try:
        n = int(input())
        array = ['-'] * (3 ** n)
        cal(array, 0, len(array))
        print(''.join(array))
    except EOFError:
        break

