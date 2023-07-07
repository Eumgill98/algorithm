a, b = map(int, input().split(":"))

def gcd(a,b):
    while b> 0:
        a,b = b, a%b
    return a

temp = gcd(a, b)

print(f'{a//temp}:{b//temp}')