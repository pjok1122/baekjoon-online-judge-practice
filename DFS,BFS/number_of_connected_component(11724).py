# import sys
# sys.setrecursionlimit(10**6)

def DFS(start):
    visited[start]=1
    for w in edge[start]:
        if not visited[w]:
            DFS(w)

N,M = map(int,input().split())
edge = [[] for row in range(N+1)]
visited = [0]*(N+1)
for _ in range(M):
    x,y = map(int,input().split())
    edge[x].append(y)
    edge[y].append(x)

count = 0
for i in range(1,N+1):
    if not visited[i]:
        count+=1
        DFS(i)

print(count)