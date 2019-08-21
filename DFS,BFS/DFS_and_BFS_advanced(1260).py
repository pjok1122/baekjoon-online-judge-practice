
from queue import Queue

def DFS(start, visited): #Complex : O(m) 
    visited[start] = 1
    print(start, end=' ')
    for i in edge[start]:  # Complex : deg(i)
        if not visited[i]:
            DFS(i, visited)

def BFS(start, visited,que):
    visited[start] = 1
    que.put(start)
    print(start, end=' ')
    while que.qsize():
        v = que.get()
        for i in edge[v]: # Complex : deg(i)
            if not visited[i]:
                visited[i] = 1
                que.put(i)
                print(i, end=' ')

N,M,start = map(int,input().split())

edge = [ [] for row in range(N+1)]
visited =[0 for row in range(N+1)]
que = Queue(1000)
for _ in range(M):
    s,e = map(int,input().split())
    # edge[s][e], edge[e][s] = 1,1
    edge[s].append(e)
    edge[e].append(s)

for i in range(N):
    edge[i].sort()

DFS(start, visited)
visited =[0 for row in range(N+1)]
print()
BFS(start, visited, que)