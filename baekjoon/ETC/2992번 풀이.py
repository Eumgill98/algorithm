from itertools import permutations

n = list(input())
permu = (sorted(set(map(lambda x: ''.join(x), permutations(n, len(n))))))

print(0) if permu[-1] == ''.join(n) else print(permu[permu.index(''.join(n)) + 1])
