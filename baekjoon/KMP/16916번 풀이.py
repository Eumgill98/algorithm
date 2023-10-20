import sys

class kmp:
    def __init__(self, verse, v):
        self.verse = verse
        self.v = v

    def kmp_table(self):
        table = [0 for _ in range(len(self.v))]
        i = 0
        for j in range(1, len(self.v)):
            
            #i가 0이 되거나, v[i]와 v[j]가 같아 질때 까지 이전 같았던 값까지 i 조정
            while i >0 and self.v[i] != self.v[j]:
                i = table[i - 1]
            #만약 i,j의 문자가 같다면 i를 1증가 시키고 증가시킨값을 table[j]로 저장
            if self.v[i] == self.v[j]:
                i += 1
                table[j] = i
        
        return table

    def progress(self):
        table = self.kmp_table()
        print(table)
        result = 0
        i = 0
        for j in range(len(self.verse)):
            while i>0 and self.v[i] != self.verse[j]:
                i = table[i-1]
            
            if self.v[i] == self.verse[j]:
                i += 1
                if i == len(self.v):
                    result +=1
                    i = table[i-1]
        
        return result

input = sys.stdin.readline
verse = input().strip()
v = input().strip()

solve = kmp(verse, v)
result = solve.progress()

if result == 0:
    print(result)
else:
    print(1)