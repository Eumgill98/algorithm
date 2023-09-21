import math

def one_solution(n, k):
    if len(answer) == N -1:
        answer.append(array[-1])
        return

    num = math.factorial(n) // n
    idx = math.ceil(k / num)
    answer.append(array.pop(idx))

    one_solution(n-1, k-(num*(idx-1)))    
    

def two_solution():
    n = N

    for num in q_v:
        num_c = math.factorial(n) // n
        idx = array.index(num)

        if len(array) == 2:
            idx += 1
            answer.append(num_c*idx)
            return
        
        array.pop(idx)
        answer.append(num_c*idx)
        n -= 1


N = int(input())
q = list(map(int, input().split()))

q_k = q[0]
q_v = q[1:]
answer = []

if q_k == 1:
    array = [f for f in range(N+1)]
    one_solution(N, q_v[0])
    print(*answer)

else:
    array = [f for f in range(1, N+1)]
    two_solution()
    print(sum(answer))


