'''
1. DFS로도 풀릴 것 같지만, 풀리지 않음. 접근하기 전에 반드시 생각해볼 것!
'''

import sys
from collections import deque



# 변수 선언
N,M = map(int,input().split())
Min = 10000000
rel = [[] for _ in range(N+1)] #relation
visited = [0]*(N+1)
kevin_num = 0

#BFS 방식
def BFS(start):
    q = deque()
    visited[start] = 1
    q.append((start,0))  #노드, depth
    kevin_num = 0
    while q:
        x,depth = q.popleft()
        for w in rel[x]:
            if not visited[w]:
                visited[w] =1
                q.append((w,depth+1))
                kevin_num += depth+1
    global answer,Min
    if(Min>kevin_num):
        Min = kevin_num
        answer = start


for i in range(M):
    x,y = map(int, sys.stdin.readline().split())
    rel[x].append(y)
    rel[y].append(x)

for i in range(1,N+1):
    visited = [0]*(N+1)
    BFS(i)

print(answer)