import sys

input = sys.stdin.readline

def cal(graph):
    new_graph = []
    max_row = 0
    for idx in range(len(graph)):
        tmp = []
        row = graph[idx][:]

        for num in set(row):
            if num == 0: continue
            cnt = row.count(num)
            tmp.append((num, cnt))

        tmp = sorted(tmp, key=lambda x:[x[1], x[0]])
        
        new_row = []
       
        for num, cnt in tmp:
            new_row += [num, cnt]
        new_graph.append(new_row)
        max_row = max(max_row, len(new_row))

    for row in new_graph: 
        row += [0] * (max_row - len(row))
        if len(row) > 100: row = row[:100] 

    return new_graph

def main():
    r, c, k = map(int, input().split())
    graph = list(list(map(int, input().split())) for _ in range(3))
    time = 0

    while True:
        if r-1 < len(graph) and c-1 < len(graph[0]):
            if graph[r-1][c-1] == k:
                return time
            
        if len(graph) >= len(graph[0]):
            graph = cal(graph)
        else:
            graph = cal(list(map(list, zip(*graph))))
            graph = list(map(list, zip(*graph)))

        time += 1

        if time > 100:
            return -1
        

print(main())