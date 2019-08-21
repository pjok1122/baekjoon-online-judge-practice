
from queue import Queue

def DFS(start, N, visited):
    visited[start] = 1
    print(start, end=' ')
    for i in range(1,N+1): #O(n)
        if (edge[start][i] and not visited[i]): #O(n)
            DFS(i, N, visited)
def BFS(start, N, visited,que):
    que.put(start)
    visited[start] = 1
    print(start, end=' ')
    while que.qsize():
        v = que.get()
        for i in range(1,N+1):
            if(edge[v][i] and not visited[i]):
                que.put(i)
                visited[i] = 1
                print(i, end=' ')

N,M,start = map(int,input().split())

edge = [[0 for col in range(N+1)] for row in range(N+1) ] 
visited =[0 for row in range(N+1)]
que = Queue(1000)
for _ in range(M):
    s,e = map(int,input().split())
    edge[s][e], edge[e][s] = 1,1

DFS(start, N, visited)
visited =[0 for row in range(N+1)]
print()
BFS(start, N, visited, que)