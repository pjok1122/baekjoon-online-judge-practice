from queue import Queue

def BFS(start,que,visited,result):
    if visited[start]:
        return None
    que.put(start)
    visited[start] = 1
    result[start][start] = 1

    while que.qsize():
        v = que.get()
        for w in edge[v]: #O(M)
            if not visited[w]:
                visited[w]=1
                result[v][w], result[w][v] = 1, 1
                que.put(w)

N = int(input())
edge = [[] for row in range(N)]
visited = [0 for row in range(N)]
result = [ [0 for col in range(N)] for row in range(N)]
que = Queue()
for i in range(N): #O(N^2)
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j]:
            edge[i].append(j)

for i in range(N): #O(n)
    BFS(i, que, visited, result)

for i in range(N):
    for j in range(N):
        print(result[i][j], end=' ')
    print()
