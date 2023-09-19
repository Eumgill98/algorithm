n = input()
k=0

for i in range(len(n)):
    k+=(int(n)-(10**i)+1)
print(k)
