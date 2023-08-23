import re
s = re.compile('^[A-F]?A+F+C+[A-F]?$')

for _ in range(int(input())):
    print('Good' if s.match(input())==None else 'Infected!')