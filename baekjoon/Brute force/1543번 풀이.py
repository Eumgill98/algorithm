import sys
input = sys.stdin.readline

doc = input().rstrip()
verse = input().rstrip()

result = doc.split(verse)
print(len(result) - 1)

