
num_str = input()

cnt = 0

for i in range(len(num_str)-1):
    if num_str[i] != num_str[i+1]:
        cnt+=1

print((cnt+1) // 2)



#다른풀이

c=input().count
print(c('01'))
print(max(c("01"),c("10")))