s = input()
s_array  = []
for i in range(len(s)):
    s_array.append(s[i:])

print(*sorted(s_array), sep="\n")