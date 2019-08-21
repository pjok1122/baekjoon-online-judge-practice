# from queue import Queue
from collections import deque
from sys import stdin
input = stdin.readline

def BFS(x, y, e_x,e_y, visited):
    # que = Queue()
    que = deque()
    visited[x][y] = 1
    step = 0
    # que.put((x,y,step))
    que.append((x,y,step))
    dx=[-1,-2,-2,-1,1,2,1,2]
    dy=[-2,-1,1,2,-2,-1,2,1]

    while que: #que.qsize()
        #x, y, step = que.get()
        x, y, step = que.popleft()
        if (x,y) ==(e_x,e_y):
            print(step)
            return 
        for i in range(8):
            nx,ny = x+dx[i], y+dy[i]
            if (nx<0 or ny<0 or nx>=L or ny>=L):
                continue
            if not visited[nx][ny]:
                visited[nx][ny] = 1
                # que.put((nx,ny,step+1))
                que.append((nx,ny,step+1))

T = int(input())

for test_case in range(T):
    L = int(input())
    
    s_x, s_y = map(int, input().split())
    e_x, e_y = map(int, input().split())
    visited = [[0]*L for row in range(L)]

    BFS(s_x,s_y, e_x,e_y, visited)
