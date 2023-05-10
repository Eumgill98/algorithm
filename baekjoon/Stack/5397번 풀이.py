import sys
input = sys.stdin.readline

for _ in range(int(input())):
	key = input().rstrip()
	left, right = [], []
	for typ in key:
		if typ == '<':
			if left:
				right.append(left.pop())
		elif typ == '>':
			if right:
				left.append(right.pop())
		elif typ == '-':
			if left:
				left.pop()
		else:
			left.append(typ)
	left.extend(reversed(right))
	print(''.join(left))