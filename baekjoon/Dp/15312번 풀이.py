A = input()
B = input()
alpha = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]

dp = []

for i in range(len(A)):
    dp.append(alpha[ord(A[i]) - 65])
    dp.append(alpha[ord(B[i]) - 65])

while True:
    tmp = []
    for i in range(len(dp) - 1):
        tmp.append((dp[i]+ dp[i+1]) % 10)

    dp = tmp
    if len(dp) == 2:
        break

print("".join(list(map(str,dp))))