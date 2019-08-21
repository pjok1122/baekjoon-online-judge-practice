from queue import Queue

def BFS(start,que,visited):
    que.put(start)
    while que.qsize():
        v = que.get()
        for w in edge[v]: #O(M)
            if not visited[w]:
                visited[w]=1

                que.put(w)
def DFS(start,visited):
    for w in edge[start]:
        if not visited[w]:
            visited[w] = 1
            DFS(w, visited)


#데이터 전처리
N = int(input())
edge = [[] for row in range(N)]
for i in range(N): #O(N^2)
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j]:
            edge[i].append(j)


# 알고리즘 로직 : O(n * m)
for i in range(N):
    visited = [0 for row in range(N)]
    DFS(i,visited)
    print(' '.join(map(str,visited)))
